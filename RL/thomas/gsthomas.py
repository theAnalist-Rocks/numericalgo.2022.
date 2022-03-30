from __future__ import annotations
from ctypes import Union
from interpolation.transformation import set_inputs

import numpy as np


def solvable(matrix: np.array | list, n: int):
    # on vérifie d'abord que la première ligne contient (n-2) zéro
    ligne = (matrix[0][:2] != 0).all()
    colonne = (np.array([matrix[i][0] for i in range(n)][:2]) != 0).all()
    return ligne and colonne


def Thomas(matrix: np.array | list, b: np.array|list):
    # voir si on peut le résoudre par la méthode de Thomas
    n = len(matrix[0]) - 1
    if solvable(matrix, n):
        pass
    else:
        print("La méthode de Thomas ne peut pas résoudre")


Thomas(np.array([[1, 2, 0],
                 [1, 3, 2],
                 [0, 1, 1]]),
       [1, 1, 1])
