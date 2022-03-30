#! /usr/bin/env python3
import numpy as np
from RL.factorization import EFDGenerate


def get_new_x_jacobi(A, b, E, F, D, X):
    new = []
    cpt = 0
    n = len(X)

    while cpt != n:
        temp = b[cpt]
        q = 0
        for i in range(n):
            if i != cpt:
                temp -= A[cpt, i] * X[i]
            if i == cpt and A[cpt, i] != 0:
                q = i
            elif i == cpt and A[cpt, i] == 0:
                print(f"Résolution impossible A[{cpt}, {cpt}] = 0")
                exit(0)
        new.append(temp/A[cpt, q])

        cpt += 1
    print(new)
    new = np.array(new, dtype=float)
    return new


def check_answers(A: np.array, b: np.array, answers: np.array):
    return A.dot(answers) == b


def compare(A, b, answers, eps):
    return sum(A.dot(answers) - b)/b.sum() <= eps


def Jacobi(A: np.array, b: np.array, init: list or np.array):
    answers = init # np.array(init, dtype=float)
    temp = answers
    E, F, D = EFDGenerate(A)

    while (not (check_answers(A, b, answers)).all()) or compare(A, b, answers, 5):
        answers = get_new_x_jacobi(A, b, E, F, D, answers)

    return answers


# ans = Jacobi(np.array([[1, 2, 1], [1, 3, 1], [2, 1, 3]], dtype=float), np.array([1, 2, 1], dtype=float),
# np.array([0, 0, 0])) ans = Jacobi(np.array([[1, 2, 1], [1, 1, 1], [0, 1, 2]], dtype=float), np.array([1, 2, 1],
# dtype=float), np.array([0, 0, 0])) print(check_answers(np.array([[1, 2, 1], [1, 1, 1], [0, 1, 2]], dtype=float),
# np.array([1, 2, 1]), np.array([2, -1, 1]))) print(ans)
