import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from Wszystkie_funkcje.Function import fun
from Wszystkie_funkcje.Lagrange import lagrange_interpolation
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
    roots = [2, 3, 4, 5, 6, 7, 8, 9, 18, 19]
    roots1 = [i for i in range(10, 101, 5)]
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
        even_x = even_distribution(root)
        even_y = fun(even_x)
        chebyshev_x = chebyshev_zeros(root)
        chebyshev_y = fun(chebyshev_x)

        even_interpolation = function(X, even_x, even_y)
        chebyshev_interpolation = function(X, chebyshev_x, chebyshev_y)

        # Oblicza maksymalne bledy
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
    df_result.style.set_properties(**{
        'background-color': 'grey',
        'font-size': '50pt', })
    # zapisz tabelę do pliku JPG
    plt.table(cellText=df_result.values, colLabels=df_result.columns, loc='center', fontsize=20)
    plt.axis('off')
    if function == lagrange_interpolation:
        plt.savefig(f".\\Wykresy\\Tabela błędów dla Lagrange'a.jpg", dpi=1000, bbox_inches='tight')
    else:
        plt.savefig(f".\\Wykresy\\Tabela błędów dla Newton'a.jpg", dpi=1000, bbox_inches='tight')
