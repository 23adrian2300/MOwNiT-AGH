import os
import shutil
from Wszystkie_funkcje.Appro import *
from Wszystkie_funkcje.Errors import do_table, find_best_max
from Wszystkie_funkcje.Function import fun
from Wszystkie_funkcje.Plot_drawing import plot_function


if __name__ == '__main__':
    # ścieżka do folderu "Wykresy"
    folder_path = ".\\Wykresy"

    # usuwanie plików z folderu
    shutil.rmtree(folder_path, ignore_errors=True)

    # tworzenie folderu
    os.makedirs(folder_path)
    print("Witaj w programie aproksymacji trygonometrycznej")
    print("Badana funkcja to: f(x) = x**2 - cos(pi*x/0.3)\n")
    plot_function(fun)
    roots = [10, 15, 20, 30, 40, 50,60,70,80,90,100,200,300]
    print("Trwa rysowanie wykresów ...")
    m = [i for i in range(1, 15)]
    for root in roots:
        for w in m:
            if (root-1)/2>w:
                trig_approximation(root, w)
    trig_approximation(1000, 20)
    trig_approximation(2000,20)
    trig_approximation(1000,3)
    trig_approximation(1000,10)
    trig_approximation(1000,14)
    trig_approximation(5000,20)
    print("Wykresy zostaly zapisane do folderu ./Wykresy\n")
    print("Obliczanie bledow dla funkcji aproksymujacej")
    print("Tabela błędów zawiera błędy dla różnych liczb węzłów")
    do_table(trig_approximation)
    print("Błędy zostały zapisane do folderu ./Wykresy\n")
    print("Dziekuje za skorzystanie z programu")
    print("Autorzy: Adrian Żerebiec\n")
    print("Koniec programu")
    exit(1)
