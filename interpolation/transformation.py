import matplotlib.pyplot as plt
import numpy as np
import math
# from polynomial import Polynomial


def isZero(data):
    return data > 0


def transform(y):
    p = []
    for i in y:
        p.append(y)
    return tuple(p)


def phi(x: float, x_array: np.array, x_index: int):
    num = []
    denum = []
    #  coeff_sent_in = []

    # numérateur
    for i in range(x_array.size):
        if i != x_index:
            num.append(x - x_array[i])
            #  coeff_sent_in.append([1, x_array[i]])
            # dénominateur
            denum.append(x_array[x_index] - x_array[i])
    num = math.prod(num)
    denum = math.prod(denum)

    return num / denum


def P(x, x_data: np.array, coeff: tuple or list or np.array):
    n = len(coeff)
    ans = []
    for i in range(n):
        ans.append(coeff[i] * phi(x, x_data, i))
    return sum(ans)


def plot(X, y):
    plt.scatter(X, y, color='blue')

    x_set = np.linspace(min(X), max(X), num=150)
    y_set = []
    for i, j in enumerate(X):
        plt.annotate(f"({j}, {y[i]})", xy=(j, y[i]))

    for i in x_set:
        y_set.append(P(i, X, y))
    plt.plot(x_set, y_set, color="blue")
    plt.show()


def N(data: list or np.array, n: int, x: float):
    if n == 0:
        return 1
    arr = []
    for i in range(n):
        arr.append((x - data[i]))
    return math.prod(arr)


def set_inputs():
    print("Recueil des valeurs initiales x et y :")
    n = int(input("Taille du dataset : "))
    x, y = [], []
    if isZero(n):
        for i in range(n):
            x.append(float(input(f"Entrer la valeur x{i + 1}: ")))
            y.append(float(input(f"Entrer la valeur y{i + 1}: ")))
        return np.array(x), y
    else:
        print("Pas d'exécution: Fin du programme")
        exit(0)


def takeVarX():
    as_array = input("Entrer plusieurs données à la suite ? [y/n]: ").lower()
    as_array = 1 if as_array in ['y', 'oui', 'yes'] else 0

    if as_array:
        n = int(input("Entrer la taille: "))

        if isZero(n):
            data = []
            for i in range(n):
                data.append(float(input(f"Donnée N°{i + 1}:")))

            return np.array(data, dtype=float)
        else:
            print("Vous avez entré une valeur incorrecte: Fin du programme")
            exit(0)
    else:
        return [float(input("Entrer la donnée: "))]


"""def get_coeff_newton(x_data: np.array, coeff: np.array):
    Polynomial.generate_newton(Polynomial, x_data, coeff)"""
