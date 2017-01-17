import random
from grille import *
from case import *

# La rivière est une grille hexagonale qui stokera des cases (telles que définies dans
# le fichier case.py. En plus elle contient une colonne de départ sur la 1ere ligne
# et une colonne d'arrivée sur le dernière ligne


def Riviere(nbLig,nbCol,paire=True, colDepart=0,colArrivee=0):
    """
    Représentation de la rivière sur laquelle les joueurs évolueront
    :param nbLig: integer. Nombre de lignes
    :param nbCol: integer. Nombre de colonnes
    :param paire: bool. True si les colonnes paires contiennent les lignes paires
    :param colDepart: integer. Indice de la colonne de départ
    :param colArrivee: integer. Indice de la colonne d'arrivée
    :return: Dictionnaire.
    """
    d_riviere = {'Lignes': nbLig,
                 'Colonnes': nbCol,
                 'Paire': paire,
                 'Depart': colDepart,
                 'Arrivée': colArrivee}

    # Dans la foulée je vais rajouter une premiere initialisation aux valeurs paramètrées
    initRiviere(d_riviere, d_riviere['Lignes'], d_riviere['Colonnes'], d_riviere['Paire'])

    return d_riviere



def initRiviere(r,nbLig,nbCol,paire):
    """
    Initialise une rivière. Ecrase nbLig,nbCol, paire de Riviere()
    :param r: retour de la fonction Riviere()
    :param nbLig: integer. Nombre de lignes de la riviere
    :param nbCol: integer. nombre de colonnes de la riviere
    :param paire: bool. True si les lignes paires contiennent les colonnes paires (cf API grille)
    :return: None. Modifie r
    """
    r['Lignes'] = nbLig
    r['Colonnes'] = nbCol
    r['Paire'] = paire
    r['Grille'] = GrilleHexa(nbLig, nbCol, paire, Case(VIDE, 'X'))



# retourne la colonne de départ de la rivière
def getColDepart(r):
    return r['Depart']

# retourne la colonne d'arrivée de la rivière
def getColArrivee(r):
    return r['Arrivée']

# retourne le nombre de lignes de la rivière
def getNbLigR(r):
    return r['Lignes']

# retourne le nombre de colonnes de la rivière
def getNbColR(r):
    return r['Colonnes']

# indique si la rivière est paire ou non
def estPaireR(r):
    return r['Paire']

# retourne la case qui se trouve à la ligne l colonne c
def getCase(r,l,c):
    pass

# met la case dans la rivière à la ligne l colonne c
def setCase(r,l,c,case):
    pass

# retourne le contenu (l'objet) qui se trouve sur la case à la ligne l colonne c
def getContenuR(r,l,c):
    pass

# met un objet (tronc, joueur, rocher) sur la case qui se trouve à la ligne l colonne c
def setContenuR(r,l,c,contenu):
    pass

# retourne le courant de la case qui se trouve sur la case à la ligne l colonne c
def getCourantR(r,l,c):
    pass

# met le courant sur la case qui se trouve à la ligne l colonne c
def setCourantR(r,l,c,courant):
    pass

# recupère la grille qui représente la rivière
def getGrille(r):
    pass

# vérifie que la position (l,c) est bien une position de la rivière
def estPosR(r,l,c):
    pass

# cette fonction enlève le contenu de la case arrivée de la rivière
def viderArrivee(riviere):
    pass

# retrouve la position (l,c) du joueur dont la représentation des repJoueur sur la grille
# si le joueur n'est pas sur la grille la fonction retourne (-1,-1)
def getPositionJoueur(r,repJoueur):
    pass
            
# permet de compter combien il y a d'obstacles contigues devant la case lig,col 
# en allant dans la direction direction
# n indique jusqu'à quelle distance on recherche les obstacles
def getNbObstacles(riviere,lig,col,direction,n=3):
    pass

# retourne le nom du joueur qui se trouve sur la case d'arrivée et None si il n'y
# a pas de joueur sur cette case
def joueurArrive(r):
    pass

# cette fonction verifie que le déplacement partant de la case en position (lig,col)
# en direction de direction est bien possible
def deplacementAutorise(riviere,lig,col,direction):
    pass

