import OutilsMath as OM

import Alphabet

def Code(message):
    return message[::-1]

# print((Code("Hello, World!")))  # Output: "!dlroW ,olleH"

#------------------------------------------------------------------------------------

def Cesar(message, b):
    result = ""
    for char in message:
        if char in Alphabet.alphabet:
            result += Alphabet.alphabet[(ord(char) + b) % Alphabet.alpha_size]
    
    return result


# print(Cesar("Hello, World!", 3))  # Output: "Khoor,

#------------------------------------------------------------------------------------

def Vigenere(message, key, dechiffre=0):
    result = ""
    key_index = 0  # Indice de position dans la clé

    for char in message:
        if char in Alphabet.alphabet:  # Chiffré les charactères qui appartient à l'alphabet
            char_index = Alphabet.alphabet.index(char)  # Indice du caractère du message dans l'alphabet
            key_char = key[key_index % len(key)]  # Répeté la clé autant que nécessaire
            key_char_index = Alphabet.alphabet.index(key_char)  # Indice du caractère de la clé dans l'alphabet

            # Encryption ou decryption
            if dechiffre == 0:  # Encryption
                new_index = (char_index + key_char_index) % Alphabet.alpha_size
            else:  # Decryption
                new_index = (char_index - key_char_index) % Alphabet.alpha_size

            # Ajoute le caractère au résultat
            result += Alphabet.alphabet[new_index]
            key_index += 1  # Avancé l'iterateur sur la clé
            
        else: # Sinon gardé les inchangé
            result += char

    return result

# print(Vigenere("ilfaitfroidcematin", "azur"))

#------------------------------------------------------------------------------------

def CesarAffine(message, a, b) :
    result = ""
    for char in message:
        if char in Alphabet.alphabet:
            result += Alphabet.alphabet[(a*(Alphabet.alphabet.index(char)) + b) % Alphabet.alpha_size]
    
    return result

#------------------------------------------------------------------------------------

def decrypteCesarAffine(message, a, b):
    result = ""
    
    # trouvé les inverse de a et b 
    inverse_a = OM.modInv(a, Alphabet.alpha_size)
    inverse_b = (b * inverse_a) % Alphabet.alpha_size
    
    for char in message:
        if char in Alphabet.alphabet:
            index = Alphabet.alphabet.index(char)
            result += Alphabet.alphabet[(inverse_a * (index - b)) % Alphabet.alpha_size]
            
    return result

    
    