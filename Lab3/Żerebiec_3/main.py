import shutil
from Wszystkie_funkcje.Errors import *
from Wszystkie_funkcje.Plot_drawing import *
from Wszystkie_funkcje.Spline import *
from Wszystkie_funkcje.Spline import *

if __name__ == '__main__':
    # ścieżka do folderu "Wykresy"
    folder_path = ".\\Wykresy"

    # usuwanie plików z folderu
    shutil.rmtree(folder_path, ignore_errors=True)

    # tworzenie folderu
    os.makedirs(folder_path)
    print("Witaj w programie interpolacji wielomianowej funkcjami sklejanymi")
    print("Badana funkcja to: f(x) = x**2 - cos(pi*x/0.3)\n")
    plot_function(fun)
    print("Podaj liczbe wezlow dla ktorej chcesz uzyskac wykresy:")
    n = int(input("Twoja liczba: "))
    if n < 4:
        print("Liczba wezlow musi byc wieksza od 4")
        exit(1)
    print("Trwa rysowanie wykresów ...")
    i = 4
    while i <= n:
        plotgenerator(i)
        i += 1
    print("Wykresy zostaly zapisane do folderu ./Wykresy\n")
    print("Obliczanie bledow dla funkcji sklejanych")
    print("Tabela błędów zawiera błędy dla węzłów z przedziału od 4 do 100")
    do_table_cubic()
    do_table_quad()
    print("Błędy zostały zapisane do folderu ./Wykresy\n")
    print("Dziekuje za skorzystanie z programu")
    print("Autorzy: Adrian Żerebiec\n")
    print("Koniec programu")
    exit(1)

