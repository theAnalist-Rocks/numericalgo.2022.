#! /usr/bin/env python3
import numpy as np
from numpy import matrix
import numpy as npy


# problème de permutation, si on a pas une matrice triangulaire, on ne peut pas procéder
def permuter_lignes(A, b, index: int, point_pivaut: int, max_line: int):
    for i in range(index, max_line):
        if A[i][point_pivaut] != 0:
            temp = A[index].copy()
            A[index] = A[i]
            A[i] = temp

            # pour b aussi
            temp_b = b[index].copy()
            b[index] = b[i]
            b[i] = temp_b

            return A, b
    return A, b


def matrix_multiply(A, b, i: int, ligne: int, not_null: int, coeff):
    # print(A[ligne], A[i])
    A[i] = A[i] + coeff * A[ligne]
    b[i] = b[i] + coeff * b[ligne]
    return A[i], b[i]


def Gauss(A, b) -> (matrix, np.array):
    temp_A = A
    n = b.size
    cpt = 0
    ligne = 0
    not_null = 0

    while cpt != n:

        for i in range(ligne + 1, n):

            coeff = -A[i][not_null] / A[ligne][not_null]
            if coeff != coeff:
                print(coeff)
                A, b = permuter_lignes(A, b, index=i - 1, max_line=n, point_pivaut=not_null)
                coeff = -A[i][not_null] / A[ligne][not_null]
                if coeff != coeff:
                    print("Un problème avec votre Matrice")
                    print(f"Résultat intermédiaire :\n {A}")
                    exit(0)
                # A[i], b[i] = matrix_multiply(A, i, ligne, not_null, coeff)
            A[i], b[i] = matrix_multiply(A, b, i, ligne, not_null, coeff)

        not_null += 1
        cpt += 1
        ligne += 1
    return A, b

# print(Gauss(np.array([[1, 2, 1], [1, 1, 2], [3, 2, 1]], dtype=float), np.array([1, 2, 1], dtype=float)))
