import random
import winsound

nombre_generer = random.randint(0, 9)
tentative = 0
score = 0

while True:
    nombre_deviner = input("Deviner un nombre entre  0 et 9 ou  'q' pour quitter : ")
    
    if nombre_deviner == 'q':
        print('Au revoir')
        winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) # Jouer un son de fermeture
        break
    elif int(nombre_deviner) == nombre_generer:
        print("Félicitations vous avez deviné le nombre correctement.")
        tentative +=1
        score += 1
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS) # Jouer un son de notification de succès
        break
        
    elif int(nombre_deviner) < nombre_generer:
        print("Votre nombre est trop petit.")
        tentative += 1
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS) # Jouer un son d'erreur système
        
    else:
        print("Votre nombre est trop grand.")
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS) # Jouer un son d'erreur système
        tentative += 1
print("Votre score est de",  score,"/", tentative)