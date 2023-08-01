import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from Wszystkie_funkcje.Function import *
from Wszystkie_funkcje.Distributions import even_distribution, chebyshev_zeros

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
    roots = [i for i in  range(3,30)]
    roots1 = [30,40,50]
    roots = roots + roots1
    roots = sorted(roots)
    return roots

def calculate_error(function):
    roots = roots_maker()
    # Tworzenie list na bledy
    even_max_error = []
    chebyshev_max_error = []
    even_sum_square_error = []
    chebyshev_sum_square_error = []

    # Tworzenie wektora X
    X = np.linspace(-4, 4.01, 801)
    # obliczanie wartosci funkcji w wektorze X
    function_value = fun(X)

    # Petla obliczajaca bledy
    for root in roots:
        #
        # even_x = even_distribution(root)
        # even_det = derivative_fun(even_x)
        # chebyshev_x = chebyshev_zeros(root)
        # chebyshev_det = chebyshev_det(chebyshev_x)

        even_x = even_distribution(root)
        even_deriv_x = derivative_fun(even_x)
        even_p_and_deriv = list(zip(even_x, even_deriv_x))
        even_interpolation = function(even_p_and_deriv, X)

        # chebyt
        chebyt_x = chebyshev_zeros(root)
        chebyt_deriv_x = derivative_fun(chebyt_x)
        chebyt_p_and_deriv = list(zip(chebyt_x, chebyt_deriv_x))
        chebyshev_interpolation = function(chebyt_p_and_deriv, X)

        #
        # # even_interpolation = function(X, even_x)
        # chebyshev_interpolation = function(X, chebyshev_x)
        #
        # # Oblicza maksymalne bledy
        max_even_error_value = max_error(even_interpolation, function_value)
        max_chebyszev_error_value = max_error(chebyshev_interpolation, function_value)

        # Oblicza sume bledow w kwadracie
        square_even_error_value = sum_square_error(even_interpolation, function_value)
        square_chebyshev_error_value = sum_square_error(chebyshev_interpolation, function_value)

        # Dodaje bledy do list
        even_max_error.append(round(max_even_error_value, 4))
        chebyshev_max_error.append(round(max_chebyszev_error_value, 4))
        even_sum_square_error.append(round(square_even_error_value, 4))
        chebyshev_sum_square_error.append(round(square_chebyshev_error_value, 4))
    return roots, even_max_error, chebyshev_max_error, even_sum_square_error, chebyshev_sum_square_error


def do_table(function):
    roots, even_max_error, chebyshev_max_error, even_sum_square_error, chebyshev_sum_square_error = calculate_error(function)
    # Tworzy słownik z błędami
    error_dict = {"Liczba węzłów": roots,
                  "Maksymalny rów.": even_max_error,
                  "Maksymalny Czeb.": chebyshev_max_error,
                  "Średniokwad. rów.": even_sum_square_error,
                  "Średniokwad. Czeb": chebyshev_sum_square_error}

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
    plt.savefig(f".\\Wykresy\\Tabela błędów dla Hemite'a.jpg", dpi=1000, bbox_inches='tight')


