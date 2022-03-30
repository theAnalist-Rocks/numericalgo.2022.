import sys

sys.path.append("/home/junior/PycharmProjects/resolutionNumerique/Euler")
import Euler.euler as e
import matplotlib.pyplot as plt


def isContinue(f, t, y):
    try:
        x = f(t, y)
    except:
        return False
    return True


def RK(f, y_0, a, b, **kwargs):
    def k1(t, y):
        return f(t, y)

    def k2(t, y):
        return f(t + .5 * h, y + .5 * h * k1(t, y))

    def k3(t, y):
        return f(t + .5 * h, y + .5 * k2(t, y))

    def k4(t, y):
        return f(t + h, y + h * k3(t, y))

    # on définit le pas
    h = e.h
    x, yPre = [], []
    y = y_0
    if kwargs['precision']:
        h = e.step(kwargs['precision'])


    # on vérifie l'ordre dans les paramètres
    if kwargs["order"] == 2:
        for t in e.nextStep(a, b):
            x.append(t)
            yPre.append(y)
            if isContinue(f, t, y):
                print(y, h, f(t, y), t)
                y = y + h * f(t + .5 * h, y + .5 * k1(t, y))

            else:
                print("La fonction n'est pas continue sur ce intervalle")
                exit(0)

    elif kwargs["order"] == 4:
        for t in e.nextStep(a, b):
            x.append(t)
            yPre.append(y)
            if isContinue(f, t, y):
                y = y + .6 * h * (k1(t, y) + 2 * k2(t, y) + 3 * k3(t, y) + k4(t, y))
            else:
                print("La fonction n'est pas continue sur cet intervalle")
                exit(0)

    plt.plot(x, yPre, color="green")
    plt.title(f"Méthode de Runge-Kutta ordre {kwargs['order']}")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.show()
