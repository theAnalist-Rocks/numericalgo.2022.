def changer_signe(f, a, b):
    temp = b
    signe = f(temp)
    while temp != a:
        print(f(temp), temp)
        # il y at-il un changement de signe ?
        if signe * f(temp) <= 0:
            return True
        if temp < 0:
            temp += abs(a + b) / 32
        else:
            temp -= abs(a + b) / 32

    return False


def next_temp(temp, speed, signe_depart):
    if signe_depart < 0:
        temp += speed
    else:
        temp -= speed
    return temp


def change_signe(f, a, b, where: str):
    temp = b
    # print("Checking for solutions in given range")
    print(where)
    while temp != a:
        # print(f(b), f(temp), temp, a)
        try:
            if f(temp) * f(b) <= 0:
                return True
        except :
            print("Une exception avec la fonction entrée a été trouvée")
        finally:
            temp = next_temp(temp, (abs(a) + abs(b))/4, b)

    return False
