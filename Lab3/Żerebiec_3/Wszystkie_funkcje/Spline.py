import numpy as np
from Wszystkie_funkcje.Function import fun
from Wszystkie_funkcje.Plot_drawing import *

def cubic_spline(X, Y, spline_type):
    n = len(X)
    sigma = 0
    h_matrix = [[0] * n for _ in range(n)]
    d_matrix = [0] * n

    def h(i):
        return X[i + 1] - X[i]

    def delta(i):
        return (Y[i + 1] - Y[i]) / h(i)

    def delta2(i):
        return (delta(i + 1) - delta(i)) / (X[i + 1] - X[i - 1])

    def delta3(i):
        return (delta2(i + 1) - delta2(i)) / (X[i + 2] - X[i - 1])

    def solve_matrix_vector(matrix, vector):
        n = len(matrix)
        for i in range(n):
            divisor = matrix[i][i]
            for j in range(i, n):
                matrix[i][j] /= divisor
            vector[i] /= divisor
            for j in range(i + 1, n):
                multiplier = matrix[j][i]
                for k in range(i, n):
                    matrix[j][k] -= multiplier * matrix[i][k]
                vector[j] -= multiplier * vector[i]
        x = np.zeros(shape=(n, 1))
        for i in reversed(range(n)):
            x[i] = vector[i]
            for j in range(i + 1, n):
                x[i] -= matrix[i][j] * x[j]
        return x

    def fill_boundaries(h_matrix, d_matrix, spline_type):
        nonlocal sigma

        if spline_type == "cubic":
            h_matrix[0][0] = -h(0)
            h_matrix[0][1] = h(0)
            h_matrix[n - 1][n - 2] = h(n - 2)
            h_matrix[n - 1][n - 1] = -h(n - 2)

            d_matrix[0] = h(0) ** 2 * delta3(0)
            d_matrix[n - 1] = -h(n - 2) ** 2 * delta3(n - 4)
            sigma = solve_matrix_vector(h_matrix, d_matrix)
        elif spline_type == "natural":
            h_matrix = [h_matrix[i][1:-1] for i in range(1, n - 1)]
            d_matrix = d_matrix[1:-1]
            sigma = [0, *solve_matrix_vector(h_matrix, d_matrix), 0]

    for i in range(1, n - 1):
        h_matrix[i][i - 1] = h(i - 1)
        h_matrix[i][i] = 2 * (h(i - 1) + h(i))
        h_matrix[i][i + 1] = h(i)

        d_matrix[i] = delta(i) - delta(i - 1)

    fill_boundaries(h_matrix, d_matrix, spline_type)

    def find_interval(x):
        for i in range(n - 1):
            if x >= X[i] and x < X[i + 1]:
                return i
        return n - 2

    def s(x):
        i = min(find_interval(x), n - 2)
        b = (Y[i + 1] - Y[i]) / h(i) - h(i) * (sigma[i + 1] + 2 * sigma[i])
        c = 3 * sigma[i]
        d = (sigma[i + 1] - sigma[i]) / h(i)
        return Y[i] + b * (x - X[i]) + c * (x - X[i]) ** 2 + d * (x - X[i]) ** 3

    def S(xs):
        return [s(x) for x in xs]

    return S



def quadratic_spline(X, Y, spline_type):
    n = len(X)
    a = None
    b = None

    def gamma(i):
        return (Y[i] - Y[i - 1]) / (X[i] - X[i - 1])

    def a_natural(i):
        return (b_natural(i + 1) - b_natural(i)) / (2 * (X[i + 1] - X[i]))

    def b_natural(i):
        if i == 0:
            return 0
        return 2 * gamma(i) - b_natural(i - 1)

    def a_clamped(i):
        return (b_clamped(i + 1) - b_clamped(i)) / (2 * (X[i + 1] - X[i]))

    def b_clamped(i):
        if i == 0:
            return (Y[1] - Y[0]) / (X[1] - X[0])
        return 2 * gamma(i) - b_clamped(i - 1)

    def solve(spline_type):
        nonlocal a, b
        if spline_type == "clamped":
            a = a_clamped
            b = b_clamped
        elif spline_type == "natural":
            a = a_natural
            b = b_natural

    solve(spline_type)

    def find_interval(x):
        for i in range(n - 1):
            if x >= X[i] and x < X[i + 1]:
                return i
        return n - 2

    def evaluate_quadratic_spline(x):
        i = min(find_interval(x), n - 2)
        a_i = a(i)
        b_i = b(i)
        return a_i * np.power(x - X[i], 2) + b_i * (x - X[i]) + Y[i]

    def evaluate_quadratic_spline_list(xs):
        return [evaluate_quadratic_spline(x) for x in xs]

    return evaluate_quadratic_spline_list



def plotgenerator(n):
    X = np.linspace(-4, 4, n) #rozkład równomierny
    Y = fun(X)
    cubicsplinenatural = cubic_spline(X, Y, "natural")
    cubicsplinecubic = cubic_spline(X, Y, "cubic")
    quadraticsplinenatural = quadratic_spline(X, Y, "natural")
    quadraticsplineclamped = quadratic_spline(X, Y, "clamped")
    plot_drawing("Splajn sześcienny - natural", X, Y, n, cubicsplinenatural)
    plot_drawing("Splajn sześcienny - cubic", X, Y, n, cubicsplinecubic)
    plot_drawing("Splajn kwadratowy - natural", X, Y, n, quadraticsplinenatural)
    plot_drawing("Splajn kwadratowy - clamped", X, Y, n, quadraticsplineclamped)
