import numpy as np

def gauss(A, B, dtype = np.float64):
    n = len(A)
    AB = np.hstack([A, B.reshape((n, 1))]).astype(dtype)

    for i in range(n):
        pivot = AB[i, i]
        for j in range(i + 1, n):
            base = AB[j, i] / pivot
            AB[j] -= base * AB[i]

    X = AB[:, n]
    X[n - 1] /= AB[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        pivot = AB[i, i]
        X[i] -= (AB[i, i + 1:n] * X[i + 1:n]).sum()
        X[i] /= pivot

    return X