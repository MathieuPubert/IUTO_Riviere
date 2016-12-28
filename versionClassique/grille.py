# -*- coding:UTF-8 -*-
from case import *


def GrilleHexa(nbLig,nbCol,paire=True,valeur=None):
    """
    Grille de cases hexagonales
    :param nbLig: integer. Nombre de lignes de la grille
    :param nbCol: integer. Nombre d ecolonnes de la grille
    :param paire: bool. Les lignes paires contiennent les colonnes paires
    :param valeur: Valeur par défaut des cases de la grille. Idéalement une Case()
    :return: dictionnaire. {'lignes':nbLig, 'colonnes':nbCol, 'estPaire':paire, '(0,0):None'}
    """
    d_grille={'lignes':nbLig,
              'colonnes': nbCol,
              'estPaire':paire}

    for x in range(nbLig):
        for y in range(nbCol):

            if d_grille['estPaire'] and x%2==y%2: #Si paire est True et x, y pairs/impairs ensemble
                d_grille[(x,y)]=valeur

            elif not d_grille['estPaire'] and x%2!=y%2:
                d_grille[(x,y)]=valeur

            else:
                d_grille[(x,y)]="WTF???"

    return d_grille

def getNbLigGH(grille):
    """
    Donne le nombre de lignes de la grille
    :param grille: retour de la fonction GrilleHexa
    :return: integer. Nombre de lignes de grille
    """
    return grille['lignes']


def getNbColGH(grille):
    """
    Donne le nombre de colonnes de la grille
    :param grille: retour de la fonction GrilleHexa
    :return: integer. Nombre de colonnes de grille
    """
    return grille['colonnes']

def estPaireGH(grille):
    """
    Indique si la grille est paire
    :param grille: retour de la fonction GrilleHexa
    :return: bool. True si la grille est paire
    """
    return grille['estPaire']

def estPosGH(grille,lig,col):
    """
    Indique si une position fait partie de la grille par exemple si la grille est paire, lig vaut 2 et col vaut 3
    la fonction retourne False car il n'y a pas de colonne 3 dans une ligne
    :param grille: retour de la fonction GrilleHexa
    :param lig: integer. Indice de ligne
    :param col: integer. Indice de colonne
    :return: bool. True si la position est valide
    """
    estvalide=False
    if (grille['estPaire'] and lig%2==col%2) or (not grille['estPaire'] and lig%2!=col%2):
        estvalide=True
    return estvalide


def getValGH(grille,lig,col):
    """
    Retourne la valeur(contenu) de la case de la grille aux coordonnées (lig,col)
    :param grille: retour de la fonction GrilleHexa
    :param lig: integer. Indice de ligne
    :param col: integer. Indice de colonne
    :return: valeur de la grille à (lig,col)
    """
    val=None
    if estPosGH(grille, lig, col):
        val=grille[(lig,col)]
    return val


def setValGH(grille,lig,col,val):
    """
    Affecte la valeur de la grille aux coordonnées (lig,col)
    :param grille: retour de la fonction GrilleHexa
    :param lig: integer. Indice de ligne
    :param col: integer. Indice de colonne
    :param val: valeur à affecter.
    :return: None. Modifie la grille
    """
    if estPosGH(grille, lig, col):
        grille[(lig,col)]=val



def incDirectionGH(direction):
    """
    Donne un vecteur mouvement (+x,+y) à appliquer a des coordonnées pour un deplacement
    :param direction: string. sens du déplacement
    :return: tuple. (+x, +y). renvoie un vecteur (0,0) si la direction est inexistante
    """
    d_modificateurs={'N':(-2,0),
                     'NE':(-1,1),
                     'E':(0,2),
                     'SE':(1,1),
                     'S':(2,0),
                     'SW':(-1,1),
                     'W':(-2,0),
                     'NW':(-1,-1)}

    return d_modificateurs.get(direction, (0,0))


