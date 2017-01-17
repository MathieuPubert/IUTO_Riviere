import random
from jeu import *

# Cette fonction retourne une grille hexgonale qui donne pour chaque case de la
# rivière sa distance jusqu'à la case qui se trouve en lig,col
def marquage(riviere,lig,col):
    marque=GrilleHexa(getNbLigR(riviere),getNbColR(riviere),estPaireR(riviere),0)
    for cpt in range(int(getNbLigR(riviere)*(getNbColR(riviere)/2))):
        ligCpt=1
        if estPaireR(riviere) :
            colCpt=1
        else :
            ligCpt=2
        marque["valeurs"][ligCpt][colCpt]=abs(lig-ligCpt+col-colCpt)
        if colCpt+2>getNbColR(riviere):
            ligCpt+=1
        else:
            colCpt+=2
    return marque

# fonction qui choisit automatiquement une direction (qui doit être une 
# direction valide) pour le joueur courant. L'implémentation choisi aléatoirement
# une direction mais vous pouvez l'améliorer notamment avec la fonction précédente
def choixDirection2(jeu):
    r=getRiviere(jeu)
    marque=marquage(r,getNbLigR(r),getColArrivee(r))
    (lig,col)=getPosJoueurCourant(jeu)
    S=marque["valeurs"][lig+2][col]
    SO=marque["valeurs"][lig+1][col-1]
    SE=marque["valeurs"][lig+1][col+1]
    tmp=[]
    if verifDirection(jeu,"S")==DIRECTION_OK:
        tmp.append(S)
    if verifDirection(jeu,"SO")==DIRECTION_OK:
        tmp.append(SO)
    if verifDirection(jeu,"SE")==DIRECTION_OK:
        tmp.append(SE)
    if min(tmp)==S:
        return "S"
    if min(tmp)==SO:
        return "SO"
    if min(tmp)==SE:
        return "SE"

#    (lig,col)=getPosJoueurCourant(jeu)
#    r=getRiviere(jeu)
#    aux=[]
#    for direction in getDirections():
#        if verifDirection(jeu,direction)==DIRECTION_OK:
#            aux.append(direction)
#    return random.choice(aux)
