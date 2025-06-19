import OutilsMath
import RSA
import math

BobA = [93,660,1479,3218,6602,13594]
BobB =[2,3,6,13,27,52]
def trouvePQ(N):
    """Trouve P et Q tels que N = P * Q, avec P et Q premiers."""
    for Q in range(2, N):
        if N % Q == 0 and OutilsMath.est_premier(Q):  # Q est un diviseur et premier
            P = N // Q  # Division entière
            if OutilsMath.est_premier(P):  # Vérifie si P est aussi premier
                return P, Q  # Retourne les deux nombres premiers
    
    return None  # Aucun couple trouvé
    
# Fonction pour trouver les diviseurs de N
def diviseurs(N):
    diviseurs = []
    for i in range(1, N):
        if N % i == 0:
            diviseurs.append(i)
            
            return diviseurs
            
def sacDifficile(Sac,E,N): #transforme un sac facile en sac difficile., E est le compliqueur, N le modulo
    
    for i  in range (0, len(Sac)-1) :
        Sac[i] = (Sac[i]*E )% N

    return Sac


def faciliteur(x,N): #permet de transformer un sac difficile en sac facile
    return OutilsMath.euclide_etendu(x,N)[2]
# print(faciliteur(10693,25922))

def glouton(message , Sac): #message est un nombre reçu, sac est une liste de nombre formant un sac
    
    res=[]
    i = len(Sac)-1
    
    while i != -1 :
       
        if (message - Sac[i]) >= 0 :
            message = message-Sac[i]
            res.append(1)
        else :
            res.append(0)
        i=i-1

    if message == 0 :
       
        print(res[::-1])
        print("le message est la seule solution\n")
        return res[::-1]
    else :
        print("aucune solution! \n")
        return []
    
def traitementFacile(message,D, N): #D est le faciliteur, N le nombre que l'on va modulo
        return (message*D%N)

    
# glouton(faciliteur(10693,25922),BobA)
