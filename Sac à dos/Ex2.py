# Exercice 2

import RSA 
import OutilsMath as om
import SacDos as sd
import math

# Code RSA 
N = 221 # Module 
E = 11 # Compliqueur
D = 35   # Faciliteur

# 1 
# a 
M = 112 
print(RSA.ChiffreRSA(M, E, N))

# b
C = 78
print(RSA.DechiffreRSA(C, D, N))

#2
p = 53
q = 71

#a 
N = p * q
print(N)

phiN = (p - 1) * (q - 1)
print("Phi(N) = {} ".format(phiN))

#b
E = 307 
print("E acceptable si E et N sont premiers entre eux : {}".format("True" if math.gcd(E, N) == 1 else "False"))
D = pow(E, -1, N)
print("D = E^-1 % N = {} ".format(D))

#c
Cle_public = [E, N]
Cle_prive = [D, N]
print("Cle publique : {} | Cle privee : {}".format(Cle_public, Cle_prive))

#d 
# Il faut les gardé caché pour une raison ou une autre !
