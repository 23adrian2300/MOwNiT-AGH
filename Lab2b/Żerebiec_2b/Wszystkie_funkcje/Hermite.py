from math import factorial
from Wszystkie_funkcje.Function import *
from Wszystkie_funkcje.Distributions import *
from Wszystkie_funkcje.Plot_drawing import *


def hermite_interpolation(points, x):
    def p(i):
        idx = 0
        j = 0
        if i == 0:
            return 1
        result = 1
        while j < i:
            for k in range(len(points[idx])):
                if i <= j:
                    break
                result *= (x - points[idx][0])
                j += 1
            idx += 1
        return result

    # punkty
    n = sum([len(point) for point in points])

    p_list = []
    for i in range(n):
        p_list.append(p(i))

    b_matrix = [[-1 for _ in range(n)] for _ in range(n)]
    # budowanie listy punktow z indeksami
    pts_and_idx = []
    for idx, row in enumerate(points):
        for k in range(len(row)):
            pts_and_idx.append((row[0], idx))

    # budowanie wierszy z pierwsza kolumna, ktora jest tylko funkcja
    row = 0
    for i in range(len(points)):
        for k in range(len(points[i])):
            b_matrix[row][0] = fun(points[i][0])
            row += 1

    # budowanie wierszy z pochodnymi
    for i in range(1, n):
        for j in range(1, i + 1):
            first_idx = pts_and_idx[i][1]
            second_idx = pts_and_idx[i - j][1]
            if points[first_idx] == points[second_idx] and j < len(points[first_idx]):
                b_matrix[i][j] = points[first_idx][j] / factorial(j)
            else:
                first_val = pts_and_idx[i][0]
                second_val = pts_and_idx[i - j][0]
                b_matrix[i][j] = (b_matrix[i][j - 1] - b_matrix[i - 1][j - 1]) / (first_val - second_val)
    # obliczanie wartosci interpolowanej
    sol = 0
    for i in range(n):
        sol += b_matrix[i][i] * p_list[i]
    return sol
