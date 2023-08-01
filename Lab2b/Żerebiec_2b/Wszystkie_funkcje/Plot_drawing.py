from Wszystkie_funkcje.Distributions import even_distribution, chebyshev_zeros
from Wszystkie_funkcje.Function import *
import errno
import os
import numpy as np
from matplotlib import pyplot as plt
from Wszystkie_funkcje.Hermite import hermite_interpolation


def plot_function(fun):
    plt.title(f"Wykres funkcji")
    X = np.arange(-4, 4 + 0.01, 0.01)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.gca().set_facecolor('white')
    plt.plot(X, fun(X), label="Funkcja", color="orange")
    plt.savefig(f".\\Wykresy\\Wykres Funkcji.png")
    plt.close()

# tworzenie folderu, jeśli nie istnieje
def create_folder_if_not_exists(folder_path):
    try:
        os.makedirs(folder_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def plot_drawing_for_Hermite(n):
    # Czebyszew
    chebyt_x = chebyshev_zeros(n)
    chebyt_y = fun(chebyt_x)
    plt.scatter(chebyt_x, chebyt_y, label="Węzły", color="green")
    X = np.arange(-4, 4 + 0.01, 0.01)
    plt.plot(X, fun(X), label="Funkcja", color="orange")
    # obliczanie pochodnej
    deriv_x = derivative_fun(chebyt_x)
    # tworzenie listy punktów (x, x')
    p_and_deriv = list(zip(chebyt_x, deriv_x))
    function_name = "Hermite z rozkładem Czebyszewa"
    plt.plot(X, hermite_interpolation(p_and_deriv, X), label=function_name, color="blue")
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

    # równoodległe
    even_x = even_distribution(n)
    even_y = fun(even_x)
    plt.scatter(even_x, even_y, label="Węzły", color="green")
    X = np.arange(-4, 4 + 0.01, 0.01)
    plt.plot(X, fun(X), label="Funkcja", color="orange")
    # obliczanie pochodnej
    deriv_x = derivative_fun(even_x)
    # tworzenie listy punktów (x, x')
    p_and_deriv = list(zip(even_x, deriv_x))
    function_name = "Hermite z rozkładem równoodległym"
    plt.plot(X, hermite_interpolation(p_and_deriv, X), label=function_name, color="blue")
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