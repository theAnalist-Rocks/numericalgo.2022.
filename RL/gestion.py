#! /usr/bin/env python3
from numpy import array
from methodGauss import Gauss
from solution import MatrixSuperior
import os
from methodeGaussJordan import GaussJordan


def check_input(value, ofType):
    valid = True

    while valid:
        try:
            value = ofType(value)
            valid = False
        except:
            print("\033[91m Entrez une valeur NUMÉRIQUE svp \033[0m")
            value = input("Data :")
    return value


def set_objectif():
    print("------ Vecteur Solution -------")
    dim_b = check_input(input("Nombre d'éléments ?:"), int)
    b = []

    for i in range(dim_b):
        b.append(check_input(input("Data (%d):" % (i + 1)), float))

    return array(b, dtype=float)


def set_matrix(b):
    print("------- Matrice ---------")
    # n = check_input(input("Nombre de lignes ? (Même Nombre de colonnes ET même): "), int)
    n = b.size
    A = []

    for i in range(n):
        temp_array = []
        for j in range(n):
            data = check_input(input("Donnée(%d): " % (j + 1)), float)
            temp_array.append(data)
        A.append(temp_array)
    A = array(A)
    return A


def FirstPivotISNull(A: array, b: array):
    if (A[0] == 0).any():
        n, m = A.shape
        done = 0
        for i in range(1, n):
            if A[i, 0] != 0:
                temp = A[0].copy()
                temp_b = b[0].copy()
                A[0] = A[i]
                A[i] = temp

                b[0] = b[i]
                b[i] = temp_b
                done = 1
                break
        if not done:
            print('\033[91;1;5mLes pivots possibles pour débuter la triangulation sont tous nuls\033[0m')
        else:
            print("\033[96;1mGénération d'une nouvelle matrice ... Patientez SVP\033[0m")
    return A
        

def Answer(A, b):
    if A.size // b.size != b.size:
        print("Utilisez une matrice carrée svp")
        exit(0)
    A = FirstPivotISNull(A, b)
    print('Matrice: ', A, 'Objectif B: ', b, sep='\n')
    A_, b_ = Gauss(A, b)
    print("SOLUTION :", MatrixSuperior(A_, b_))


def main_gauss(A, b):

    os.system("clear")
    Answer(A, b)


def startMatrices():
    b = set_objectif()
    A = set_matrix(b)
    return A, b
    
    
