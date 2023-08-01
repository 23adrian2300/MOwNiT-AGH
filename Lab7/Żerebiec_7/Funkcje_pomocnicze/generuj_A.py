import numpy as np


def generate_A(n, k, m):
    return np.array([[k if i == j else m / (n - i - j + 0.5) for j in range(n)] for i in range(n)])