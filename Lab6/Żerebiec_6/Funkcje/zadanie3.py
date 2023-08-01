from time import perf_counter

import numpy as np
import pandas as pd

from Funkcje.Gauss import gauss
from Funkcje.Thomas import thomas

max_err = lambda v1, v2: max(abs(v1 - v2))


def zad3(numbers, k, m, float_type):
    sol = []
    for n in numbers:
        A = np.zeros((n, n))
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    A[i - 1][j - 1] = float_type(k)
                elif j == i + 1:
                    A[i - 1][j - 1] = float_type(1 / (i + m))
                elif i > j == i - 1:
                    A[i - 1][j - 1] = float_type(k / (i + m + 1))

        vec = np.array([1 if i % 2 == 0 else -1 for i in range(n)]).astype(float_type)
        B = A.astype(float_type) @ vec.astype(float_type)

        gauss_time_start = perf_counter()
        xg = gauss(A, B).astype(float_type)
        gauss_time_stop = perf_counter()

        gtime = gauss_time_stop - gauss_time_start
        gauss_err = max_err(vec, xg).astype(float_type)

        thomas_time_start = perf_counter()
        xt = thomas(A, B, float_type).astype(float_type)
        thomas_time_end = perf_counter()

        ttime = thomas_time_end - thomas_time_start
        thomas_err = max_err(vec, xt).astype(float_type)

        sol += [gauss_err, thomas_err, gtime, ttime]

    table = pd.DataFrame(data={"n": numbers,
                            "błąd dla Gaussa": sol[::4],
                            "błąd dla Thomasa": sol[1::4],
                            "czas dla Gaussa[s]": sol[2::4],
                            "czas dla Thomasa[s]": sol[3::4]})

    return table
