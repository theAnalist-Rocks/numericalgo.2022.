
def pointsfixes(f, g, a, b, prec):
    xn = f((a + b)/2)

    while True:
        if g(xn) == 0 or 0 <= g(xn) <= 5:
            return xn, g(xn)
        else:
            x, xn = xn, f(xn)
            
# print(pointsfixes(lambda x: 6 / (x + 1), lambda x: x**2 + x - 6, , 0.001))
