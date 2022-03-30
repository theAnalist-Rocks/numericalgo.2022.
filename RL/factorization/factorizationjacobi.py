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


def k1(D, E):
    return np.dot(D, E)


def generate_new(X, B, E, F, D):
    return np.dot(k1(D, (E + F)), X) + np.dot(D, B)


def generate_new_solution(D, E, F, X, B):
    x = np.dot(np.dot(D, E), X) + np.dot(np.dot(D, F), X) + np.dot(D, B)
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
                temp += abs(A[i, j])
        if abs(A[i, i]) < temp:
            return False
    return True


def get_error(temp, X):
    temp = np.array(temp)
    X = np.array(X)
    return temp - X


def get_inputs_jacobi():
    print("Initiation du vecteur X_0: ")
    n = int(input("Nombre d'éléments: "))
    X = []

    for i in range(n):
        X.append(float(input(f"Entrer la valeur x[{i+1}]: ")))

    print("Entrer l'erreur (sous forme de matrice) : ")
    epsi = []

    for i in range(n):
        epsi.append(float(input(f"Entrer la valeur à la position i[{i+1}] :")))

    return X, epsi

