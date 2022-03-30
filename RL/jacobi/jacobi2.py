import numpy as np
import sys
sys.path.append("/home/junior/PycharmProjects/resolutionNumerique/RL/factorization")
import factorizationjacobi
from factorizationjacobi import *
from factorizationgs import generate


def Jacobi(A, B, X, epsilon, __iteration__=100):
    E, F, D = EFDGenerate(A)
    cpt = 0
    temp = X.copy()

    while cpt != __iteration__ and (epsilon >= get_error(temp, X)).all():
        if (B == check_solution(A, X)).all():
            print(f"La solution est: \033[92;1m{X}\033[0m ")
            break

        X = generate(func='jacobi', D=D, E=E, F=F, X=X, B=B)
        cpt += 1

    if cpt == __iteration__:
        print(
            f"Pas de convergence en {__iteration__}. Réessayer en augmentant le nombre d'itérations.\nSolution finale:"
            f"\n{X}\nEtat de convergence: \033[96;1m{convergence(A)}\033[0m")

# Jacobi(np.array([[1, 2, 1], [3, 1, 2], [2, 3, 1]], dtype=float), np.array([1, 2, 1], dtype=float), np.array([15,
# 10, -20]))
# Jacobi(np.array([[1, -1 / 2, 1 / 2], [1 / 2, 1, 0], [-1 / 2, -1 / 2, 1]], dtype=float), np.array([5 / 2, -1 / 2, 2],
# dtype=float),
#       np.array([0, 0, -0]), [0.1, .1, .1])
