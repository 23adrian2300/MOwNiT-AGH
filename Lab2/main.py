from Wszystkie_funkcje.Errors import *
from Wszystkie_funkcje.Lagrange import *
from Wszystkie_funkcje.Newton import *
import shutil
from Wszystkie_funkcje.Plot_drawing import *
from Wszystkie_funkcje.Finder import *
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
        lagrange_plot_drawing(i)
        newton_plot_drawing(i)
    print("Wykresy zostaly zapisane do folderu ./Wykresy\n")
    print("Obliczanie bledow dla wariantu Netwon'a i Lagrange'a")
    print("Błędy są zawsze dla węzłów od 2 do 100")
    do_table(lagrange_interpolation)
    do_table(newton_interpolation)
    print("Błędy zostały zapisane do folderu ./Wykresy\n")
    print("Czy chcesz zobaczyc najmniejsze bledy?")
    print("Jesli tak, to wybierz 1")
    print("Jesli nie, to wybierz 0")
    choice = int(input("Twoj wybor: "))
    while (choice != 1 and choice != 0):
        print("Niepoprawny wybor")
        print("Wybierz 1 lub 0")
        choice = int(input("Twoj wybor: "))
    if choice == 1:
        print("Trwa szukanie najlepszej funkcji przyblizajacej dla interpolacji Lagrange'a")
        find_errors(lagrange_interpolation)
        print("Trwa szukanie najlepszej funkcji przyblizajacej dla interpolacji Netwon'a")
        find_errors(newton_interpolation)
        print("Dziekuje za skorzystanie z programu")
        print("Autor: Adrian Żerebiec\n")
        print("Koniec programu")
    elif choice == 0:
        print("Dziekuje za skorzystanie z programu")
        print("Autorzy: Adrian Żerebiec\n")
        print("Koniec programu")
        exit(1)

