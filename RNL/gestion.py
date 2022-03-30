# from balayage import next_temp
from math import *


def check_input(value, ofType):
    valid = True

    while valid:
        try:
            value = ofType(value)
            valid = False
        except:
            print("\033[91m Entrez une valeur NUMÉRIQUE svp \033[0m")
            value = input("Data :")
    return value


def get_function():
    print("INFORMATIONS IMPORTANTES:\n",
          "- ln = log2\n"
          "- e = exp\n"
          "- 2² = 2 ** 2\n\n")
    func = input("Entrer la fonction: \nf(x) = ")
    # sous la forme x ** 2 + ...
    try:
        func = eval(f'lambda x:{func}')
        if func:
            # l'intervalle de base
            a = check_input(input("Borne [a]: "), int)
            b = check_input(input("Borne [b]: "), int)
            x = check_input(input("x_0: "), float)
            prec = check_input(input("Precision: "), float)
            __INT__ = [a, b]
            return func, *__INT__, x, prec
    except:
        print("Problème dans la fonction: Une entrée invalide")
        exit(0)


def get_intervals(func, f, a, b, prec):
    intervals, solutions = func(f, a, b, prec)
    if intervals:
        print("On a trouvé des intervalles où la fonction change de signe:", *intervals)
    else:
        print("Il n'y a aucune solution dans l'intervalle donné")
    return intervals


def get_solutions(func, f, intervals, prec, nmax=None):
    answers = []

    if intervals:

        for interval in intervals:
            answers.append(func(f, *interval, prec))
        print("-" * 100 + "Solutions" + "-" * 100)

        if answers:
            for answer in answers:
                try:
                    if f(answer) == 0 or 0 <= abs(f(answer)) <= prec + abs(answer):
                        print(answer, "\t|en arrondissant à 10^-5 près|\t", round(answer, 5))

                except Exception as e:
                    print("An error occured ... Please contact the programmer", f"\nException(s): {e.args}")
        else:
            print("Program ends here because no solution where found in given range")
    else:
        print("Program ends here because no solutions where found in given range")


def get_newton_solutions(func_newton, f, x, prec, intervals):
    answers = []
    xn = x
    test = 0

    # essaie d'abord avec la l'entrée de l'utilisateur pour voir la convergence
    try:
        first_try = func_newton(f, x, prec)
        if f(first_try) == 0 or 0 <= f(first_try) <= 5:
            print(f"Pour xo({x}) newton retourne {first_try}")
            exit(0)
        else:
            print(f"Avec xo({x}) donné, la méthode ne converge pas.")
    except:
        print("An error occurred. \nThis error can be caused by ZeroDivisionError. Please contact the programmer")

    # On essaie les intervalles succeptibles de contenir des solutions
    for interval in intervals:
        xn = sum(interval) / 2
        print(f"Essai avec x={xn}")

        # prendre en compte l'erreur de division par zero
        try:
            answers.append(func_newton(f, xn, prec))
        except:
            print("There have been an Error. Contact The programmer for more details onthis issue")

    # On affiche les résultats trouvés
    if answers:
        print("-" * 100 + "SOLUTIONS POSSIBLES" + 100 * "-")
        for answer in answers:
            if f(answer) == 0 or 0 <= f(answer) <= 5:
                print(answer)
                test = 1
        if not test:
            print("Program ends here because no solutions where found")
    else:
        print("No solution found ... Did you inputted a wrong function ? Wrong interval perhaps ?")

# Docs: on peut changer, pour résoudre le problème des fonctions non monotones les intervalles que la fonction reçoit
