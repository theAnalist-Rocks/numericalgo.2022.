def g(f, x):
    return (f(x + f(x)) / f(x)) - 1 # ou même si on met 1 ça passe


def Steffenson(f, x, prec, nmax=100):
    cpt = 0

    while True and cpt != 100:
        temp = x
        gx = g(f, x)
        x = x - f(x) / gx
        cpt += 1

        if gx == 0 or (abs(x) - abs(temp))/abs(x) <= prec or 0 <= abs(f(x)) <= prec or cpt == nmax:
            return x



