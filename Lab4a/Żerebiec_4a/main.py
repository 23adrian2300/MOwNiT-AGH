import os
import shutil
from Wszystkie_funkcje.Appro import ls_approximation
from Wszystkie_funkcje.Errors import do_table
from Wszystkie_funkcje.Function import fun
from Wszystkie_funkcje.Plot_drawing import plot_function

if __name__ == '__main__':
    # ścieżka do folderu "Wykresy"
    folder_path = ".\\Wykresy"

    # usuwanie plików z folderu
    shutil.rmtree(folder_path, ignore_errors=True)

    # tworzenie folderu
    os.makedirs(folder_path)
    print("Witaj w programie interpolacji wielomianowej")
    print("Badana funkcja to: f(x) = x**2 - cos(pi*x/0.3)\n")
    plot_function(fun)
    print("Trwa rysowanie wykresów ...")
    m = [2, 3, 4, 6, 7, 8, 10, 15, 20, 25]
    rr = [4, 6, 10, 15, 20, 30, 25, 26,40]
    for i in rr:
        for w in m:
            ls_approximation(i, w)
    print("Wykresy zostaly zapisane do folderu ./Wykresy\n")
    print("Obliczanie bledow dla aproksymacji ...")
    print("Tabela błędów zawiera błędy dla węzłów z przedziału od 4 do 40")
    do_table()
    print("Błędy zostały zapisane do folderu ./Wykresy\n")
    print("Dziekuje za skorzystanie z programu")
    print("Autorzy: Adrian Żerebiec\n")
    print("Koniec programu")
    exit(1)
