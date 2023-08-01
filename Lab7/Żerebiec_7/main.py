import os
from Funkcje_zadanie1.zadanie1_wektor0 import zadanie1_0
from Funkcje_zadanie1.zadanie1_wektor100 import zadanie1_100
from Funkcje_zadanie1.zadanie1_wektor10E20 import zadanie1_10E20
from Funckje_zadanie2.zadanie2 import zadanie2

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

if __name__ == '__main__':
    print("Program do rozwiązywania układów równań liniowych metodami iteracyjnymi")
    print("Zapisywanie tabel do folderów...")
    print("Zadanie 1")
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 400, 500]
    epsilons = [0.001, 0.00001, 10**(-8), 10**(-10), 10**(-12), 10**(-14), 10**(-16)]

    for eps in epsilons:
        directory = f"results/test1"
        create_directory_if_not_exists(directory)
        df_1 = zadanie1_0(numbers, eps, 7, 0.5)
        df_1.to_csv(os.path.join(directory, f"exercise_1_{eps}.csv"), index=False)

    for eps in epsilons:
        directory = f"results/test100"
        create_directory_if_not_exists(directory)
        df_1 = zadanie1_100(numbers, eps, 7, 0.5)
        df_1.to_csv(os.path.join(directory, f"exercise_1_{eps}.csv"), index=False)

    for eps in epsilons:
        directory = f"results/test10000"
        create_directory_if_not_exists(directory)
        df_1 = zadanie1_10E20(numbers, eps, 7, 0.5)
        df_1.to_csv(os.path.join(directory, f"exercise_1_{eps}.csv"), index=False)

    print("Zadanie 2")
    directory = "results"
    create_directory_if_not_exists(directory)
    df_2 = zadanie2(numbers, 7, 0.5)
    df_2.to_csv(os.path.join(directory, "exercise_2.csv"), index=False)

    print("Zapisywanie tabel zakończone")
    print("Dziękuję za skorzystanie z programu")