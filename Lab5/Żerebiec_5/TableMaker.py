import pandas as pd
from matplotlib import pyplot as plt

pd.options.display.float_format = "{:,.12f}".format
from Metods import *

def function(x):
    y = 40* x * np.e ** (-8) - 40 * np.e ** (-8 * x) + 1/40
    return y


def der_function(x):
    n = 8
    m = 40
    y = m * np.e ** (-n) + n * m * np.e ** (-n * x)
    return y

def calculate(method_name, epsilon, max_no_iterations, condition):
    X = np.arange(-0.2, 2 + 0.1, 0.1)
    result = []
    for x_0 in X:
        x_0 = round(x_0, 2)
        if method_name == "newton":
            x, n = newton(function, der_function, x_0, epsilon, max_no_iterations, condition)
            if x == None or x == np.inf or x == np.nan:
                result += [x, n, x_0]
            else:
                result += [round(x,8), n, x_0]
        elif method_name == "secant":
            x, n = secant(function, x_0, 2, epsilon, max_no_iterations, condition)
            x_0 = round(x_0, 2)
            if x == None or x == np.inf or x == np.nan:
                result += [x, n, f"[{x_0}, 2]"]
            else:
                result += [round(x,8), n, f"[{x_0}, 2]"]
            x, n = secant(function, -0.2, x_0, epsilon, max_no_iterations, condition)
            if x == None or x == np.inf or x == np.nan:
                result += [x, n, f"[-0.2, {x_0}]"]
            else:
                result += [round(x,8), n,f"[-0.2, {x_0}]"]

    for i in range(len(result)):
        if result[i] == None or result[i] == np.inf or result[i] == np.nan:
            result[i] =  "-"
    df = pd.DataFrame(data={"Miejsce zerowe": result[::3],
                            "Liczba iteracji": result[1::3],
                            "x": result[2::3]})
    df_result = pd.DataFrame(df)
    df_result_formatted = df_result.copy()

    cell_text = df_result_formatted.values
    table = plt.table(cellText=cell_text, colLabels=df_result.columns, loc='center', cellLoc='center')
    table[0, 0].get_text().set_color('red')
    table[0, 0].get_text().set_weight('bold')
    table[0, 0].set_linestyle('solid')
    table[0, 0].set_linewidth(2)
    for j in range(1, df_result.shape[1]):
        table[0, j].get_text().set_color('red')
        table[0, j].get_text().set_weight('bold')
        table[0, j].set_linestyle('solid')
        table[0, j].set_linewidth(2)
    for i in range(1, df_result.shape[0]):
        for j in range(df_result.shape[1]):
            table[i, j].get_text().set_color('black')
            table[i, j].get_text().set_weight('normal')
    table.auto_set_column_width(col=list(range(df_result.shape[1])))
    plt.axis('off')
    plt.savefig(f".\\Wykresy\\Zadanie_1_Wyniki_{method_name}_{condition}_{epsilon}.jpg", dpi=1000, bbox_inches='tight')
    return df

