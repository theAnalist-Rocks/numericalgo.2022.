#! /usr/bin/python3

import numpy as np


def MatrixSuperior(A, b):
    n = m = b.size
    A, b = A[::-1], b[::-1]
    ans_index = n-1
    answers = np.array([0]*n, dtype=float)

    answers = answers.reshape((1, n))
    b = b.reshape((1, n))

    cpt = 0

    while cpt != n:

        sum_left = A[cpt][: ans_index]
        sum_right = A[cpt][ans_index + 1: m: 1] * answers[0][ans_index+1:m].T # ils auront la mêmme taille donc c'est bon
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
    answers = np.array([0]*n, dtype=float)
    answers = answers.reshape((1, n))
    b = b.reshape((1, n))
    cpt = 0
    answer_index = 0
    temp = [0]
    temep_array = [0]

    # vérifier que ce n'est pas nul
    while cpt != n:

        sum_left = A[cpt][:answer_index] * answers[0][:answer_index].T
        sum_right = A[cpt][answer_index+1: m: 1]

        if A[cpt][answer_index] != 0:
            x = (b[0][cpt] - (sum_left.sum() + sum_right.sum())) / A[cpt][answer_index]

            print(A[cpt][:answer_index].shape, answers[0][:answer_index].shape, temp)
            answers[0, answer_index] = x
            cpt += 1
            answer_index += 1
        else:
            print("There is an issue with the matrix: [ZeroDivisionError Encountered]")
            exit(0)
    return answers


# A = np.array([[3, 2, 1], [0, 1, 2], [0, 0, 1]], dtype=float)
# b = np.array([1, 2, 1], dtype=float)

# print(MatrixSuperior(np.array([[1, 2, 1], [0, -1, 1], [0, 0, -6]]), np.array([1, 1, -6], dtype=float)))
