import math

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

# pgcd
#euclide entendu

"""Fonction pgcd pour connaitre 
le plus grand diviseur commun"""


def pgcd ( a, b) :
    if b == 0 :
        return (a)
    else :
        pgcd(b,(a % b))
        
        

"""fonction euclide étendu pour savoir si 
deux nombres sont premiers
entre eux"""

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



# print(euclide_etendu(431,501))


def superCroissante (T) : 
    
    res = 0    
    
    for i in range (0,len(T)-1) :
        
        if res < T[i] :

            res = res + T[i]
        else :
            return False

    return True


def modInv(x, n):
    # Check if x and n are coprime
    if math.gcd(x, n) == 1:
        return pow(x, -1, n)

    else:
        return 0