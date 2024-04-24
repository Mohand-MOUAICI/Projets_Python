import random

choix =  ["Ciseaux", "Papier", "Pierre"]
score_utilisateur = 0
score_machine = 0
choix_num = 1

while True:
    cpu = random.choice(choix)
    # print(cpu)
    print("Round", choix_num)
    choix_utilisateur = input("Faite votre choix : ")
    if choix_utilisateur not in choix:
        print('Votre choix est incorrect')
        continue
    elif (choix_utilisateur == "Ciseaux" and cpu == "Ciseaux") or (choix_utilisateur == "Papier" and cpu == "Papier") or (choix_utilisateur == "Pierre" and cpu == "Pierre"):
        print("La machine à joué : ", cpu, "Egalité")
        choix_num  +=1

    elif (choix_utilisateur == "Ciseaux" and cpu == "Papier") or (choix_utilisateur == "Papier" and cpu == "Pierre") or (choix_utilisateur == "Pierre" and cpu == "Ciseaux"):
        print("La machine à joué : ", cpu, "Vous avez gagné !")
        score_utilisateur  += 1
        choix_num  +=1

    elif (choix_utilisateur == "Ciseaux" and cpu == "Pierre") or (choix_utilisateur == "Papier" and cpu == "Ciseaux") or (choix_utilisateur == "Pierre" and cpu == "Papier") :
        print("La machine à joué : ", cpu, "Vous avez perdu...")
        score_machine += 1
        choix_num  +=1
        
    rejouer = input("\nVoulez-vous rejouer ? O/N\n").lower()
    
    if rejouer != 'o':
        print("Votre score", score_utilisateur, "/", "Score machine", score_machine)
        if score_utilisateur  > score_machine:
            print("Vous avez battu la machine ! Bravo !")
        elif score_machine > score_utilisateur:
            print("La machine vous a battue ! Patience pour le prochain.")
        else:
            print("Match nul ! Essayez encore une fois.")
        print("Au revoire")
        break