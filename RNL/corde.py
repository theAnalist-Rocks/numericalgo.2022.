def corde(f, a, b, prec, nmax=100):
    temp = a
    xn = b
    c = b
    cpt = 0

    while cpt < nmax and xn <= b:

        c = xn - (f(xn)*(xn - temp)/(f(xn) - f(temp)))
        if abs(c - xn) <= prec:
            return c
        else:
            temp, xn = xn, c
        cpt += 1
    print(f"Après {nmax} itérations, on n\'a pas de solution")

