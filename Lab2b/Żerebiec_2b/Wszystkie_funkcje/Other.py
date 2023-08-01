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

# rysowanie wykresow
def plot_drawing(function_name, x, y, function, n):
    plt.scatter(x, y, label="Węzły", color="green")
    X = np.arange(-4, 4 + 0.01, 0.01)
    plt.plot(X, fun(X), label="Funkcja", color="orange")
    plt.plot(X, function(X, x, y), label="Interpolacja", color="purple")
    plt.title(f"{function_name} dla {n} węzłów")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.gca().set_facecolor('white')

    # ścieżka do folderu, w którym mają być zapisane wykresy
    folder_path = ".\\Wykresy\\{}".format(function_name)

    # tworzenie folderu, jeśli nie istnieje
    create_folder_if_not_exists(folder_path)
    plt.savefig(f".\\Wykresy\\{function_name}\\{function_name}_{n}.png")
    plt.close()

# rysowanie wykresow dla roznych rozkladow
def other_plot_drawing(n):
    even_x = even_distribution(n)
    chebyshev_x = chebyshev_zeros(n)
    chebyshev_y = fun(chebyshev_x)
    even_y = fun(even_x)
    plot_drawing("Lagrange z rozkładem równoodległym", even_x, even_y, lagrange_interpolation, n)
    plot_drawing("Lagrange z rozkładem Czebyszewa", chebyshev_x, chebyshev_y, lagrange_interpolation, n)
    even_x = even_distribution(n)
    chebyshev_x = chebyshev_zeros(n)
    even_y = fun(even_x)
    chebyshev_y = fun(chebyshev_x)
    plot_drawing("Newton z rozkładem równoodległym", even_x, even_y, newton_interpolation, n)
    plot_drawing("Newton dla rozkładem Czebyszewa", chebyshev_x, chebyshev_y, newton_interpolation, n)