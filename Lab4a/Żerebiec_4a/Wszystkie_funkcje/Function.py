import numpy as np

# zadana funkcja
def fun(x):
    k = 0.3
    m = 1
    y = x ** 2 - m * np.cos((np.pi * x) / k)
    return y
