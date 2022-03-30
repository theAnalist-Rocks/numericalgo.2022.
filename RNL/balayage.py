def next_temp(temp, speed, a, b):
    if a <= 0 and b < 0:
        return temp


def isNeg(temp, speed):
    if temp < 0:
        return [temp, temp - speed]
    else:
        return [temp, temp + speed]


def spec(temp, speed):
    return temp + speed


def scanf(f, a, b, speed, signe_depart, prec):
    try:
        signe = f(a)
    except ZeroDivisionError:
        signe = f(a + prec)
        a += prec
    finally:
        temp = a

    signe_change = False

    while not signe_change and temp <= b:
        # debug print(f(temp), signe, temp)
        # tip: il peut y avoir changement de signe sans qu'on ait une solution
        # On enlève les possibles ZeroDivisionError
        # On renvoie les intervalles à la fonction qui prend en compte la recherche de solution
        try:
            if f(temp) * signe <= 0:
                # if temp < 0:
                #    return [temp, temp - speed]
                return [temp, temp + speed]
        except Exception as e:
            print(e.args)
        finally:
            temp = spec(temp, speed)


def search_intervals(f, a, b, prec):
    # global new_a
    intervals = []
    temp = a
    count = 0
    b += .1

    while temp <= b:
        # regarder quand il y a un changement de signe
        print("Trows in a:", a, " and b:", temp)
        try:
            new_a, temp = scanf(f, temp, b, 0.000001, a, prec)
            # debug print(new_a, temp)
            intervals.append([new_a, temp])
        except Exception as e:
            print(*e.args, "Limit Reached")
            break
        count += 1

    return intervals, count
