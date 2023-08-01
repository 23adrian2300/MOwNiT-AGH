from Wszystkie_funkcje.Errors import *
import shutil
from Wszystkie_funkcje.Plot_drawing import *
import os
from Wszystkie_funkcje.Other import *

if __name__ == "__main__":
    # ścieżka do folderu "Wykresy"
    folder_path = ".\\Wykresy"

    # usuwanie plików z folderu
    shutil.rmtree(folder_path, ignore_errors=True)

    # tworzenie folderu
    os.makedirs(folder_path)
    print("Witaj w programie interpolacji wielomianowej")
    print("Badana funkcja to: f(x) = x**2 - cos(pi*x/0.3)\n")
    plot_function(fun)
    print("Podaj liczbe wezlow dla ktorej chcesz uzyskac funkcje:")
    n = int(input("Twoja liczba: "))
    if n < 2:
        print("Liczba wezlow musi byc wieksza od 2")
        exit(1)
    print("Trwa rysowanie wykresów ...")
    for i in range(2, n + 1):
        # rysowanie wykresów
        plot_drawing_for_Hermite(i)
        other_plot_drawing(i)
    print("Wykresy zostaly zapisane do folderu ./Wykresy\n")
    print("Obliczanie bledow dla wariantu Hermite'a")
    print("Tabela błędów zawiera błędy dla węzłów z przedziału od 3 do 50")
    do_table(hermite_interpolation)
    print("Błędy zostały zapisane do folderu ./Wykresy\n")
    print("Dziekuje za skorzystanie z programu")
    print("Autorzy: Adrian Żerebiec\n")
    print("Koniec programu")
    exit(1)

