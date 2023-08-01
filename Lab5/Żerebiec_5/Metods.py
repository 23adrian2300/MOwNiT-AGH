import numpy as np
import pandas as pd
pd.options.display.float_format = "{:,.12f}".format

def newton(function, der_function, x_0, epsilon, max_no_iterations, condition):
    x_n = x_0
    for n in range(max_no_iterations):
        f = function(x_n)
        df = der_function(x_n)
        if df == 0:
            return None, None
        if condition == "second" and abs(f) < epsilon:
            return x_n, n
        elif condition == "first" and abs(f / df) < epsilon:
            return x_n, n
        x_n -= f / df
    return None, np.inf


def secant(function, x_1, x_2, epsilon, max_no_iterations, condition):
    for n in range(max_no_iterations):
        if function(x_1) == function(x_2):
            return None, None
        x_1, x_2 = x_2, x_2 - (x_2 - x_1) * function(x_2) / (function(x_2) - function(x_1))
        if condition == "second" and abs(function(x_2)) < epsilon:
            return x_2, n
        elif condition == "first" and abs(x_1 - x_2) < epsilon:
            return x_2, n
    return None, np.inf
