texte = str(input("Entrez une chaine de caractére : "))

def accro_gen(texte):
    mots = texte.split()
    print("Voici le texte : ",texte)
    print("Voici les mots du texte : ",mots)
    accro = ""
    for i in mots:
        accro = accro+str(i[0]).upper() + "-"
    print("L'acronyme est :",accro[:-1])

accro_gen(texte)