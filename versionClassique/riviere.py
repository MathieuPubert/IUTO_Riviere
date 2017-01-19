import random
from grille import *
from case import *


# La rivière est une grille hexagonale qui stokera des cases (telles que définies dans
# le fichier case.py. En plus elle contient une colonne de départ sur la 1ere ligne
# et une colonne d'arrivée sur le dernière ligne

# cette fonction créer une rivière dont toutes les cases contiennent VIDE
# et n'ont pas de courant
def Riviere(nbLig, nbCol, paire=True, colDepart=0, colArrivee=0):
    riviere = None
    if type(nbCol) is int and type(nbLig) is int and type(paire) is bool and type(colDepart) is int and type(
            colArrivee) is int:
        riviere = {"grille": None, "colDepart": colDepart, "colArrivee": colArrivee}
        initRiviere(riviere, nbLig, nbCol, paire)
    return riviere


# Cette fonction initialise une rivière avec des cases vides et sans courant
def initRiviere(r, nbLig, nbCol, paire):
    r["grille"] = GrilleHexa(nbLig, nbCol, paire)
    for l in range(getNbLigR(r)):
        for c in range(getNbColR(r)):
            setValGH(r["grille"], l, c, Case(VIDE, 'X'))


# retourne la colonne de départ de la rivière
def getColDepart(r):
    return r["colDepart"]


# retourne la colonne d'arrivée de la rivière
def getColArrivee(r):
    return r["colArrivee"]


# retourne le nombre de lignes de la rivière
def getNbLigR(r):
    return getNbLigGH(getGrille(r))


# retourne le nombre de colonnes de la rivière
def getNbColR(r):
    return getNbColGH(getGrille(r))


# indique si la rivière est paire ou non
def estPaireR(r):
    return estPaireGH(getGrille(r))


# retourne la case qui se trouve à la ligne l colonne c
def getCase(r, l, c):
    return getValGH(getGrille(r), l, c)


# met la case dans la rivière à la ligne l colonne c
def setCase(r, l, c, case):
    setValGH(getGrille(r), l, c, case)


# retourne le contenu (l'objet) qui se trouve sur la case à la ligne l colonne c
def getContenuR(r, l, c):
    case = getCase(r, l, c)
    return getContenu(case)


# met un objet (tronc, joueur, rocher) sur la case qui se trouve à la ligne l colonne c
def setContenuR(r, l, c, contenu):
    setContenu(getCase(r, l, c), contenu)


# retourne le courant de la case qui se trouve sur la case à la ligne l colonne c
def getCourantR(r, l, c):
    case = getCase(r, l, c)
    return getCourant(case)


# met le courant sur la case qui se trouve à la ligne l colonne c
def setCourantR(r, l, c, courant):
    case = getCase(r, l, c)
    setCourant(case, courant)


# recupère la grille qui représente la rivière
def getGrille(r):
    return r["grille"]


# vérifie que la position (l,c) est bien une position de la rivière
def estPosR(r, l, c):

    return estPosGH(getGrille(r), l, c)


# cette fonction enlève le contenu de la case arrivée de la rivière
def viderArrivee(riviere):
    setContenuR(riviere, (getNbLigR(riviere) - 1), riviere["colArrivee"], VIDE)


# retrouve la position (l,c) du joueur dont la représentation des repJoueur sur la grille
# si le joueur n'est pas sur la grille la fonction retourne (-1,-1)
def getPositionJoueur(r, repJoueur):

    jx=-1
    jy=-1

    x=-1
    while x<getNbLigR(r) and jx == -1:
        x += 1
        y=-1
        while y<getNbColR(r) and jy == -1:
            y += 1

            if getContenuR(r,x,y) == repJoueur:
                (jx,jy) = (x,y)

    #print('riviere.py/ getPositionJoueur', getContenuR(r, x, y), x, y, jx, jy)
    return (jx,jy)

# permet de compter combien il y a d'obstacles contigues devant la case lig,col
# en allant dans la direction direction
# n indique jusqu'à quelle distance on recherche les obstacles
# un joueur est un obstacle
def getNbObstacles(riviere, lig, col, direction, n=3):
    listeVal = getNProchainsGH(getGrille(riviere), lig, col, direction, n)
    i = 0
    nbobst=0
    while i < len(listeVal) and nbobst<3:
        if getContenu(listeVal[i]) != VIDE:
            nbobst += 1
        i+=1
    return nbobst


