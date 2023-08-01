import numpy as np
import pandas as pd

from Funkcje.Gauss import gauss

max_err = lambda v1, v2: max(abs(v1 - v2))


def zad1(num, float_type):
    sol = []
    for n in num:
        A = np.array([[float_type(1 / (i + j - 1)) if i != 1 else float_type(1) for j in range(1, n + 1)] for i in range(1, n + 1)]).astype(
            float_type)
        vec = np.array([1 if i % 2 == 0 else -1 for i in range(n)]).astype(float_type)
        B = A @ vec
        B.astype(float_type)
        X = gauss(A, B)
        X.astype(float_type)
        err = float_type(max_err(vec, X))
        sol += [float_type(err)]

    if float_type == np.float32:
        table = pd.DataFrame(data={"n": num,
                                "float32": sol})
    else:
        table = pd.DataFrame(data={"n": num,
                                "float64": sol})

    return table
