#! /usr/bin/env python3
from gestion import get_function, get_intervals, get_solutions, get_newton_solutions
from balayage import search_intervals
from dicothomie2 import dicothomie
from newton import newton
from corde import corde
from pointsfixes import pointsfixes
from steffenson import Steffenson

func, a, b, x, prec = get_function()

__INT__ = get_intervals(search_intervals, func, a, b, prec)

print("\033[92;1mDICHOTOMIE \033[0m")
get_solutions(dicothomie, func, __INT__, prec)

print("\033[92;1mCORDE \033[0m")
get_solutions(corde, func, __INT__, prec)

print("\033[92;1mNEWTON \033[0m")
get_newton_solutions(newton, func, x, prec, __INT__)

print("\033[92;1mPOINTS FIXE \033[0m")
get_newton_solutions(Steffenson, func, x, prec, __INT__)
