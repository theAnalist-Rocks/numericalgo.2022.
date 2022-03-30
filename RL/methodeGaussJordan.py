#! /usr/bin/env python3
import numpy as np
from methodGauss import Gauss


def get_ones(A, b):
    # s'assurer que c'est une matrice np
    index = 0
    A_ = A.copy()
    b_ = b.copy()

    for i in range(len(A[0])):
        A_[i] = A[i] / A[i][index]
        b_[i] = b[i] / A[i][index]
        index += 1
    return A_, b_


def get_jordan_solution(A, b):
    n = b.size
    cpt = n - 2
    temp_cpt = cpt
    for i in range(n - 1, -1, -1):

        while cpt >= 0:
            # print(f'Before\nb: {b}\nA: {A}')
            b[cpt] = b[cpt] - A[cpt][i] * b[i]
            A[cpt] = A[cpt] - A[cpt][i] * A[i]
            # print(f"After\nb: {b}\nA: {A}")

            cpt -= 1
        cpt = temp_cpt - 1
        temp_cpt = cpt
    return A, b


def GaussJordan(A, b):
    A, b = Gauss(A, b)

    A, b = get_ones(A, b)
    # print('Matrix A:', '\n', A, '\n', 'Matrix b:', '\n', b)
    # s'il y a une erreur, on ne laisse pas la suite s'exécuter
    A, b = get_jordan_solution(A, b)

    # matrice augmentée
    print('MATRICE AUGMENTÉE:')
    for i in range(b.size):
        print(f'{A[i]} | {b[i]}')
    print("Solution:", '\n', b)

