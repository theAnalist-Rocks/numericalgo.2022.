# marche seulement sur des fonctions continues
from math import *
import os
import numpy as np
import matplotlib.pyplot as plt

h = 10 ** -1


def step(precision: int):
    global h
    h = 10 ** precision
    return h


def getValues():
    f = input("Entrer la fonction f(t; y): ")
    f = eval(f"lambda t, y: {f}")
    y_0 = float(input("entre la valeur de y_0: "))
    a, b = map(float, input("Entrer les bornes [a, b] (sous cette forme): ").split())
    return f, y_0, a, b


def nextStep(a, b):
    for i in np.linspace(a, b, num=int((b - a) // h) + 1):
        yield i


def raffiner():
    global h
    answer = input("Voulez vous raffiner? [y/n]: ")
    if answer not in ["no", "n", "N", "Non", "non"]:
        raffine = int(input("Précision du pas 10 ^ ( entre -5 et 5) :"))
        step(raffine)
        return True
    else:
        return False


def EulerFonction(f, y, a, b):
    plt.title("Equation Différentielle: Méthode de Euler")
    # On prédit les valeurs

    x, yPred = [], []
    for t in nextStep(a, b):
        x.append(t)
        yPred.append(y)     # On prend en compte y_0
        temp = f(t, y)
        y = y + h * temp

    plt.plot(x, yPred, color="red")
    plt.legend(f"Pas:{h}")
    plt.show()
    return x, yPred


def Euler():
    f, y, *arr = getValues()
    while raffiner():
        EulerFonction(f, y, *sorted(arr))
    os.system("clear")


# Euler()
