import random
from jeu import *


# Cette fonction retourne une grille hexgonale qui donne pour chaque case de la
# rivière sa distance jusqu'à la case qui se trouve en lig,col
def marquage(riviere,lig,col):
    pass

# fonction qui choisit automatiquement une direction (qui doit être une 
# direction valide) pour le joueur courant. L'implémentation choisi aléatoirement
# une direction mais vous pouvez l'améliorer notamment avec la fonction précédente
def choixDirection2(jeu):
    (lig,col)=getPosJoueurCourant(jeu)
    r=getRiviere(jeu)
    aux=[]
    for direction in getDirections():
        if verifDirection(jeu,direction)==DIRECTION_OK:
            aux.append(direction)
    return random.choice(aux)