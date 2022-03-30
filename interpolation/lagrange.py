from transformation import *

def Lagrange():

    print(30*'-', "INTERPOLATION POLYNOMIALE AVEC LE POLYNOME DE LAGRANGE", 30*'-')
    x_data, y = set_inputs()

    res = []
    pre_ans = []
    maxi = max(x_data)
    mini = min(x_data)
    pre_set = np.linspace(start=mini, stop=maxi, num=250)
    for i in x_data:
        res.append(P(i, x_data, y))
    print("\033[96;1mPolynôme Généré:\033[0m", Polynomial.generate_lagrange(Polynomial, x_data, y))
    # plot(x_data, res)