# deplace un objet placé sur la case de position (lig,col) dans la direction direction
# Attention la fonction doit "pousser" dans la même direction les objets qui trouvent devant.
# On considère que lorsqu'on appelle la fonction le déplacement est possible
# La fonction retourne la représentation du joueur qui se trouve sur la case d'arrivée
# si il y en a un et None sinon
def deplacer(riviere,lig,col,direction):
    pass

# Cette fonction retourne la position (lig,col) de l'objet qui se trouve sur
# une case courant qui a le moins d'objet devant lui et qui se trouve le plus au
# nord ouest possible
# si aucun objet n'est à dans ce cas la fonction retourne (-1,-1)
def getMinADeplacer(r):
    pass


                       
# cette fonction affiche une rivière en mode texte
# Attention! ne marche pas dans le terminal de Wing
def afficheRiviere(riviere):
    grille=getGrille(riviere)
    paire=estPaireGH(grille)
    nbLig=getNbLigGH(grille)
    nbCol=getNbColGH(grille)
    colDep=getColDepart(riviere)
    colArr=getColArrivee(riviere)
    if paire:
        print(" ",end='')
        debut=0
    else:
        debut=1
        print("   ",end='')
    for j in range(debut,nbCol,2):
        if j==colDep:
            print("↓   ",end='')
        else:
            print("_   ",end='')
    print()

    c1=c2=' '
    c=cprec=None
    for i in range(nbLig):
        if debut==1:
            if i<2:
                print(c1+'_',end='')
            else:
                print(c1+'\x1b[4m'+getCourantChar(getValGH(grille,i-1,0))+'\x1b[0m',end='')
        prem=''
        for j in range(debut,nbCol,2):
            c=getValGH(grille,i,j)
            print(prem+'/'+getContenu(c)+'\\',end='')
            if i==0 or j==getNbColGH(grille)-1:
                prem="_"
            else:
                prem='\x1b[4m'+getCourantChar(getValGH(grille,i-1,j+1))+'\x1b[0m'


        if j==nbCol-1:
            print()
        else:
            print(prem+c2)
        c1='\\'
        c2='/'
        debut=(debut+1)%2
    if debut==1:
        print('\\',end='')
        debut=0
    else:
        print('  \\',end='')
        debut=1
    for j in range(debut,nbCol-2,2):
        if j==colArr:
            print(' / \\',end='')
        else:
            print('\x1b[4m'+getCourantChar(getValGH(grille,nbLig-1,j))+'\x1b[0m/ \\',end='')

    if j+2==colArr:
        print(' /')
    else:
        print('\x1b[4m'+getCourantChar(getValGH(grille,nbLig-1,j+2))+'\x1b[0m/')
    print()

# Cette fonction permet d'initialiser une rivière en fonction du contenu d'un fichier texte
def lireRiviere(nomFic):
    fic=open(nomFic)
    r=None
    for ligne in fic:
        decomp=ligne.split(",")
        if decomp[0]=="entete":
            nbLig=int(decomp[1])
            nbCol=int(decomp[2])
            paire=decomp[3]=="True"
            colDepart=int(decomp[4])
            colArrivee=int(decomp[5])
            r=Riviere(nbLig,nbCol,paire,colDepart,colArrivee)
        elif decomp[0]=='rocher':
            for i in range(1,len(decomp),2):
                lig=int(decomp[i])
                col=int(decomp[i+1])
                setContenuR(r,lig,col,ROCHER)
        elif decomp[0]=='tronc':
            for i in range(1,len(decomp),2):
                lig=int(decomp[i])
                col=int(decomp[i+1])
                setContenuR(r,lig,col,TRONC)
        elif decomp[0] in ["N","S","NO","SO","SE","NE"]:
            for i in range(1,len(decomp),2):
                lig=int(decomp[i])
                col=int(decomp[i+1])
                setCourantR(r,lig,col,decomp[0])
        else:
            for i in range(1,len(decomp),2):
                lig=int(decomp[i])
                col=int(decomp[i+1])            
                setContenuR(r,lig,col,decomp[0])
            
    fic.close()
    return r
