import time
from jeu import *
from ia import *

def saisirDirection():
    print("Choisissez votre direction (X, N, S, NO, NE, SO, SE)")
    rep=input()
    return rep

def afficheJeu(jeu,msg=''):
    print('\x1b[2J')
    afficheRiviere(getRiviere(jeu))
    if getNbJoueursJ(jeu)!=0:
        print("c'est au tour du joueur",getNom(getJoueurCourantJ(jeu)),"de jouer")
        print("Il lui reste "+str(getNbCoupsRestants(jeu))+" coups à effectuer")
    else:
        print("Partie terminée")
    print(msg)
    
def afficherClassement(jeu):
    classement=getClassement(jeu)
    print("CLASSEMENT")
    print("----------")
    for i in range(getNbJoueurs(classement)):
        print(i+1,'->',getNom(getJoueurI(classement,i)))
        
# cette fonction permet de choisir des joueurs parmi la liste de joueurs possibles
def saisirJoueurs(joueurs):
    rep=1
    possibles=getJoueursPossibles(joueurs)
    noms=getListeNomsJoueur(possibles)
    while len(noms)>0 and rep!='Q':
        print("Quel joueur souhaitez vous représenter?")
        print("Pour un joueur automatique tapez l'initale en minuscule")
        print("Q. Quitter")
        for nom in noms:
            print(getRepresentationJoueur(possibles,nom)+".",nom)
        rep=input()
        nom2=getNomJoueur(possibles,rep.upper())
        if nom2 != None:
            humain=rep.upper()==rep
            print('Vous avez choisi',nom2,end=' ')
            if not humain:
                print('en mode automatique')
            ajouterJoueur(joueurs,nom2,humain)
            noms.remove(nom2)

    print("Voici la liste des joueurs",getNbJoueurs(joueurs))
    for i in range(getNbJoueurs(joueurs)):
        j=getJoueurI(joueurs,i)
        print(getNom(j),"représenté par",getRepresentation(j),end=' ')
        if estHumain(j):
            print('est humain')
        else:
            print('est automatique')
     
def jouerUnePartie(jeu):
    initJeu(jeu)
    attenteDirection=True
    afficheJeu(jeu)
    while getNbJoueursJ(jeu)!=0:
        time.sleep(0.1)
        if attenteDirection:
            joueurCourant=getJoueurCourantJ(jeu)
            if estHumain(joueurCourant):
                direction=saisirDirection()
            else:
                direction=choixDirection(jeu)
            attenteDirection=False
        else:
            if getNbCoupsRestants(jeu)==0:
                    attenteDirection,msg=finirDeplacement(jeu)
            else:
                msg=jouerDirection(jeu,direction)
                attenteDirection=getNbCoupsRestants(jeu)!=0
            afficheJeu(jeu,msg)
            
    print("Fin du jeu")
    afficheJeu(jeu)
    afficherClassement(jeu)
    
        
def jouer(jeu):
    fini=False
    while not fini:
        saisirJoueurs(getJoueursJ(jeu))
        jouerUnePartie(jeu)
        rep=input("Voulez-vous rejouer (O/N)? ")
        fini=rep not in 'oO'

        
j=Jeu("./","joueurs.txt","riviere1.txt")
jouer(j)