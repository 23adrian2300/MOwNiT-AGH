from copy import deepcopy

import numpy as np

from Wszystkie_funkcje.Function import fun
from Wszystkie_funkcje.Plot_drawing import plot_drawing

class Trig_Apro:
    # m to stopien wielomianu
    def __init__(self, X, Y,m):
        if m > np.floor((len(X) - 1) / 2):
            raise Exception("m musi byc mniejsze od (n-1)/2")
        if len(Y) != len(X):
            raise Exception("X i Y musza miec taka sama dlugosc")

        self.X = X
        self.Y = Y
        self.m = m
        self.start = X[0]
        self.end = X[-1]
        self.A = (0 for _ in range(len(X)))
        self.B = (0 for _ in range(len(X)))
        self.scaleX()
        self.Bk()
        self.Ak()
        self.unscaleX()

    def Bk(self):
        n = len(self.X)
        calculated_B = [0] * n
        for k in range(n):
            bk = 0
            for j in range(n):
                bk += self.Y[j] * np.sin(k * self.X[j])
            calculated_B[k] = 2 * bk / n
        self.B = calculated_B


    def Ak(self):
        n = len(self.X)
        calculated_A = [0] * n
        for k in range(n):
            ak = 0
            for j in range(n):
                ak += self.Y[j] * np.cos(k * self.X[j])
            calculated_A[k] = 2 * ak / n
        self.A = calculated_A

    def scaleX(self):
        lr = 8
        scaled_X = []
        for x in self.X:
            scaled_x = x / lr
            scaled_x *= 2 * np.pi
            scaled_x += -np.pi - (2 * np.pi * self.start / lr)
            scaled_X.append(scaled_x)

        self.X = scaled_X

    def unscaleX(self):
        lr = 8
        unscaled_X = []
        for x in self.X:
            unscaled_x = x - (-np.pi - (2 * np.pi * self.start / lr))
            unscaled_x /= 2 * np.pi
            unscaled_x /= lr
            unscaled_X.append(unscaled_x)
        self.X = unscaled_X

    def pointscaleX(self, x):
        lr = self.end - self.start
        x /= lr
        x *= 2 * np.pi
        x += -np.pi - (2 * np.pi * self.start / lr)
        return x

    def approximation(self, X):
        result = []
        for x in X:
            cp_x = deepcopy(x)
            cp_x = self.pointscaleX(cp_x)
            approx = 1 / 2 * self.A[0] + sum(self.A[j] * np.cos(j * cp_x) + self.B[j] * np.sin(j * cp_x) for j in range(1, self.m))
            result.append(approx)

        return result


def trig_approximation(n, m):
    X = np.linspace(-4, 4, n)
    Y = fun(X)
    trigonometric_approximation = Trig_Apro(X, Y, m)
    plot_drawing(X, Y, len(X), m, trigonometric_approximation.approximation)

