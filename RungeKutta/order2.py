import sys
sys.path.append("/home/junior/PycharmProjects/resolutionNumerique/Euler")
import Euler.euler as e
import matplotlib.pyplot as plt


def RK2(f, y_0: float, a, b, **kwargs):

    def k1(t: float, y: float):
        return f(t, y)

    def k2(t, y):
        return f(t + h, y + h * k1(t, y))

    h = e.step(kwargs["precision"])
    x, yPre = [], []
    y = y_0

    for t in e.nextStep(a, b):
        x.append(t)     # On récupère les x
        yPre.append(y)      # on s'assure d'avoir la première valeur
        y = y + h * (k1(t, y) * 0.5 + k2(t, y) * 0.5)       # formule de Runge-Kutta ordre 2

    plt.plot(x, yPre, color="green")




