from scanf import change_signe


def dichotomie(f, a, b, precision):
    m = (b + a) / 2
    temp_a = a
    temp_b = b
    redo = False

    while not redo:
        redo = True
        # print(m, f(m))
        try:
            while abs(temp_a - temp_b) > precision and f(m) != 0:
                print(" while ", "m:", m, "a:", temp_a, "b:", temp_b,
                      "f(m):", f(m), "f(temp_a):", f(temp_a), "f(temp_b):", f(temp_b))

                if f(temp_a) * f(m) <= 0 and change_signe(f, temp_a, m, "if"):
                    temp_b = m

                # il se passe quoi si les deux cas sont vrais à la fois ?
                # choix du bon intervalle
                elif f(temp_b) * f(m) <= 0 and change_signe(f, m, temp_b, "elif"):
                    temp_a = m

                else:
                    print("Ambiguity: il peut y avoir 0 ou plusieurs solutions, choisir un intervalle plus précis")

                m = (temp_a + temp_b) / 2

        except ZeroDivisionError:
            if a > 0:
                temp_a = a - 1
            else:
                temp_a = a + 1
            # temp_b = b - 1
            m = (temp_a + temp_b) / 2
            redo = False
    return m
