import numpy as np
from Funkcje.zadanie2 import zad2
from Funkcje.zadanie1 import zad1
from Funkcje.uwarunkowanie import condition
from Funkcje.zadanie3 import zad3

if __name__ == '__main__':
    print("Program rozwiązywania układów równań liniowych metodami bezpośrednimi")
    print("Zapisywanie tabel do folderów...")
    # Zadanie1
    print("Zadanie 1")
    fl32 = zad1([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], np.float32)
    fl32.to_csv("./Zadanie1/1fl32.csv", index=False)
    fl64 = zad1([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], np.float64)
    fl64.to_csv("./Zadanie1/1fl64.csv", index=False)
    print("Zapisano tabele do katalogu Zadanie1")
    # Zadanie 2
    print("Zadanie 2")
    fl32 = zad2(
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 500],
        np.float32)
    fl32.to_csv("./Zadanie2/2fl32.csv", index=False)
    fl64 = zad2(
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 500],
        np.float64)
    fl64.to_csv("./Zadanie2/2fl64.csv", index=False)
    # Uwarunkowanie
    condition_df = condition([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    condition_df.to_csv("./Zadanie2/condition.csv", index=False)
    print("Zapisano tabele do katalogu Zadanie2")
    # Zadanie 3
    print("Zadanie 3")
    fl32 = zad3(
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 300, 500], 9, 2,
        np.float32)
    fl32.to_csv("./Zadanie3/3fl32.csv", index=False)
    fl64 = zad3(
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 300, 500], 9, 2,
        np.float64)
    fl64.to_csv("./Zadanie3/3fl64.csv", index=False)
    print("Zapisano tabele do katalogu Zadanie3")
    print("Zapisywanie tabel zakończone")
    print("Dziękuje za skorzystanie z programu")