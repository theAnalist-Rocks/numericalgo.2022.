import numpy as np


def compare(A, x):
    return np.dot(A, x[0])


def set_start_l_LU(A):
    arr = []
    arr2 = []

    # pour LU
    for i in A:
        temp = []
        for j in range(len(i)):
            if j == 0:
                temp.append(i[j])
            else:
                temp.append(0)
        arr.append(temp)

    for i in range(len(A[0])):
        temp = []
        for j in range(len(A[i])):
            if i == j:
                temp.append(1)
            elif i == 0 and j != 0:
                temp.append(A[i][j] / arr[0][0])
            else:
                temp.append(0)
        arr2.append(temp)

    return np.array(arr, dtype=float), np.array(arr2, dtype=float)


def set_start_LU(A):
    L, U = set_start_l_LU(A)
    maxi = A[0].size

    # on cherche à compléter les informations qu'on n'a pas encore
    for i in range(1, maxi):
        for j in range(1, maxi):
            sumy = 0
            for k in range(j):
                sumy += L[i, k] * U[k, j]
                # print(f'Sum: {L[i, k]} {U[k, j]} {i, k, j} L: {L[i]}')

            if i >= j:
                L[i, j] = A[i, j] - sumy
                # print(L[i, j], A[i, j], sumy, i, j)

            elif j > i:
                temp = 0
                for k in range(i):
                    temp += L[i, k] * U[k, j]
                    # print(f'U sum: {L[i, k]} {U[k, j]}{i, k, j}')
                U[i, j] = (A[i, j] - temp) / L[i, i]

    return L, U


def MatrixSuperior(A, b):
    n = m = b.size
    A, b = A[::-1], b[::-1]
    ans_index = n - 1
    answers = np.array([0] * n, dtype=float)

    answers = answers.reshape((1, n))
    b = b.reshape((1, n))

    cpt = 0

    while cpt != n:

        sum_left = A[cpt][: ans_index]  # juste pour vérifier qu'on a bien des 0
        sum_right = A[cpt][ans_index + 1: m: 1] * answers[0][
                                                  ans_index + 1:m].T  # ils auront la même taille donc c'est bon
        if A[cpt][ans_index] != 0:
            x = (b[0][cpt] - (sum_left.sum() + sum_right.sum())) / A[cpt][ans_index]
            # print(sum_left, A[cpt][ans_index + 1:m :1], A[cpt, ans_index], answers[0][ans_index + 1:m], b[0, cpt],
            # sum_right) print(x, answers)
            answers[0, ans_index] = x
            # print(answers[0][:cpt], A[cpt][:ans_index], A[cpt][ans_index + 1: m: 1])
            # print(x, answers)

            cpt += 1
            ans_index -= 1
        else:
            print("There is an issue with the matrix: [ZeroDivisionError Encountered]")
            exit(0)
    return answers


def MatrixInferior(A, b):
    n = m = b.size
    answers = np.array([0] * n, dtype=float)
    answers = answers.reshape((1, n))
    b = b.reshape((1, n))
    cpt = 0
    answer_index = 0


    while cpt != n:

        sum_left = A[cpt][:answer_index] * answers[0][:answer_index].T
        sum_right = A[cpt][answer_index + 1: m: 1]  # juste pour vérifier qu'on a bien des 0

        if A[cpt][answer_index] != 0:
            x = (b[0][cpt] - (sum_left.sum() + sum_right.sum())) / A[cpt][answer_index]

            # print(A[cpt][:answer_index].shape, answers[0][:answer_index].shape, temp)
            answers[0, answer_index] = x
            cpt += 1
            answer_index += 1
        else:
            print("There is an issue with the matrix: [ZeroDivisionError Encountered]")
            exit(0)
    return answers

# t = MatrixSuperior(np.array([[1, 2, 1], [0, -1, 1], [0, 0, -6]], dtype=float), np.array([1, 1, -6]))
# print(t)
# print(MatrixInferior(np.array([[1, 0, 0], [2, 1, 0], [3, 0, 1]], dtype=float), np.array([1, 1, -3])))
# L, R = set_start_LU(np.array([[1, -1, 1, -1], [2, -1, 3, 1], [1, 1, 2, 4], [5, 1, 1, 1]], dtype=float))
# print(L, "\n", R)
# print('Produit:\n', np.dot(L, R))
