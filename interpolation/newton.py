from transformation import N, plot, set_inputs, takeVarX
import numpy as np
from polynomial import Polynomial


def difference_divise(x_data, y_data, ntimes: int):
    if ntimes == 0:
        return y_data[ntimes]
    else:
        return (y_data[ntimes] - difference_divise(x_data, y_data, ntimes - 1)) / (x_data[ntimes] - x_data[ntimes - 1])


def diffdiv(x_data, y_data):
    # pour éviter une division par zéro au dénominateur, on peut soit faire un set ou alors échapper si on a zéro
    n = np.size(x_data)
    if n != np.size(y_data):
        exit("Erreur de taille pour les deux tableaux")
    coeff = y_data.copy()
    for i in range(n):
        for j in range(n - 1, i, -1):
            coeff[j] = (coeff[j] - coeff[j - 1]) / (x_data[j] - x_data[j - i - 1])
    return coeff


def set_coeff(x_data: np.array or list, y_data: np.array or list):
    alpha = []

    for i in range(x_data.size):
        alpha.append(difference_divise(x_data, y_data, i))

    return alpha


def P(x, y_data, x_data):
    coeff = diffdiv(x_data, y_data)
    # print(coeff)
    ans = []

    for i in range(len(coeff)):
        w = N(x_data, i, x)
        ans.append(w * coeff[i])

    return sum(ans)


def NewtonInterpolate():
    print('---------------------------------------INTERPOLATION DE NEWTON---------------------------------------------')
    ans = []
    pre_ans = []
    x_data, y_data = set_inputs()

    maxi = max(x_data)
    mini = min(x_data)
    pre_set = np.linspace(start=mini, stop=maxi, num=250)

    for x in x_data:
        ans.append(P(x, y_data, x_data))
    for x in pre_set:
        pre_ans.append(P(x, y_data, x_data))
    get_coeff_newton(x_data, y_data)
    Polynomial.generate_newton(Polynomial, x_data, y_data)
    plot(x_data, ans)
