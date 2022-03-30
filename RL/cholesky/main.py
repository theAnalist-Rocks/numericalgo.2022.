import sys
from gauss.gestion import set_objectif, set_matrix
from cholesky import Choleski


b = set_objectif()
A = set_matrix(b)
Choleski(A, b)

