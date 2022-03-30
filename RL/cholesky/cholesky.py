#! /usr/bin/env python3
import numpy as np
import sys
sys.path.append("/home/junior/PycharmProjects/resolutionNumerique/RL/factorization")
from factorizationcholesky import *


def define_as_pos(A: np.array):
    n = A[0].size
    x = np.random.randint(low=1, high=10, size=n).reshape((n, 1))
    x_t = x.T
    return np.dot(np.dot(x_t, A), x) > 0


def define_L(A: np.array):
    L = []
    n = A[0].size

    for i in range(n):
        temp = []
        for j in range(n):
            if i == j == 0:
                temp.append(A[i, i] ** .5)
            elif j == 0:
                temp.append(A[i, 0] / A[0, 0])
            else:
                temp.append(0)
        L.append(temp)

    return np.array(L, dtype=float)


def get_LL(A: np.array):
    n = A[0].size
    col = 1
    x = col
    L = define_L(A)

    while col != n:

        temp = 0
        for k in range(col):
            temp += L[col, k]**2
        L[col, col] = (A[col, col] - temp)**0.5

        for i in range(col+1, n):
            temp_2 = 0
            for k in range(col):
                temp_2 += L[i, k] * L[col, k]
            L[i, col] = (A[i, col] - temp_2) / L[col, col]
        col += 1

    return L, L.T


def Choleski(A: np.array, b: np.array):
    print(A)
    if (A.T == A).all() and define_as_pos(A).all():
        L, L_ = get_LL(A)
        y = MatrixInferior(L, b)
        x = MatrixSuperior(L_, y[0])
        print(x)
        # return x
    else:
        print("Impossible de résoudre avec Choleski")
        print(f"""
            Définie positive: {define_as_pos(A).all()}
            Symétrique: {(A.T == A).all()}
        """)


