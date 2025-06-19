import fonctionsCryptage as crypto

# Test de la fonction codage inverse 
print((crypto.Code("Hello, World!")))  # Sortie: "!dlroW ,olleH"

# Test de la fonction de codage cesar
print(crypto.Cesar("Hello, World!", 3))  # Output: "Khoor,

# Test de la fonction codage inverse 
print("\nVignere :")
vigenere = crypto.Vigenere("il fait froid ce matin", "azur")
print(vigenere)
# Decryptage 
print(crypto.Vigenere(vigenere, "azur", dechiffre=1))

# Test de la fonction cesar affine
print("\nCesar")

cesar = (crypto.CesarAffine("Hello", 3, 5))
print(cesar)
print(crypto.decrypteCesarAffine(cesar, 3, 5))