import errno
import os
import numpy as np
from matplotlib import pyplot as plt
from TableMaker import *

def plot_function(fun):
    X = np.arange(-0.2, 2 + 0.01, 0.01)
    plt.title(f"Wykres funkcji")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.gca().set_facecolor('white')
    plt.plot(X, function(X), label="Funkcja", color="orange")
    plt.legend()
    plt.savefig(f".\\Wykresy\\Wykres Funkcji.png")
    plt.close()


# tworzenie folderu, jeśli nie istnieje
def create_folder_if_not_exists(folder_path):
    try:
        os.makedirs(folder_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
