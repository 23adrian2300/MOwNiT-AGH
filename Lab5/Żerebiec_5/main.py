import shutil

from TableMaker import *
from plot import *


if __name__ == '__main__':
    print("Witaj w programie do obliczania miejsc zerowych funkcji i  badania ilości iteracji")
    print("Trwa zapisaywanie tabel do zadania 1...")
    folder_path = ".\\Wykresy"
    # usuwanie plików z folderu
    shutil.rmtree(folder_path, ignore_errors=True)
    # tworzenie folderu
    os.makedirs(folder_path)
    plot_function(function)
    plt.clf()
    lambdas = [0.001,0.0001,10**(-10),10**(-5)]
    for i in lambdas:
        calculate("newton", i, 1000, "second")
        plt.clf()
        calculate("newton", i, 1000, "first")
        plt.clf()
    lambdas = [0.001,0.0001,10**(-10),10**(-5)]
    for i in lambdas:
        plt.clf()
        print("secant","second",i)
        calculate("secant", i, 1000, "second")
        plt.clf()
        print("secant", "first", i)
        calculate("secant", i, 1000, "first")
        plt.clf()
    print("Tabele z zadania 1 zostały zapisane")
    print("Trwa zapisaywanie tabel do zadania 2...")
    print("Tabele z zadania 2 zostały zapisane")
    print("Dziękuje za skorzystanie")
