import pygame
import sys
import random

pygame.init()

#SCREEN ------------------------------------------------------------------------------

WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#COULEURS ----------------------------------------------------------------------------

ROUGE = (255,0,0)
VERT = (0,200,0)
CIEL = (220,220,255)
NOIR = (0,0,0)
BEIGE = (255,170,170)
screen.fill(CIEL)

#AFFICHAGE PENDU ---------------------------------------------------------------------

pendu1 = pygame.image.load("Assets/pendu1.png")
pendu1 = pygame.transform.scale(pendu1,(500,400))

pendu2 = pygame.image.load("Assets/pendu2.png")
pendu2 = pygame.transform.scale(pendu2,(500,400))

pendu3 = pygame.image.load("Assets/pendu3.png")
pendu3 = pygame.transform.scale(pendu3,(500,400))

pendu4 = pygame.image.load("Assets/pendu4.png")
pendu4 = pygame.transform.scale(pendu4,(500,400))

pendu5 = pygame.image.load("Assets/pendu5.png")
pendu5 = pygame.transform.scale(pendu5,(500,400))

pendu6 = pygame.image.load("Assets/pendu6.png")
pendu6 = pygame.transform.scale(pendu6,(500,400))

pendu7 = pygame.image.load("Assets/pendu7.png")
pendu7 = pygame.transform.scale(pendu7,(500,400))


#FONCTIONNEMENT -----------------------------------------------------------------------

#IMPORTATION MOTS + TRIAGE DIFFICULTE -------------------------------------------------

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

#CHOIX DU MOT -------------------------------------------------------------------------

mot = random.choice(difficle)
mot = mot[1:]
long = len(mot)-1
masque = str(long*"_")

#AFFICHAGE TEXTE ----------------------------------------------------------------------

fontbold = pygame.font.SysFont("funneldisplayextrabold",60)
font = pygame.font.SysFont("funneldisplay",32)
win = font.render("Et c'est gagné !",True,VERT)
winRect = win.get_rect(topleft=(450,245))
lose = font.render("Vous avez perdu..",True,ROUGE)
loseRect = lose.get_rect(topleft=(450,245))

#FONCTIONS ----------------------------------------------------------------------------

def remplace(st:str,i:int,s:str)->str:
    l = []
    for e in st:
        if e in st:
            l.append(e)
    for ind in range(len(l)):
        if ind == i:
            l[ind] = f"{s}"
    st = ""
    for el in l:
        st += el
    return st

#TOUCHES ------------------------------------------------------------------------------

commandes = [pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d,pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h,pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_m,pygame.K_n,pygame.K_o,pygame.K_p,pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t,pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x,pygame.K_y,pygame.K_z]

#BOUCLE  ------------------------------------------------------------------------------

chances = 1
inp = []
running = True
lettres = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(CIEL)
    utilise = font.render(f"Lettres utilisés : {lettres}",True,NOIR)
    utiliseR = utilise.get_rect(topleft=(330,70))
    screen.blit(utilise,utiliseR)

    #JEU -----------------------------------------------------------------------------

    mask = fontbold.render(masque,True,NOIR)
    maskR = mask.get_rect(topleft=(400,140))
    screen.blit(mask,maskR)

    #VERIFICATIONS ------------------------------------------------------------------- 

    if "_" not in masque:
        screen.blit(win,winRect)
        pygame.display.flip()
        pygame.time.delay(1000)
        running = False
    if chances == 1: 
        screen.blit(pendu1,(300,300))
    if chances == 2:
        screen.blit(pendu2,(300,300))
    if chances == 3:
        screen.blit(pendu3,(300,300))
    if chances == 4:
        screen.blit(pendu4,(300,300))
    if chances == 5:
        screen.blit(pendu5,(300,300))
    if chances == 6:
        screen.blit(pendu6,(300,300))    
    if chances == 7:
        screen.blit(pendu7,(300,300))
    if chances > 7:
        screen.blit(lose,loseRect)
        pygame.display.flip()
        pygame.time.delay(1000)
        running = False

    keys = pygame.key.get_pressed()
    
    #SAVOIR SI UNE LETTRE EST DANS LE MOT ----------------------------------------------

    pygame.time.delay(200)
    for touche in commandes:
        if keys[touche]:
            keyn = pygame.key.name(touche)
            lettres += keyn
            if keyn in mot:
                i = 0
                while i < len(mot):
                    if mot[i] == keyn:
                        masque = remplace(masque,i,keyn)
                    i += 1
                    print(masque)
            else:
                faux = font.render(f"La lettre {keyn} n'est pas dans le mot ! Vous avez encore {7-chances} ESSAIS..",True,ROUGE)
                fauxR = faux.get_rect(topleft=(100,245))
                p = 0
                screen.blit(faux,fauxR)
                pygame.display.flip()
                pygame.time.delay(1000)
                chances += 1
                p = 1
                print(f"Touche {pygame.key.name(touche)} maintenue !")
            
    pygame.display.flip()

sys.exit()
pygame.quit()