def getNProchainsGH(grille,lig,col,direction,n=3):
    """
    Permet de retourner la liste des n valeurs qui se trouvent dans la grille
    dans une direction donnée à partir de la position lig,col
    si il y a moins n celulles dans la grille dans la direction données on retourne
    toutes le cellules trouvées
    :param grille: retour de la fonction GrilleHexa
    :param lig: integer. Indice de ligne
    :param col: integer. Indice de colonne
    :param direction: string. Clé du dictionnaire directions
    :param n: integer. Nombre de cases maximum à retourner
    :return: liste. [d_grille[(x1,y1)],d_grille[(x2,y2)],d_grille[(x3,y3)]]
    """
    l_valeurs=[]
    vx,vy=incDirectionGH(direction) #je récupère le vecteur mouvement
    for i in range(n):
        # Calcul de la valeur de la cellule aux coordonnées :
        # x= position initiale +  abscisse vecteur mouvement*pas
        # y= position initiale +  ordonnées vecteur mouvement*pas
        # Si les coordonnées n'existent pas, je ne rentre rien dans la liste
        valeur = grille.get((lig + (i * vx), col + (i * vy)), None)
        if valeur is not None:
            l_valeurs.append(valeur)

    return l_valeurs


# fonction d'initiation d'une grille avec des caractères pour faire des tests
# la grille doit être créée
def initAlphaGH(grille):
    possibles='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    nbLig=getNbLigGH(grille)
    nbCol=getNbColGH(grille)
    if estPaireGH(grille):
        dec=0
    else:
        dec=1
    k=0
    for i in range(nbLig):
        for j in range(dec,nbCol,2):
            setValGH(grille, i, j, possibles[k])
            k = (k + 1) % len(possibles)
        dec=(dec+1)%2




################################################################# FONCTION SEMBLE ERRONNEE #############################
# affichage en mode texte d'une grille hexagonale        
def afficheGH(grille):
    nbLig=getNbLigGH(grille)
    nbCol=getNbColGH(grille)
    if estPaireGH(grille):
        print(" ", end='')
        debut=0
    else:
        debut=1
        print("   ",end='')
    for j in range(debut,nbCol,2):
        print("_   ",end='')
    print()

    c1=c2=' '
    for i in range(nbLig):
        if debut==1:
            print(c1+'_',end='')
        prem=''
        for j in range(debut,nbCol,2):
            print(prem+'/'+str(getValGH(grille,i,j))+'\\',end='')
            prem='_'
        if j!=nbCol-1:
            print('_'+c2)
        else:
            print()
        c1='\\'
        c2='/'
        debut=(debut+1)%2
    if debut==1:
        print('\\',end='')
        debut=0
    else:
        print('  \\',end='')
        debut=1
    for j in range(debut,getNbColGH(grille)-2,2):
        print('_/ \\',end='')
    print('_/')

########################################################################################################################

########################################################################################################################
#TESTS
########################################################################################################################

if __name__=='__main__':
    print('Grille paire :')
    grille_P = GrilleHexa(10, 10, True)
    grille_I = GrilleHexa(5, 5, False)
    print('Grille paire vide:')
    afficheGH(grille_P)
    print('Grille paire remplie:')
    initAlphaGH(grille_P)
    afficheGH(grille_P)
    print('Grille paire avec valeur modifiée en (2,2):')
    # Comportement pas joli, mais attendu. On souhaite voir le contenu de l'hexagone de la grille au coordonnées, qui est une case
    setValGH(grille_P, 2, 2, Case('J', 'X'))
    afficheGH(grille_P)

    print('Grille impaire vide:')
    afficheGH(grille_I)
    print('Grille impaire remplie:')
    initAlphaGH(grille_I)
    afficheGH(grille_I)
    print('Grille impaire avec valeur modifiée en (2,2), valeur absente:')
    # Comportement pas joli, mais attendu. On souhaite voir le contenu de l'hexagone de la grille au coordonnées, qui est une case
    setValGH(grille_I, 2, 2, Case('J', 'X'))
    afficheGH(grille_I)
