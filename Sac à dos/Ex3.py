import math

# Code RSA 
N = 1073  # Module 
E = 257   # Compliqueur
D = 353   # Faciliteur

message = [17, 18, 00]

def combin3(message):
    _ = ""
    for i in range(0, 3):
        _ += f"{message[i]:02d}"  # s'assurer qu'on a bien 2 chiffres
    message = int(_)
    return message

def decoupEn2(message):
    """
    Découpe un message en deux parties et les convertit en entiers.
    """
    message = str(message)
    if len(message) % 2 != 0:
        raise ValueError("Le message doit avoir une longueur paire")
    
    millieu = len(message) // 2
    part1 = int(message[:millieu])  # Première moitié
    part2 = int(message[millieu:])  # Deuxième moitié
    
    return part1, part2

def chiffre_paquet(paquet, E, N):
    """
    Chiffre un paquet de 2 entiers en utilisant la fonction RSA.
    """
    chiffre1 = pow(paquet[0], E, N)
    chiffre2 = pow(paquet[1], E, N)
    return chiffre1, chiffre2

def colle2(message):
    _ = ""
    for i in range(0, 2):
        _ += f"{message[i]:02d}" 
        
    message = int(_)
    return message

def decoupEn3(message):
    message = str(message)
    if len(message) % 3 != 0:
        raise ValueError("Le message doit avoir une longueur multiple de 3")
    millieu = len(message) // 3
    part1 = int(message[:millieu])  # Première tier
    part2 = int(message[millieu:2*millieu])  # Deuxième tier
    part3 = int(message[2*millieu:])  # Troisième tier
    return part1, part2, part3

def string_to_numbers(message):
    return [ord(char) for char in message]  # Convertir chaque caractère en son code ASCII

# a
def Chiffre_RSA_avancé(message, E, N):
    message = decoupEn2(combin3(message))
    message = chiffre_paquet(message, E, N)
    message = colle2(message)
    return message

# Exemple d'utilisation
message = string_to_numbers("METHODE")
print(Chiffre_RSA_avancé(message, E, N))
