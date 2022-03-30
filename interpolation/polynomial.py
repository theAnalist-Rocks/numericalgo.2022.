from __future__ import annotations

import numpy as np
from typing import Callable, NewType, Iterable, Union
import time
import math


class Polynomial:
    # Lagrange = NewType('Lagrange', Callable[[float, Union[Iterable, np.array], Union[Iterable, np.array]], float])
    # Newton = 0

    def __init__(self, coeff: np.array | list = None, order='min'):
        self.polynom = coeff
        self.degree = len(self) - 1
        self.order = order

    def __str__(self):
        if (self.polynom == 0).all():
            return "0"
        return " + ".join(self.transform(self.polynom))

    @staticmethod
    def transform(data:list|np.array):
        n = len(data)
        d = data[::-1]
        form = []
        for i in range(n):
            if d[i] == 1:
                if i == 1:
                    form.append(f"X")
                elif i == 0:
                    form.append("1")
                else:
                    form.append(f"X^{i}")
            elif d[i] == 0:
                continue
            else:
                if i == 1:
                    form.append(f"{d[i]}X")
                elif i == 0:
                    form.append(f"{d[i]}")
                else:
                    form.append(f'{d[i]}X^{i}')
        return form

    def predict(self, **kwargs):
        data = []
        for i in kwargs['x']:
            data.append(self.func(i))
        return data

    def func(self, x: float):
        data = 0
        for i, j in enumerate(self.polynom[::-1]):
            data += j * (x ** i)
        return data

    @staticmethod
    def isNotZero(value: float):
        return " + " if value != 0 else ''

    @staticmethod
    def define_data(value: float, i: int):
        if value == 0:
            return str()
        elif value:
            if i == 0:
                return str(value)
            elif i == 1:
                return "[" + str(value) + "]" + "X"
            else:
                return "[" + str(value) + "]" + f"X^{i}"

    # Il faut prendre en compte aussi le cas où le dernier est nul ... donc on aura plus de +

    @staticmethod
    def multiMul(array: list[Polynomial] | np.array):
        q = Polynomial([0, 1])
        for i in array:
            q *= i
        return q

    def __len__(self):
        return len(self.polynom)

    def __mul__(self, other):
        if self.order == 'max':
            self.polynom = self.polynom[::-1]

        degree = len(self) + len(other) - 1
        coeff = np.zeros(degree)
        for i, x in enumerate(self.polynom):
            for j, val in enumerate(other.polynom):
                coeff[i + j] += x * val
        return Polynomial(coeff=coeff)

    def generate_lagrange(self, x_data, y_data):

        # on donne l'index du x qu'on souhaite calculer
        def phi(x_index, x_data):
            q = Polynomial([0, 1])
            d = 1
            for i, k in enumerate(x_data):
                if x_index != i:
                    q *= Polynomial([1, -k])
                    d *= (x_data[x_index] - x_data[i])
            Q = Polynomial([0, 1 / d])
            return Q * q

        def lagrange(x_data, y_data):
            p = Polynomial([0, 0])
            for i in range(len(x_data)):
                p += phi(i, x_data) * Polynomial([0, y_data[i]])
            return p
        return lagrange(x_data, y_data)

    def generate_newton(self, x_data, y_data):
        def N(x_data, index):
            # print('Index:', index)
            if index == 0:
                return Polynomial([0, 1])
            else:
                Z = Polynomial([0, 1])
                for ind in range(index):
                    # print(f'{i}-th time')
                    # print(q, [1, -x_data[i]])
                    Z *= Polynomial([1, -x_data[ind]])
                return Z

        def diffdiv(x, y):
            n = np.size(x)
            if n != np.size(y):
                exit("Erreur de taille")
            coeff = y.copy()
            for i in range(n):
                for j in range(n - 1, i, -1):
                    coeff[j] = (coeff[j] - coeff[j - 1]) / (x[j] - x[j - i - 1])
            return coeff

        coeff = diffdiv(x_data, y_data)[::-1]
        q = []
        n = len(coeff)
        for i in range(len(coeff)):
            q.append(Polynomial([0, coeff[i]]) * N(x_data, n - i - 1))
        q = self.multiadd(q)
        print("\033[96;1mPolynôme Généré:\033[0m", q)

    def __add__(self, other: Polynomial):
        def add(longer_polynom, shorter_polynom, greatest_length, shortest_length):
            temp = np.zeros(greatest_length)
            short = np.array(temp)
            short[(greatest_length - shortest_length):] = np.array(shorter_polynom)
            mshort = len(short)
            for i in range(greatest_length):
                for j in range(mshort):
                    if i == j:
                        temp[i] = longer_polynom[i] + short[i]
                        break
                    elif i != j:
                        temp[i] = longer_polynom[i]
            return temp

        n = len(self)
        m = len(other)
        if n >= m:
            return Polynomial(add(self.polynom, other.polynom, n, m))
        else:
            return Polynomial(add(other.polynom, self.polynom, m, n))

    @staticmethod
    def multiadd(array: list[Polynomial]):
        q = Polynomial([0, 0])
        for i in array:
            q += i
        return q

"""
print(Polynomial.generate_lagrange(Polynomial, [-1., -2., 2., 0., 1.], [2, 5, 5, 1, 2]))
Polynomial.generate_newton(Polynomial, [-1., -2., 2., 0., 1.], [2, 5, 5, 1, 2])
P = Polynomial(   [1, 1, 0])
Q = Polynomial([2, 0, 0, 1])
E = Polynomial(   [0, 1, 1])
R = Polynomial(         [1])
print(Polynomial.multiadd([P, Q, E, R]))
"""
