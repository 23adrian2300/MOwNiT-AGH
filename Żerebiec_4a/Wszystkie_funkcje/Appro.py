import numpy as np

from Wszystkie_funkcje.Function import fun
from Wszystkie_funkcje.Plot_drawing import plot_drawing

# funkcja pomocnicza do obliczania współczynników - eliminacja Gaussa
def calculate_A(G, B):
    n = len(G)
    G_copy = [row[:] for row in G]
    B_copy = B[:]
    # eliminacja Gaussa
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(G_copy[j][i]) > abs(G_copy[max_row][i]):
                max_row = j

        G_copy[i], G_copy[max_row] = G_copy[max_row], G_copy[i]
        B_copy[i], B_copy[max_row] = B_copy[max_row], B_copy[i]

        for j in range(i + 1, n):
            factor = G_copy[j][i] / G_copy[i][i]
            for k in range(i, n):
                G_copy[j][k] -= factor * G_copy[i][k]
            B_copy[j] -= factor * B_copy[i]

    A = [0] * n
    for i in range(n - 1, -1, -1):
        s = sum(G_copy[i][j] * A[j] for j in range(i, n))
        A[i] = (B_copy[i] - s) / G_copy[i][i]
    return A

""" 
W kodzie m nie jest liczbą funkcji bazowych, tylko stopniem wielomianu.
Wynika to z faktu łatwiejszego tworzenia poźniej wykresów i tabel.
"""

def approximation(X, Y, m):
    n = len(X)
    W = [1 for _ in range(n)]
    G = np.zeros((m + 1, m + 1))
    B = np.zeros(m + 1)

    for j in range(m + 1):
        for k in range(m + 1):
            G[j, k] = sum(W[i] * X[i] ** (j + k) for i in range(n))
        B[j] = sum(W[i] * Y[i] * X[i] ** j for i in range(n))

    A = calculate_A(G, B)

    return lambda x: sum(A[i] * x ** i for i in range(m + 1))


def ls_approximation(n, m):
    X = np.linspace(-4, 4, n)
    Y = fun(X)
    ls_appr_res = approximation(X, Y, m)
    plot_drawing(X, Y, n, m, ls_appr_res)
