import numpy as np


def EFDGenerate(A):
    E, F, D = [], [], []

    # matrice inf
    for i in range(len(A[0])):
        temp_e = []
        for j in range(len(A[0])):
            if i > j:
                temp_e.append(A[i, j])
            else:
                temp_e.append(0)
        E.append(temp_e)
    E = np.array(E, dtype=float)

    # matrice sup

    for i in range(len(A[0])):
        temp_f = []
        for j in range(len(A[0])):
            if j > i:
                temp_f.append(A[i, j])
            else:
                temp_f.append(0)
        F.append(temp_f)
    F = np.array(F, dtype=float)

    # matrice diagonale

    for i in range(len(A[0])):
        temp_d = []
        for j in range(len(A[0])):
            if i == j:
                temp_d.append(A[i, j])
            else:
                temp_d.append(0)
        D.append(temp_d)
    D = np.array(D, dtype=float)

    return E, F, D


def generate_new_solution(Q, F, X, B):
    x = np.dot(np.dot(Q, F), X) + np.dot(Q, B)
    # print(x)
    return x


def check_solution(A, X):
    return np.dot(A, X)


def convergence(A):
    n = A[0].size

    for i in range(n):
        temp = 0
        for j in range(n):
            if i != j:
                temp += A[i, j]**.5
        if A[i, i] < temp:
            return False
    return True


def check_inverso(D, E):
    Q = D + E
    for i in range(Q[0].size):
        if Q[i, i] == 0:
            return False
    return Q


def get_error(temp, X):
    return abs(temp.sum()) - abs(X.sum()) / (abs(temp.sum()) + 1)
