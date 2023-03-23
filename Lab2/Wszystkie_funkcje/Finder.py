import numpy as np

from Wszystkie_funkcje.Distributions import even_distribution, chebyshev_zeros
from Wszystkie_funkcje.Errors import max_error, sum_square_error
from Wszystkie_funkcje.Function import fun


def find_errors(function):
    roots = [i for i in range(2, 101)]
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

    index = 0
    maks = float("inf")
    for i in range(len(roots)):
        # sprawdza czy błąd jest mniejszy od maksymalnego
        if even_sum_square_error[i] < maks:
            maks = even_sum_square_error[i]
            index = roots[i]
    print("Najmniejszy błąd średniokwadratowy dla rozkładu równomiernego to", maks, " dla", index, " węzłów\n")

    index = 0
    maks = float("inf")
    for i in range(len(roots)):
        if chebyshev_sum_square_error[i] < maks:
            maks = chebyshev_sum_square_error[i]
            index = roots[i]
    print("Najmniejszy błąd średniokwadratowy dla rozkładu Czebyszewa to", maks, " dla", index, " węzłów\n")

    index = 0
    maks = float("inf")
    for i in range(len(roots)):
        if even_max_error[i] < maks:
            maks = even_max_error[i]
            index = roots[i]
    print("Najmniejszy błąd maksymalny dla rozkładu równoodległego to", maks, " dla", index, " węzłów\n")

    index = 0
    maks = float("inf")
    for i in range(len(roots)):
        if chebyshev_max_error[i] < maks:
            maks = chebyshev_max_error[i]
            index = roots[i]
    print("Najmniejszy błąd maksymalny dla rozkładu Czebyszewa to", maks, " dla", index, " węzłów\n")