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
                temp += A[i, j] ** .5
        if abs(A[i, i]) < temp:
            return False
    return True


def check_inverso(D, E):
    def checkD(D):
        for i in range(D[0].size):
            if D[i, i] == 0:
                return False
        return True
    Q = D + E
    try:
        Q = np.linalg.inv(Q)
        return Q, checkD(D)
    except:
        return None, False

def get_error(temp, X):
    temp = np.array(temp, dtype=float)
    X = np.array(X, dtype=float)
    return abs(temp.sum()) - abs(X.sum()) / (abs(temp.sum()) + 1)


def get_new_solution(D, E, F, X, B):
    X = np.array(X, dtype=float)
    new = np.zeros(X.shape, dtype=float)
    for i in range(X.size):
        temp = 0
        for j in range(X.size):
            if i < j:
                temp += F[i, j] * X[j]
            elif j < i:
                temp += E[i, j] * X[j]
        new[i] = (1 / D[i, i]) * (B[i] - temp)

    return new


def gs_generate(D, E, F, X, B):
    X = np.array(X, dtype=float)
    Q = np.linalg.inv(E + D)
    W = np.dot(F, X)
    return -np.dot(Q, W) + np.dot(Q, B)


def generate(**kwargs):
    if kwargs['func'] in ['jacobi', 'jac', 'jc']:
        return get_new_solution(kwargs["D"], kwargs["E"], kwargs["F"], kwargs["X"], kwargs["B"])
    elif kwargs['func'] in ['gausseidel', "gs"]:
        return gs_generate(kwargs["D"], kwargs["E"], kwargs["F"], kwargs["X"], kwargs["B"])