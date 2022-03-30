from scipy.misc import derivative


def newton(f, x, precision):

    f_ = derivative(f, x)
    xn = x - f(x)/f_

    while abs(xn - x) <= precision and f(xn) != 0:
        temp = xn

        try:
            f_ = derivative(f, xn)
            xn = xn - f(xn)/f_
        except Exception as e:
            print(e.args)
        if temp == xn:
            break
    return xn
