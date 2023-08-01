import numpy as np

# rozkład równoodległy
def even_distribution(n):
    return np.linspace(-4, 4, num=n)


# rozkład Czebyszewa
def chebyshev_zeros(n):
    roots = []
    for i in range(1, n + 1):
        tryg = np.cos((2 * i - 1) / (2 * n) * np.pi)
        curr_result = 0.5 * (-4 + 4) + 0.5 * (-4 - 4) * tryg
        roots.append(curr_result)
    return np.array(roots)
