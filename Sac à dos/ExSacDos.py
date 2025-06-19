import SacDos
import OutilsMath
import math

#Exo 1
print("\n Exo 1\n")
print("Le message facilité est : \n")
x = SacDos.traitementFacile(41577,SacDos.faciliteur(10693,25922) , 25922)
print("D*message reçu = ")
print(x)

print("le message décrypter est :")
SacDos.glouton(20949,SacDos.BobA)

#Exo 2
print("\n Exo 2 \n")
print("Bobb est-elle supercroissante?")
print(OutilsMath.superCroissante(SacDos.BobB))
print("pgcd de N et E :")
print(math.gcd(105,31))

print("le sac à dos difficile de BobB est")
print(SacDos.sacDifficile(SacDos.BobB,31,105))
print("le faciliteur D est ")
D =SacDos.faciliteur(31,105)
print(D)
print("le message 011000 110101 101110 devient : 93+81; 62+93+88+52; 62+81+88+102 = [69,85,18]\n")

print(SacDos.traitementFacile(69 ,D,105))
print(SacDos.traitementFacile(85,D,105))
print(SacDos.traitementFacile(18,D,105))


SacDos.BobB =[2,3,6,13,27,52]
SacDos.glouton(9,SacDos.BobB)
SacDos.glouton(40,SacDos.BobB)
SacDos.glouton(48,SacDos.BobB)

#h)
print("\n h) \n")
#262257139 ---> mod 478 (cumule des nombres de bobB) devient 262 257 139
print(SacDos.traitementFacile(262,D,105))
A=SacDos.glouton(22,SacDos.BobB)
print(SacDos.traitementFacile(257,D,105))
B=SacDos.glouton(32,SacDos.BobB)
print(SacDos.traitementFacile(139,D,105))
C=SacDos.glouton(79,SacDos.BobB)
print(A,B,C)
print("\n")


print("g) \n")
#g 232680541----> mod 478 (cumule des nombres de bobB) devient 23 268 05 41  or ne marchera pas car 41 laisse un reste après 
#etre passé par le sac BobB par l'algo glouton.
print(SacDos.traitementFacile(23,D,105))
A=SacDos.glouton(38,SacDos.BobB)
print(SacDos.traitementFacile(268,D,105))
B=SacDos.glouton(73,SacDos.BobB)
print(SacDos.traitementFacile(5,D,105))
C=SacDos.glouton(95,SacDos.BobB)
print(SacDos.traitementFacile(41,D,105))
D=SacDos.glouton(86,SacDos.BobB)
print(A,B,C,D)
