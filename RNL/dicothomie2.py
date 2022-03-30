
# prends en paramètre la fonction, un intervalle subdivisé où on suppose qu'i y a une solution, la précision
# On sait qu'il y a un changement de signe

def dicothomie(f, a, b, precision):
    m = (a + b) / 2
    while abs(b - a) > precision:
        m = (a + b) / 2

        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m

    return m
