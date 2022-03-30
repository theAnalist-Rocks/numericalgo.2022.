#! /usr/bin/env python3
import numpy as np
import sys

sys.path.append("/home/junior/PycharmProjects/resolutionNumerique/RL/factorization")
import factorizationcrout
from factorizationcrout import *


def crout(A, b):

    if A[0][0] == 0:
        print("Le premier coefficient de la matrice A est nul")
        exit(0)

    L, U = set_start_LU(A)
    print(f"Matrice L:\n{L} \nMatrice R:\n{U}")
    y = MatrixInferior(L, b)
    x = MatrixSuperior(U, y[0])
    print(f"Solution: \n{x}")
    # return x


# print(crout(np.array([[0, 2, 1], [1, 1, 2], [3, 2, 1]], dtype=float), np.array([1, 2, 1], dtype=float)))
#  print(crout(np.array([[1, 2, 3], [3, 2, 1], [2, 1, 3]], dtype=float), np.array([1, 2, 3])))
# set_start_LU(np.array([[1, 2, 3], [3, 2, 1], [5, 2, 3]], dtype=float))
