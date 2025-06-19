import random
import math 

import OutilsMath

from sympy import isprime

# EN DEV, TOUTE EST À TESTÉ ENCORE

def generer_premier():
    """Génère un nombre premier de 'bits' bits."""
    while True:
        num = random.randint
        if num % 2 == 0:
            num += 1  # Assurer que le nombre est impair (2 étant le seul nombre premier pair)
        if isprime(num):
            return num

def genere_clefs():
    """Génère une paire de clés RSA."""
    # Génération de deux nombres premiers
    p = generer_premier()
    q = generer_premier()

    # Calcul du module N
    n = p * q

    # Calcul de l'indice d'Euler de N (phi(N))
    phi_n = (p - 1) * (q - 1)

    # Choix d'un exposant public E (E doit être premier avec phi_n)
    e = random.randint(2, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Calcul de l'exposant privé D (D est l'inverse multiplicatif de E modulo phi_n)
    d = OutilsMath.pow_mod(e, -1, phi_n)

    # Retour des clés publiques et privées
    clef_publique = (n, e)
    clef_privée = (n, d)
    
    return (e, d, n)

# def intToBin(n):
#     return bin(n)[2:].zfill(8)

# Crée un chiffrement RSA
def RSA(message):
    p, q
    n = 0
    while (n <= len(message)):
        p, q, n= genere_clefs()
    
    return [(message^p % q), p, q]

# Chiffré avec une clef publique (E, N)
def ChiffreRSA(message, E, N):
    return ((message ^ E) % N)

# Chiffré avec une clef privé (D, N)
def DechiffreRSA(message, d, n):
    return (message^d % n)

