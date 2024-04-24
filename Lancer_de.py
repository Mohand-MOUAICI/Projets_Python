import random
import time

# Afficher des etoiles
def pointiers():
    for i in range(3):
        print("*", end="",  flush=True)
        time.sleep(0.8)
    print()

print("Bienvenue dans le jeux du dé")

while True:
    x = int(input("Entrez 1 pour Lancer le de, ou 0 pour arreter : ")) #  On veut que l'utilisateur entre un nombre entier
    if x==0:
        pointiers()
        print("Arret du programme, à la prochaine")
        break
    elif x==1:
        pointiers()
        print(random.randint(1, 6)) # Generer un nombre aléatoire entre 1 et nb_max (inclusif)
    else:
        pointiers()
        print("Valeur incorrecte, veuillez entrer une valeur entre  0 et 1.")
