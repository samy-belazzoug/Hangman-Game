import random

mots = open("mots.txt","r")

facile = []
moyen = []
difficle = []

for mot in mots:
    if "F" in mot:
        facile.append(mot)
    if "M" in mot:
        moyen.append(mot)
    if "H" in mot:
        difficle.append(mot)

mot = random.choice(difficle)
mot = mot[1:]
long = len(mot)-1
masque = str(long*"_")

#FONCTIONS -----------------------------------------------------------------

def remplace(st:str,i:int,s:str)->str:
    l = []
    for e in st:
        if e in st:
            l.append(e)
    for ind in range(len(l)):
        if ind == i:
            l[ind] = s
    st = ""
    for el in l:
        st += el
    return st

#BOUCLE DE JEU -------------------------------------------------------------

alphabet = "abcdefghijklmnopqrstuvwxyz"
chances = 1
inp = []
while chances != 7:

    print(masque,"\n")

    #CHECK WIN

    if "_" not in masque:
        print("Et c'est gagné, vous repartez avec Modique Somme !")
        break

    user = str(input("Veuillez saisir une lettre : "))

    #VERIFICATIONS INPUT ----------------------------------------------------

    erreur = 0
    
    if user in inp:
        erreur = 2
        print("Vous avez déja entré cette lettre, je suis gentil je vous laisse une chance mais innovez s'il vous plaît.")
    
    inp.append(user)
    
    
    if user not in alphabet:
        erreur = 1
    if len(user) != 1:
        erreur = 1

    if erreur == 1:
        print("Je réiteire mes propos. Veuillez s'il vous plaît saisir une lettre minuscule : ")

    #SAVOIR SI LETTRE EST DANS LE MOT

    if erreur == 0:
        
        user = user.lower()
        
        if user in mot:
            i = 0
        
            while i < len(mot):
        
                if mot[i] == user:
                    masque = remplace(masque,i,mot[i])
                i += 1
        else:
            print(f"EH NAN IL Y EST PAS,VOUS AVEZ encore {7-chances} ESSAIS")
            chances += 1
        
if chances >= 7:
    print(masque)
    print("Vous avez perdu. Bah alors, loser.")

    erreur = 0