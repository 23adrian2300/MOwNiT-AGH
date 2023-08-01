from time import perf_counter

import numpy as np
import pandas as pd

from Funkcje_pomocnicze.generuj_A import generate_A


def jacobi(A, b, condition, epsilon):
    D = np.diag(A)
    R = A - np.diagflat(D)
    X = np.full_like(b,10**20)
    iters = 0
    for _ in range(3000):
        X_new = (b - (R @ X)) / D
        iters += 1
        if condition == 1 and np.linalg.norm(X_new - X) < epsilon:
            break
        elif condition == 2 and np.linalg.norm(A @ X - b) < epsilon:
            break
        X = X_new
    return X, iters

def zadanie1_10E20(sizes, epsilon, k, m):
    solution = []
    for n in sizes:
        A = generate_A(n,k,m)
        X_vec = np.array([1 if i % 2 == 0 else -1 for i in range(n)])
        b = A @ X_vec
        start = perf_counter()
        X, iters_1 = jacobi(A, b, 1, epsilon)
        end = perf_counter()
        time_1 = end - start
        norm_1 = np.linalg.norm(X_vec - X)
        start = perf_counter()
        X, iters_2 = jacobi(A, b, 2, epsilon)
        end = perf_counter()
        time_2 = end - start
        norm_2 = np.linalg.norm(X_vec - X)
        solution += [iters_1, iters_2, time_1, time_2, norm_1, norm_2]
    data = pd.DataFrame(data={"n": sizes,
                            "(1) iteracje": solution[::6],
                            "(2) iteracje": solution[1::6],
                            "(1) czas": solution[2::6],
                            "(2) czas": solution[3::6],
                            "(1) norma": solution[4::6],
                            "(2) norma": solution[5::6]})
    return data
