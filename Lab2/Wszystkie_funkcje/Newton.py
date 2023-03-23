from Wszystkie_funkcje.Distributions import *
from Wszystkie_funkcje.Plot_drawing import *
from Wszystkie_funkcje.Function import *

def newton_interpolation(X, x_points, y_points):
    differences_table = [[float("inf") for _ in range(len(x_points))] for _ in range(len(x_points))]
    y_interpolated = [float("inf") for _ in range(len(x_points))]
    for i in range(len(x_points)):
        differences_table[i][0] = y_points[i]
    for j in range(1, len(x_points)):
        for i in range(len(x_points) - j):
            differences_table[i][j] = (differences_table[i + 1][j - 1] - differences_table[i][j - 1]) / (x_points[i + j] - x_points[i])

    # Obliczanie wartości interpolowanej
    x_term = 1
    y_interpolated[0] = differences_table[0][0]
    for i in range(1, len(x_points)):
        x_term *= (X - x_points[i - 1])
        y_interpolated[i] = y_interpolated[i - 1] + differences_table[0][i] * x_term
    # zwrot wartości interpolowanej
    return y_interpolated[-1]

# rysowanie wykresów interpolacji Newtona
def newton_plot_drawing(n):
    even_x = even_distribution(n)
    chebyshev_x = chebyshev_zeros(n)
    even_y = fun(even_x)
    chebyshev_y = fun(chebyshev_x)
    plot_drawing("Interpolacja Newtona dla rozkładu równoodledłego", even_x, even_y, newton_interpolation, n)
    plot_drawing("Interpolacja Newtona dla rozkładu Czebyszewa", chebyshev_x, chebyshev_y, newton_interpolation, n)
