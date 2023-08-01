import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

from Wszystkie_funkcje.Appro import approximation
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
    roots = [4, 6, 10, 15, 20, 30, 40, 50]
    roots = sorted(roots)
    return roots


def calculate_error():
    m = [2, 3, 4, 5, 6, 7, 8, 10, 15, 25]
    roots = roots_maker()
    # Tworzenie list na bledy
    result_max = [None for _ in range(len(roots) * len(m))]
    result_sq = [None for _ in range(len(roots) * len(m))]
    # Tworzenie wektora X
    X1 = np.linspace(-4, 4 + 0.01, 800)
    # obliczanie wartosci funkcji w wektorze X
    function_value = fun(X1)
    idx = 0
    # Petla obliczajaca bledy
    for n in roots:
        X = np.linspace(-4, 4 + 0.01, n)
        Y = fun(X)
        for i in m:
            ls_approximation = approximation(X, Y, i)
            ls_approximation_result = ls_approximation(X1)
            result_max[idx] = round(max_error(ls_approximation_result, function_value), 2)
            result_sq[idx] = round(sum_square_error(ls_approximation_result, function_value), 2)
            idx += 1

    return roots, result_max, result_sq, m


def do_table():
    roots, result_max, result_sq, m = calculate_error()

    # Tworzy słownik z błędami
    dict = {"Liczba węzłów": [i for i in roots for _ in range(len(m))],
                  "Stopień wielomianu": m * len(roots),
                  "Błąd maksymalny": result_max,
                  "Błąd średniokwadratowy": result_sq}

    # tworzy data frame z modulu pandas
    df_result = pd.DataFrame(dict)
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
