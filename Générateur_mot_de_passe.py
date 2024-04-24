import random
import time


longPass=int(input("Enter a long passphrase : ")) # User will enter the number of characters in their passphrase.
print()
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&é'(-è_çà)@" #

PassFrase = "".join([random.choice(s) for i in range(longPass)]) # Generate a password with the length of longPass
for i in range(3): # On boucle 3 fois pour avoir une moyenne pondérée sur plusieurs essais.
    time.sleep(0.7)
    print("\rGenerating... %d%%"%((i+1)/3*100),end="")# Affichage de la progression en pourcentage.
print()
print ("Your generated Passphrase is : ", PassFrase)
print()
print("End of proramme")