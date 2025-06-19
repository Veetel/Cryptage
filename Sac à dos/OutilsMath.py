import math
import random 

# inverse modulaire 

def pow_mod(a, b, n):
    """Exponentiation modulaire : calcule (a^b) % n."""
    result = 1
    a = a % n  # Optimisation pour réduire la taille des calculs intermédiaires

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        b = b // 2

    return result

def modInv(x, n):
    # Vérifié si x et n sont premier entre eux 
    if math.gcd(x, n) == 1:
        return pow(x, -1, n)

    else:
        return 0

# pgcd (déjà présente dans la lib math gcd() )
# Fonction pgcd pour connaitre le plus grand diviseur commun

def pgcd ( a, b) :
    if b == 0 :
        return (a)
    else :
        pgcd(b,(a % b))
 
       
#euclide entendu
# fonction euclide étendu pour savoir si deux nombres sont premiers entre eux

def euclide_etendu (a,b):
    
    """initialisation des tableaux de variables
    afin d'avoir un historique"""
    
    r = [a,b]
    u = [1,0]
    v = [0,1]
    q = [0]
    
    i = 1

    q.append(r[0]//r[1])
    
    while r[i] != 0: 
        r.append( r[i-1] % r[i])
        q.append(r[i-1] // r[i])
        i=i+1
   
    q.append(r[len(r)-2])
    
    i=0
    while i != len(r)-1 :
       
        u.append( u[i]- q[i+1]  * u[i+1])
        v.append( v[i] - q[i+1] * v[i+1])
        
        i=i+1
     
    return (r[len(r)-1],u[len(u)-2],v[len(v)-2],q[len(q)-1])

def superCroissante (T) : 
    """Détermine si une suite est supercroissante, T est une suite(ou tableau de nombre)"""
    res = 0    
    
    for i in range (0,len(T)-1) :
        
        if res < T[i] :

            res = res + T[i]
        else :
            return False

    return True

def est_premier(n, k=5):
    """
    Test de primalité probabiliste utilisant l'algorithme de Miller-Rabin.

    Args:
        n (int): Le nombre à tester.
        k (int): Le nombre de tests à effectuer pour plus de certitude.

    Returns:
        bool: True si n est probablement premier, False sinon.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Écrire n - 1 sous la forme 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Effectuer k tests
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d % n
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

# List les premiers n nombre premier en utilisant la méthode Rabin-Miller
def premiers(n):
    """Liste les premiers n nombres premiers en utilisant la méthode Rabin-Miller
    """
    list = [1]
    i = 2
    while len(list) < n:
        if est_premier(i):
            list.append(i)
            i += 1
        else:
            i += 1
    return list


    
