import random
from math import *
from jeu import *


# Cette fonction retourne une grille hexgonale qui donne pour chaque case de la
# rivière sa distance jusqu'à la case qui se trouve en lig,col
def marquage(riviere, lig, col):
    marque = GrilleHexa(getNbLigR(riviere), getNbColR(riviere), estPaireR(riviere), 0)
    i=0
    while i < getNbLigGH(marque):
        j=0
        while j < getNbColGH(marque):
            if estPosGH(marque, i, j):
                (a,b)=(i,j)
                (a,b)=((a+b)/2,(b-a)/2)
                (c,d)=(lig,col)
                (c,d)=((c+d)/2,(d-c)/2)
                res = int((abs(c-a)+abs(d-b)+abs(c-a+d-b))/2)
                setValGH(marque, i, j, res)
            j+=1
        i+=1
    return marque


# fonction qui choisit automatiquement une direction (qui doit être une
# direction valide) pour le joueur courant. L'implémentation choisi aléatoirement
# une direction mais vous pouvez l'améliorer notamment avec la fonction précédente
def choixDirection(jeu):
    r = getRiviere(jeu)
    marque = marquage(r, getNbLigR(r), getColArrivee(r))
    (lig, col) = getPosJoueurCourant(jeu)
    listeDirectionVerif = []
    direction = {"S": getValGH(marque, lig+2, col), "SO": getValGH(marque, lig+1, col-1),
                 "SE": getValGH(marque, lig+1, col+1), "N": getValGH(marque, lig-2, col),
                 "NE": getValGH(marque, lig-1, col+1), "NO": getValGH(marque, lig-1, col-1)}
    for elem in direction:
        if verifDirection(jeu, elem) == DIRECTION_OK:
            listeDirectionVerif.append(direction[elem])

    for a, b in direction.items():
        if b == min(listeDirectionVerif):
            return a


def choixDirectionAlea(jeu):
    (lig, col) = getPosJoueurCourant(jeu)
    r = getRiviere(jeu)
    aux = []
    for direction in getDirections():
        if verifDirection(jeu, direction) == DIRECTION_OK:
            aux.append(direction)
    return random.choice(aux)


# TESTS
if __name__ == '__main__':

    print ("Test marquage(Riviere(12, 9, True, 0, 0),6,4) :")
    afficheGH(marquage(Riviere(12, 9, True, 0, 0),6,4))
    print ("\n")

    game=Jeu('./data/', 'joueurs.txt', 'riviere1.txt')
    for (nom, representation) in getJoueursPossibles(getJoueursJ(game)).items():
        ajouterJoueurJ(game, Joueur(nom, representation,True))
    initJeu(game)

    print ("Test choixDirection(game) :", choixDirection(game))
