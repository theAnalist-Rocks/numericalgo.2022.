#! /usr/bin/env python3
from gauss.methodGauss import Gauss
from gauss.solution import MatrixSuperior
import numpy as np
import sys

# sys.stdin = open("entry.txt", 'r')


def set_inputs():
    print("\n", 30 * "-", "SAISIE DES INFORMATIONS NECESSAIRES", "-" * 30)
    x = []
    y = []

    p = int(input("Degré du polynôme: "))
    n = int(input("Nombre d'éléments dans le vecteur x: "))

    for i in range(n):
        x.append(float(input(f"Entrer la valeur x{i + 1}: ")))
        y.append(float(input(f"Entrer la valeur y{i + 1}: ")))

    return x, y, p, n


def set_matrix():
    x, y, p, n = set_inputs()
    A = []
    temp_y = []
    cpt = 0

    for i in range(p + 1):
        ligne = []
        for j in range(p + 1):
            temp = 0
            for k in range(n):
                # print(f'{2*p} {i +i} {p} {2*p - p +1}')
                temp += x[k] ** (2 * p - (i + j))
            ligne.append(temp)
        A.append(ligne)
    # pour l'objectif

    for j in range(p, -1, -1):
        temp_sum = 0
        for k in range(n):
            temp_sum += (x[k] ** j) * y[k]
        temp_y.append(temp_sum)

    return np.array(A, dtype=float), np.array(temp_y, dtype=float)


# solution

def leastsquare():
    A, y = set_matrix()
    A_, b_ = Gauss(A, y)
    print("SOLUTION: \n\n")
    x = MatrixSuperior(A_, b_)
    print(x)


leastsquare()
