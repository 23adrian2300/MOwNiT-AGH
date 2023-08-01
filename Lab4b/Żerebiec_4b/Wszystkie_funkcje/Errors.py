import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from Wszystkie_funkcje.Appro import Trig_Apro
from Wszystkie_funkcje.Function import *


# funkcja obliczajaca bledy maksymalne
def max_error(interpolation_values, function_values):
    errors = []
    for i in range(len(interpolation_values)):
        error = abs(interpolation_values[i] - function_values[i])
        errors.append(error)
    return max(errors)


# funkcja obliczajaca bledy srednio-kwadratowe
def sum_square_error(interpolation_values, function_values):
    errors = []
    for i in range(len(interpolation_values)):
        error = (interpolation_values[i] - function_values[i]) ** 2
        errors.append(error)
    return sum(errors)


def roots_maker():
    roots = [10, 20, 50, 100, 200, 1000]
    roots = sorted(roots)
    return roots


def calculate_error():
    nodes = roots_maker()
    m = [i for i in range(1, 50)]
    result = [None for _ in range(2 * len(m) * len(nodes))]
    total_X = np.linspace(-4, 4, 800)
    func_val = fun(total_X)
    idx = 0
    for n in nodes:
        X = np.linspace(-4, 4, n)
        Y = fun(X)
        for i in m:
            if i > np.floor((n - 1) / 2):
                result[idx] = None
                result[idx + 1] = None
            else:
                trigonometric_approximation = Trig_Apro(X, Y, i)
                trig_appr_result = trigonometric_approximation.approximation(total_X)
                result[idx] = max_error(trig_appr_result, func_val)
                result[idx + 1] = sum_square_error(trig_appr_result, func_val)
            idx += 2

    return nodes, result, m


def find_best_max():
    total_X = np.linspace(-4, 4, 800)
    func_val = fun(total_X)
    o, p = 0, 0
    oo, pp = 0, 0
    k = float("inf")
    l = float("inf")
    for n in range(201):
        X = np.linspace(-4, 4, n)
        Y = fun(X)
        for i in range(200):
            if i < np.floor((n - 1) / 2):
                trigonometric_approximation = Trig_Apro(X, Y, i)
                trig_appr_result = trigonometric_approximation.approximation(total_X)
                mmm = max_error(trig_appr_result, func_val)
                sql = sum_square_error(trig_appr_result, func_val)
                print(n, i)
                if mmm < k:
                    k = mmm
                    o = n
                    p = i
                if sql < l:
                    l = sql
                    oo = n
                    pp = i
    print("result:")
    print("max", k, "roots", o, "st:", p, "sql:", l, "roots", oo, "st:", pp)


def do_table(function):
    roots, result, m = calculate_error()

    # Tworzy słownik z błędami
    error_dict = {"Liczba węzłów": [val for val in roots for _ in range(len(m))],
                  "Stopień wielomianu": m * len(roots),
                  "Błąd maksymalny": result[::2],
                  "Błąd średniokwadratowy": result[1::2]}

    # tworzy data frame z modulu pandas
    df_result = pd.DataFrame(error_dict)
    # formatuje kolumny
    first_col_format = lambda x: f"{int(x):d}"
    float_col_format = lambda x: f"{x:.2e}" if x > 1000 else f"{x:.2f}"
    df_result_formatted = df_result.copy()
    df_result_formatted.iloc[:, 0:2] = df_result_formatted.iloc[:, 0:2].applymap(first_col_format)
    df_result_formatted.iloc[:, 2:] = df_result_formatted.iloc[:, 2:].applymap(float_col_format)
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
    plt.savefig(f".\\Wykresy\\Tabela błędów aproksymacji.jpg", dpi=1000, bbox_inches='tight')
