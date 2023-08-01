import numpy as np
import pandas as pd


def norm(A):
    n = len(A)
    return max(sum(A[i][j] for j in range(n)) for i in range(n)).astype(np.float64)


def A1(n):
    return np.array([[1 / (i + j - 1) if i != 1 else 1 for j in range(1, n + 1)] for i in range(1, n + 1)]).astype(np.float64)

def A2(n):
    A = np.zeros((n, n)).astype(np.float64)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j >= i:
                A[i - 1][j - 1] = 2 * i / j
            else:
                A[i - 1][j - 1] = A[j - 1][i - 1].astype(np.float64)
    return A

def calculate(A):
    A_inv = np.linalg.inv(A)
    return norm(A_inv) * norm(A)

def condition(numbers):
    sol = []
    for n in numbers:
        zad1con = calculate(A1(n))
        zad2con = calculate(A2(n))
        sol += [zad1con, zad2con]
    table = pd.DataFrame(data={"n":numbers,
                            "wskaźnik uwarunkowania dla zadania 1":sol[::2],
                            "wskaźnik uwarunkowania dla zadania 2":sol[1::2]})
    return table

