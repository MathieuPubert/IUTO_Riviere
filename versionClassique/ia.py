import random
from math import *
from jeu import *


# Cette fonction retourne une grille hexgonale qui donne pour chaque case de la
# rivière sa distance jusqu'à la case qui se trouve en lig,col
def marquage(riviere, lig, col):
    marque = GrilleHexa(getNbLigR(riviere), getNbColR(riviere), estPaireR(riviere), 0)
    i=0
    while i < len(marque["valeurs"]):
        j=0
        while j < len(marque["valeurs"][i]):
            if estPosGH(marque, i, j):
                (a,b)=(i,j)
                (a,b)=((a+b)/2,(b-a)/2)
                (c,d)=(lig,col)
                (c,d)=((c+d)/2,(d-c)/2)
                marque["valeurs"][i][j] = int((abs(c-a)+abs(d-b)+abs(c-a+d-b))/2)
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
    direction = {"S": marque["valeurs"][lig + 2][col], "SO": marque["valeurs"][lig + 1][col - 1],
                 "SE": marque["valeurs"][lig + 1][col + 1], "N": marque["valeurs"][lig - 2][col],
                 "NE": marque["valeurs"][lig - 1][col + 1], "NO": marque["valeurs"][lig - 1][col - 1]}
    for elem in direction:
        print ("testDebug getPosJoueurCourant :")
        print (getPosJoueurCourant(game))
        if verifDirection(jeu, elem) == DIRECTION_OK:
            listeDirectionVerif.append(direction[elem])
    print ("testDebug listeDirectionVerif :")
    print (listeDirectionVerif)
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

    game=Jeu('./data/', 'joueurs.txt', 'riviere1.txt')
    initJeu(game)
    for (nom, representation) in getJoueursPossibles(getJoueursJ(game)).items():
        ajouterJoueurJ(game, Joueur(nom, representation))

    print ("Test choixDirection(game) :")
    choixDirection(game)
    print ("Test choixDirectionAlea(game) :")
    choixDirectionAlea(game)
