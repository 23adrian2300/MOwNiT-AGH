from Wszystkie_funkcje.Function import *
import errno
import os
import numpy as np
from matplotlib import pyplot as plt


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

def plot_drawing(x, y, n,m,function):
    function_name = "Aproksymacja"
    plt.scatter(x, y, label="węzły", color="purple")
    X = np.arange(-4, 4 + 0.01, 0.01)
    plt.plot(X, fun(X), label="Funkcja", color="orange")
    plt.plot(X, function(X), label="Aproksymacja średniokwadratowa", color="green")
    plt.title(f"Aproksymacja średniokwadratowa dla {n} węzłów i stopnia m={m}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.gca().set_facecolor('white')

    # ścieżka do folderu, w którym mają być zapisane wykresy
    folder_path = ".\\Wykresy\\{}".format(function_name)

    # tworzenie folderu, jeśli nie istnieje
    create_folder_if_not_exists(folder_path)
    plt.savefig(f".\\Wykresy\\{function_name}\\{n}_{function_name}_{m}.png")
    plt.close()
