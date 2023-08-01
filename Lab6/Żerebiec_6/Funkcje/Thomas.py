import numpy as np


def thomas(A, B, float_type):
    n = np.shape(A)[0]

    C = np.zeros(n).astype(float_type)
    C[0] = A[0][0].astype(float_type)

    X = np.zeros(n).astype(float_type)
    X[0] = B[0].astype(float_type)

    for i in range(1, n):
        r = float_type(A[i][i - 1] / C[i - 1])
        C[i] = float_type(A[i][i] - r * A[i - 1][i])
        X[i] = float_type(B[i] - r * X[i - 1])

    X[n - 1] = (X[n - 1] / C[n - 1]).astype(float_type)
    for i in range(n - 2, -1, -1):
        X[i] = ((X[i] - A[i][i + 1] * X[i + 1]) / C[i]).astype(float_type)

    return X