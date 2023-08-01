import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from Wszystkie_funkcje.Function import *
from Wszystkie_funkcje.Spline import *


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
    roots = [i for i in range(4, 30)]
    roots1 = [40, 50, 60, 70, 80, 90, 100]
    roots2 = [i for i in range(30, 40)]
    roots = roots + roots1 + roots2
    roots = sorted(roots)
    return roots


def calculate_error_cubic():
    roots = roots_maker()
    res_cubic_natural_max = [None for _ in range(len(roots))]
    res_cubic_cubic_max = [None for _ in range(len(roots))]
    res_cubic_natural_sum = [None for _ in range(len(roots))]
    res_cubic_cubic_sum = [None for _ in range(len(roots))]
    total_X = np.linspace(-4, 4, 800)
    func_val = fun(total_X)
    idx = 0
    for n in roots:
        X = np.linspace(-4, 4, n)
        Y = fun(X)
        nat_cubic_spline = cubic_spline(X, Y, "natural")
        nat_cubic_result = [item for sublist in nat_cubic_spline(total_X) for item in sublist]
        res_cubic_natural_max[idx] = max_error(nat_cubic_result, func_val)
        res_cubic_natural_sum[idx] = sum_square_error(nat_cubic_result, func_val)

        cub_cubic_spline = cubic_spline(X, Y, "cubic")
        cub_cubic_result = [item for sublist in cub_cubic_spline(total_X) for item in sublist]
        res_cubic_cubic_max[idx] = max_error(cub_cubic_result, func_val)
        res_cubic_cubic_sum[idx] = sum_square_error(cub_cubic_result, func_val)

        idx += 1
    result = [[]] * 4
    result[0] = res_cubic_natural_max
    result[1] = res_cubic_natural_sum
    result[2] = res_cubic_cubic_max
    result[3] = res_cubic_cubic_sum

    return result


def calculate_error_quad():
    roots = roots_maker()
    res_quad_natural_max = [None for _ in range(len(roots))]
    res_quad_clamped_max = [None for _ in range(len(roots))]
    res_quad_natural_sum = [None for _ in range(len(roots))]
    res_quad_clamped_sum = [None for _ in range(len(roots))]

    total_X = np.linspace(-4, 4, 800)
    func_val = fun(total_X)
    idx = 0

    for n in roots:
        X = np.linspace(-4, 4, n)
        Y = fun(X)

        nat_quadr_spline = quadratic_spline(X, Y, "natural")
        res_quad_natural_max[idx] = max_error(nat_quadr_spline(total_X), func_val)
        res_quad_natural_sum[idx] = sum_square_error(nat_quadr_spline(total_X), func_val)

        cla_quadr_spline = quadratic_spline(X, Y, "clamped")
        res_quad_clamped_max[idx] = max_error(cla_quadr_spline(total_X), func_val)
        res_quad_clamped_sum[idx] = sum_square_error(cla_quadr_spline(total_X), func_val)
        idx += 1
    result = [[]] * 4
    result[0] = res_quad_natural_max
    result[1] = res_quad_natural_sum
    result[2] = res_quad_clamped_max
    result[3] = res_quad_clamped_sum
    return result


def do_table_cubic():
    nodes = roots_maker()
    result = calculate_error_cubic()
    error_dict = {"Liczba węzłów": nodes,
                  "Natural - maksymalny": result[0],
                  "Natural - średniokwadratowy": result[1],
                  "Cubic - maksymalny": result[2],
                  "Cubic - średniokwadratowy": result[3]}

    # tworzy data frame z modulu pandas
    df_result = pd.DataFrame(error_dict)
    # formatuje kolumny
    first_col_format = lambda x: f"{int(x):d}"
    float_col_format = lambda x: f"{x:.2e}" if x > 1000 else f"{x:.2f}"
    df_result_formatted = df_result.copy()
    df_result_formatted.iloc[:, 0] = df_result_formatted.iloc[:, 0].apply(first_col_format)
    df_result_formatted.iloc[:, 1:] = df_result_formatted.iloc[:, 1:].applymap(float_col_format)
    cell_text = df_result_formatted.values
    table = plt.table(cellText=cell_text, colLabels=df_result.columns, loc='center', cellLoc='center')
    table[0, 0].get_text().set_color('red')
    table[0, 0].get_text().set_weight('bold')

    for j in range(1, df_result.shape[1]):
        table[0, j].get_text().set_color('red')
        table[0, j].get_text().set_weight('bold')

    for i in range(1, df_result.shape[0]):
        for j in range(df_result.shape[1]):
            table[i, j].get_text().set_color('black')
            table[i, j].get_text().set_weight('normal')
    table.auto_set_column_width(col=list(range(df_result.shape[1])))
    plt.axis('off')
    plt.savefig(f".\\Wykresy\\Bledy- szescienny.png", dpi=700, bbox_inches='tight')


def do_table_quad():
    nodes = roots_maker()
    result = calculate_error_quad()
    error_dict = {"Liczba węzłów": nodes,
                  "Natural - maksymalny": result[0],
                  "Natural - średniokwadratowy": result[1],
                  "Clamped - maksymalny": result[2],
                  "Clamped - średniokwadratowy": result[3]}

    # tworzy data frame z modulu pandas
    df_result = pd.DataFrame(error_dict)
    # formatuje kolumny
    first_col_format = lambda x: f"{int(x):d}"
    float_col_format = lambda x: f"{x:.2e}" if x > 1000 else f"{x:.2f}"
    df_result_formatted = df_result.copy()
    df_result_formatted.iloc[:, 0] = df_result_formatted.iloc[:, 0].apply(first_col_format)
    df_result_formatted.iloc[:, 1:] = df_result_formatted.iloc[:, 1:].applymap(float_col_format)
    cell_text = df_result_formatted.values
    table = plt.table(cellText=cell_text, colLabels=df_result.columns, loc='center', cellLoc='center')
    table[0, 0].get_text().set_color('red')
    table[0, 0].get_text().set_weight('bold')

    for j in range(1, df_result.shape[1]):
        table[0, j].get_text().set_color('red')
        table[0, j].get_text().set_weight('bold')

    for i in range(1, df_result.shape[0]):
        for j in range(df_result.shape[1]):
            table[i, j].get_text().set_color('black')
            table[i, j].get_text().set_weight('normal')
    table.auto_set_column_width(col=list(range(df_result.shape[1])))
    plt.axis('off')
    plt.savefig(f".\\Wykresy\\Bledy-podwojna.png", dpi=700, bbox_inches='tight')
