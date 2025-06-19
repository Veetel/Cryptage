🔐 Projet de Simulation – Cryptographie & Sac à dos

Ce dépôt regroupe deux projets pédagogiques autour de la **cryptographie RSA**, des **algorithmes de chiffrement classiques** et du **problème du sac à dos**, réalisés dans le cadre des TPs de simulation et sécurité à l'ISIMA.

---

## 📁 Structure des projets

### 🗂️ 1. Chiffrement RSA et Sac à Dos

Ce projet explore la cryptographie asymétrique RSA, les notions de clé publique/privée, ainsi que l’algorithme de **sac à dos** utilisé pour coder et décoder des messages.

📌 **Fichiers principaux** :
- `Ex1.py` à `Ex3.py` : exemples de chiffrés/déchiffrés RSA avec variations.
- `RSA.py` : implémentation du système RSA.
- `SacDos.py` : résolution du problème du sac à dos (version simple & difficile).
- `ExSacDos.py` : démonstrations des algorithmes de sac à dos.
- `OutilsMath.py` : fonctions utilitaires (PGCD, Euclide étendu, primalité, etc.)
- `AlphaSimple.py` : alphabet utilisé pour certains chiffrages.

📌 **Fonctionnalités** :
- Génération et manipulation de clés RSA (public/privé)
- Implémentation manuelle des opérations RSA : chiffrement, déchiffrement
- Transformation d’un sac super-croissant en sac difficile
- Algorithme glouton de décodage
- Faciliteur (clé secrète pour l’inversion du sac)
- Tests de primalité (Miller-Rabin)
- Exemples chiffrés commentés

---

### 🗂️ 2. Chiffrement Classique (César, Vigenère, Affine)

Ce module présente plusieurs algorithmes de chiffrement classiques utilisés avant les systèmes modernes.

📌 **Fichiers principaux** :
- `main.py` : script principal de test des fonctions
- `fonctionsCryptage.py` *(présumé manquant)* : contient les fonctions appelées (César, Affine, Vigenère, Inverse)

📌 **Fonctionnalités testées** :
- `Code()` : inverse un texte
- `Cesar(msg, k)` : chiffrement de César
- `Vigenere(msg, clé)` : chiffrement/déchiffrement de Vigenère
- `CesarAffine(msg, a, b)` : chiffrement affine avec inverse
- `decrypteCesarAffine(msg, a, b)` : déchiffrement affine

⚠️ **Note** : le fichier `fonctionsCryptage.py` est requis pour faire fonctionner `main.py` (il semble absent du dépôt pour l’instant).

---

## 🚀 Lancer les tests

### ▶️ Chiffrement RSA & Sac à dos

```bash
python Ex1.py
python Ex2.py
python Ex3.py
python ExSacDos.py