# retourne le nom du joueur qui se trouve sur la case d'arrivée et None si il n'y
# a pas de joueur sur cette case
def joueurArrive(r):
    winner=None
    arrivee = getCase(r, (getNbLigR(r) - 1), r["colArrivee"])

    if estJoueur(arrivee):
        winner= getContenu(arrivee)
    return winner


# cette fonction verifie que le déplacement partant de la case en position (lig,col)
# en direction de direction est bien possible
def deplacementAutorise(riviere, lig, col, direction):
    autorise = False
    vx,vy = incDirectionGH(direction)
    if getNbObstacles(riviere, lig, col, direction) <3:
        if estPosR(riviere, lig+vx, col+vy):
            autorise = True
    return autorise


# deplace un objet placé sur la case de position (lig,col) dans la direction direction
# Attention la fonction doit "pousser" dans la même direction les objets qui trouvent devant.
# On considère que lorsqu'on appelle la fonction le déplacement est possible
# La fonction retourne la représentation du joueur qui se trouve sur la case d'arrivée
# si il y en a un et None sinon
def deplacer(riviere, lig, col, direction):
    joueur = None
    vx, vy = incDirectionGH(direction)

    if getContenuR(riviere, lig+vx, col+vy) == VIDE:
        setContenuR(riviere,lig+vx, col+vy, getContenuR(riviere, lig , col ))
        setContenuR(riviere, lig, col, VIDE)

    else:
        if getContenuR(riviere, lig+vx, col+vy) != ROCHER:
            #ce qu'il y a devant se deplace si il peut
            if deplacementAutorise(riviere, lig+vx, col+vy, direction):
                deplacer(riviere, lig+vx, col+vy, direction)

    return joueur


# Cette fonction retourne la position (lig,col) de l'objet qui se trouve sur
# une case courant qui a le moins d'objet devant lui et qui se trouve le plus au
# nord ouest possible
# si aucun objet n'est à dans ce cas la fonction retourne (-1,-1)
def getMinADeplacer(r):
    pos=(-1,-1)
    for x in getNbLigR(r):
        for y in getNbColR(r):
            if getCourantR(r, x, y):
                if getContenuR(r, x, y) != VIDE:
                    if getContenuR(r, x, y) != ROCHER:
                        pos=(x,y)
    return pos




# cette fonction affiche une rivière en mode texte
# Attention! ne marche pas dans le terminal de Wing
def afficheRiviere(riviere):
    grille = getGrille(riviere)
    paire = estPaireGH(grille)
    nbLig = getNbLigGH(grille)
    nbCol = getNbColGH(grille)
    colDep = getColDepart(riviere)
    colArr = getColArrivee(riviere)
    if paire:
        print(" ", end='')
        debut = 0
    else:
        debut = 1
        print("   ", end='')
    for j in range(debut, nbCol, 2):
        if j == colDep:
            print("↓   ", end='')
        else:
            print("_   ", end='')
    print()

    c1 = c2 = ' '
    c = cprec = None
    for i in range(nbLig):
        if debut == 1:
            if i < 2:
                print(c1 + '_', end='')
            else:
                print(c1 + '\x1b[4m' + getCourantChar(getValGH(grille, i - 1, 0)) + '\x1b[0m', end='')
        prem = ''
        for j in range(debut, nbCol, 2):
            c = getValGH(grille, i, j)

            contenu=getContenu(c)

            print(prem + '/' + contenu + '\\', end='')
            if i == 0 or j == getNbColGH(grille) - 1:
                prem = "_"
            else:
                prem = '\x1b[4m' + getCourantChar(getValGH(grille, i - 1, j + 1)) + '\x1b[0m'

        if j == nbCol - 1:
            print()
        else:
            print(prem + c2)
        c1 = '\\'
        c2 = '/'
        debut = (debut + 1) % 2
    if debut == 1:
        print('\\', end='')
        debut = 0
    else:
        print('  \\', end='')
        debut = 1
    for j in range(debut, nbCol - 2, 2):
        if j == colArr:
            print(' / \\', end='')
        else:
            print('\x1b[4m' + getCourantChar(getValGH(grille, nbLig - 1, j)) + '\x1b[0m/ \\', end='')

    if j + 2 == colArr:
        print(' /')
    else:
        print('\x1b[4m' + getCourantChar(getValGH(grille, nbLig - 1, j + 2)) + '\x1b[0m/')
    print()


