import numpy as np
import pandas as pd
from Funkcje_pomocnicze.generuj_A import generate_A

def calculate_spectral_radius(A):
    n = len(A)
    B = np.diagflat(np.diag(A))
    I = np.eye(n)
    M = I - np.linalg.inv(B) @ A
    return max(abs(np.linalg.eigvals(M)))

def zadanie2(sizes, k, m):
    result = []
    for n in sizes:
        A = generate_A(n, k, m)
        spectral = calculate_spectral_radius(A)
        condition = True
        if spectral >= 1:
            condition = False
        result += [spectral, condition]
    df = pd.DataFrame(data={"n": sizes,
                            "Wektor spektralny": result[::2],
                            "Czy spełniony warunek?": result[1::2]})
    return df