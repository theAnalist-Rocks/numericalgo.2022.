#! /usr/bin/env python3
from gestion import main_gauss, startMatrices
from methodeGaussJordan import GaussJordan
from cholesky.cholesky import Choleski
from decompositionDeCrout.crout import crout
from jacobi.jacobi2 import Jacobi
from jacobi.factorization import get_inputs_jacobi
from gaussiedel.gaussxsiedel import GauSSiedel
import sys
# sys.stdin = open("/home/junior/PycharmProjects/resolutionNumerique/RL/jacobi/entry.txt", 'r')
sys.path.append("/home/junior/PycharmProjects/resolutionNumerique/utils")
from utils.stack import Stack

A, b = startMatrices()
A_, b_ = A.copy(), b.copy()
S = Stack()
S.ppush(main_gauss, A, b)
S.ppush(GaussJordan, A, b)
S.ppush(Choleski, A_, b_)
S.ppush(crout, A_, b_)
X, epsilon = get_inputs_jacobi()
S.ppush(Jacobi, A_, b_, X, epsilon)
S.ppush(GauSSiedel, A_, b_, X, epsilon)
S.exec()