# Cette fonction permet d'initialiser une rivière en fonction du contenu d'un fichier texte
def lireRiviere(nomFic):
    fic = open(nomFic)
    r = None
    for ligne in fic:
        decomp = ligne.split(",")
        if decomp[0] == "entete":
            nbLig = int(decomp[1])
            nbCol = int(decomp[2])
            paire = decomp[3] == "True"
            colDepart = int(decomp[4])
            colArrivee = int(decomp[5])
            r = Riviere(nbLig, nbCol, paire, colDepart, colArrivee)
        elif decomp[0] == 'rocher':
            for i in range(1, len(decomp), 2):
                lig = int(decomp[i])
                col = int(decomp[i + 1])
                setContenuR(r, lig, col, ROCHER)
        elif decomp[0] == 'tronc':
            for i in range(1, len(decomp), 2):
                lig = int(decomp[i])
                col = int(decomp[i + 1])
                setContenuR(r, lig, col, TRONC)
        elif decomp[0] in ["N", "S", "NO", "SO", "SE", "NE"]:
            for i in range(1, len(decomp), 2):
                lig = int(decomp[i])
                col = int(decomp[i + 1])
                setCourantR(r, lig, col, decomp[0])
        else:
            for i in range(1, len(decomp), 2):
                lig = int(decomp[i])
                col = int(decomp[i + 1])
                setContenuR(r, lig, col, decomp[0])

    fic.close()
    return r


# tests--------------------------------------------------------------------------
if __name__ == '__main__':

    print('TEST des fonctions de riviere.py : ')
    r_list = [lireRiviere('riviere1.txt'), lireRiviere('riviere2.txt')]
    for river in r_list:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
        print('RIVIERE 1 : ')



        print('getNbLigR() : ', getNbLigR(river))
        print('getNbColR() : ', getNbColR(river))
        print('estPaireR() : ', estPaireR(river))
        print('getColDepart() : ', getColDepart(river))
        print('estColArrivee() : ', getColArrivee(river))
        print('getGrille() : ', getGrille(river))


        for x in range(getNbLigR(river)):
            for y in range(getNbColR(river)):
                rannum = str(random.randint(0, 9))
                rancont = str(random.randint(0, 9))
                randir = random.choice(getDirections())
                print('estPosR() : ', estPosR(river, x, y), (x,y))

                if estPosR(river,x,y):
                    print('________________________________________________________________________________ ')

                    print('COORDS : ', (x, y))
                    print('setCase() : ', setCase(river, x, y, Case(rannum, 'X')), rannum)
                    print('getCase() : ', getCase(river, x, y))
                    print('setContenuR() : ', setContenuR(river, x, y, rancont), rancont)
                    print('getContenuR() : ', getContenuR(river, x, y))
                    print('setCourantR() : ', setCourantR(river, x, y, randir), randir)
                    print('getCourantR() : ', getCourantR(river, x, y))


                    print('On met une case Tronc sur arrivee => setCase() : ', setCase(river, getNbLigR(river)-1, getColDepart(river), Case(TRONC, 'X')), getCase(river, getNbLigR(river)-1, getColDepart(river)))
                    print('viderArrivee() : ', viderArrivee(river), getCase(river, getNbLigR(river)-1, getColArrivee(river)))
                    if estPaireR(river):
                        print('On met une case Joueur => setCase() : ', setCase(river, 3, 3, Case('I', 'X')), getCase(river, 3, 3))
                    else:
                        print('On met une case Joueur => setCase() : ', setCase(river, 3, 4, Case('I', 'X')), getCase(river, 3, 4))
                    print('getPositionJoueur() : ', getPositionJoueur(river, 'I'))
                    for dir in directions:
                        print('getNbObstacles() : ', getNbObstacles(river, x, y, dir))
                        print('deplacementAutorise() : ', deplacementAutorise(river, x, y, dir), dir)
                        print('deplacer() : ', deplacer(river, x, y, dir))
                    afficheRiviere(river)

        print('On met une case Joueur a la fin  => setCase() : ', setCase(river, getNbLigR(river) - 1, getColArrivee(river), Case('I', 'X')))
        print('joueurArrive() : ', joueurArrive(river))

        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')
