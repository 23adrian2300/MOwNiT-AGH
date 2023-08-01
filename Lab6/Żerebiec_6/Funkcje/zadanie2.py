import numpy as np
import pandas as pd
from Funkcje.Gauss import gauss

max_err = lambda v1, v2: max(abs(v1 - v2))
def zad2(num, float_type):
    sol = []
    for n in num:
        A = np.zeros((n, n)).astype(float_type)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j >= i:
                    A[i - 1][j - 1] = float_type(2 * i / j)
                else:
                    A[i - 1][j - 1] = A[j - 1][i - 1].astype(float_type)
        vec = np.array([1 if i % 2 == 0 else -1 for i in range(n)]).astype(float_type)
        B = A.astype(float_type) @ vec.astype(float_type)
        B.astype(float_type)
        X = gauss(A, B).astype(float_type)
        err = float_type(max_err(vec, X))
        sol += [float_type(err)]
    if float_type == np.float32:
        table = pd.DataFrame(data={"n": num,
                                "float32": sol})
    else:
        table = pd.DataFrame(data={"n": num,
                                "float64": sol})

    return table

