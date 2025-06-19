# Exercice 1 

import RSA 
import OutilsMath as om
import SacDos as sd

# Code RSA 
N = 391 # Module 
E = 151 # Compliqueur
D = 7   # Faciliteur

# 1 
C = 17
print("Message Déchiffré ", RSA.DechiffreRSA(C, D, N))

# 2 
p, q = sd.trouvePQ(391)

print("p = {} ; q = {}".format(p, q))
print("Rho(N) = {}".format(p * q))

# 3
print(pow(E, -1, N))
