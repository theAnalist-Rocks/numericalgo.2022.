import numpy as np
import sys

sys.path.append("/home/junior/PycharmProjects/resolutionNumerique/RL/factorization")
import factorizationgs
from factorizationgs import *
import os


def GauSSiedel(A: np.array, b: np.array, X: np.array, epsilon, __iteration__=200):
    E, F, D = EFDGenerate(A)
    Q, valid = check_inverso(D, E)
    temp = X.copy()
    cpt = 0

    if valid:
        while cpt != __iteration__ and (epsilon >= get_error(temp, X)).all():
            if (b == check_solution(A, X)).all():
                print(f"Solution trouvée: \033[92;1m{X}\033[0m")
                break
            X = generate(func="gs", D=D, E=E, F=F, X=X, B=b)
            cpt += 1

        if cpt == __iteration__:
            print(f"Pas de convergence en {__iteration__} itérations\nÉtat de convergence: {convergence(A)}")
            print("Solution finale:", "\n", X)
    else:
        print("\033[91;1mLa matrice (D - E) n'est pas inversible\033[0m")
# GauSSiedel(np.array([[1, -1/2, 1/2], [1/2, 1, 0], [-1/2, -1/2, 1]], dtype=float), np.array([5/2, -1/2, 2],
# dtype=float), np.array([0, 0, -0]), 1)
