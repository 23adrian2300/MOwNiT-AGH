from Wszystkie_funkcje.Distributions import *
from Wszystkie_funkcje.Plot_drawing import *
from Wszystkie_funkcje.Function import *

#interpolacja Lagrange'a
def lagrange_interpolation(X, x_points, y_points):
    result = 0
    for k in range(len(x_points)):
        d = m = 1
        # obliczanie d
        for i in range(len(x_points)):
            if i != k:
                d *= (X - x_points[i])
        # obliczanie m
        for i in range(len(x_points)):
            if i != k:
                m *= (x_points[k] - x_points[i])
        # obliczanie wyniku
        result += y_points[k] * d / m
    return result

# rysowanie wykresów interpolacji Lagrange'a
def lagrange_plot_drawing(n):
    even_x = even_distribution(n)
    chebyshev_x = chebyshev_zeros(n)
    chebyshev_y = fun(chebyshev_x)
    even_y = fun(even_x)
    plot_drawing("Interpolacja Lagrange'a dla rozkładu równoodledłego", even_x, even_y, lagrange_interpolation, n)
    plot_drawing("Interpolacja Lagrange'a dla rozkładu Czebyszewa", chebyshev_x, chebyshev_y, lagrange_interpolation, n)
