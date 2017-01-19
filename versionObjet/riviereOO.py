import random
from grilleOO import *
from caseOO import *

# La rivière est une grille hexagonale qui stokera des cases (telles que définies dans
# le fichier case.py. En plus elle contient une colonne de départ sur la 1ere ligne
# et une colonne d'arrivée sur le dernière ligne

# cette fonction créer une rivière dont toutes les cases contiennent VIDE
# et n'ont pas de courant

class Riviere(object):
    def __init__(self,nbLig,nbCol,paire, colDepart=0,colArrivee=0):
        self.grille = {}
        self.nbLig = nbLig
        self.nbCol = nbCol
        self.paire = paire
        self.colDepart = colDepart
        self.colArrivee = colArrivee
        self.initRiviere(nbLig, nbCol, paire)

        if type(self.nbCol) is int and type(self.nbLig) is int and type(self.paire) is bool and type(self.colDepart) is int and type(self.colArrivee) is int:
            self.initRiviere(nbLig, nbCol, paire)

    # Cette fonction initialise une rivière avec des cases vides et sans courant
    def initRiviere(self,nbLig,nbCol,paire):
        case = Case(VIDE,'X')
        self.grille = GrilleHexa(nbLig,nbCol,paire,valeur=case)

    # retourne la colonne de départ de la rivière
    def getColDepart(self):
        return self.colDepart

    # retourne la colonne d'arrivée de la rivière
    def getColArrivee(self):
        return self.colArrivee

    # retourne le nombre de lignes de la rivière
    def getNbLigR(self):
        return self.nbLig

    # retourne le nombre de colonnes de la rivière
    def getNbColR(self):
        return self.nbCol

    # indique si la rivière est paire ou non
    def estPaireR(self):
        return self.paire

    # retourne la case qui se trouve à la ligne l colonne c
    def getCase(self,l,c):
        return self.grille.getValGH(l,c)

    # met la case dans la rivière à la ligne l colonne c
    def setCase(self,l,c,case):
        self.grille.setValGH(l,c,case)

    # retourne le contenu (l'objet) qui se trouve sur la case à la ligne l colonne c
    def getContenuR(self,l,c):
        return self.getCase(l,c).getContenu()

    # met un objet (tronc, joueur, rocher) sur la case qui se trouve à la ligne l colonne c
    def setContenuR(self,l,c,contenu):
        self.getCase(l,c).setContenu(contenu)

    # retourne le courant de la case qui se trouve sur la case à la ligne l colonne c
    def getCourantR(self,l,c):
        return self.getCase(l,c).getCourant()

    # met le courant sur la case qui se trouve à la ligne l colonne c
    def setCourantR(self,l,c,courant):
        self.getCase(l,c).setCourant(courant)

    # recupère la grille qui représente la rivière
    def getGrille(self):
        return self.grille

    # vérifie que la position (l,c) est bien une position de la rivière
    def estPosR(self,l,c):
        return self.estPosGH(l,c)

    # cette fonction enlève le contenu de la case arrivée de la rivière
    def viderArrivee(self):
        self.setContenuR((self.nbLig-1),self.colArrivee,Case(VIDE,'X'))

    # retrouve la position (l,c) du joueur dont la représentation des repJoueur sur la grille
    # si le joueur n'est pas sur la grille la fonction retourne (-1,-1)
    def getPositionJoueur(self,repJoueur):
        jx=-1
        jy=-1

        x=-1
        while x<self.getNbLigR() and jx == -1:
            x += 1
            y=-1
            while y<self.getNbColR() and jy == -1:
                y += 1

                if self.getContenuR(x,y) == repJoueur:
                    (jx,jy) = (x,y)

        #print('riviere.py/ getPositionJoueur', getContenuR(r, x, y), x, y, jx, jy)
        return (jx,jy)

    # permet de compter combien il y a d'obstacles contigues devant la case lig,col
    # en allant dans la direction direction
    # n indique jusqu'à quelle distance on recherche les obstacles
    # un joueur est un obstacle
    def getNbObstacles(self,lig,col,direction,n=3):
        listeVal = self.grille.getNProchainsGH(lig, col, direction, n)
        i = 0
        nbobst=0
        while i < len(listeVal) and nbobst<3:
            if listeVal[i].getContenu() != VIDE:
                nbobst += 1
            i+=1
        return nbobst


    # retourne le nom du joueur qui se trouve sur la case d'arrivée et None si il n'y
    # a pas de joueur sur cette case
    def joueurArrive(self):
        winner=None
        arrivee = self.getCase((self.getNbLigR() - 1), self.colArrivee)

        if estJoueur(arrivee):
            winner= arrivee.getContenu()
        return winner

    # cette fonction verifie que le déplacement partant de la case en position (lig,col)
    # en direction de direction est bien possible
    def deplacementAutorise(self,lig,col,direction):
        autorise = False
        vx,vy = self.incDirectionGH(direction)
        if self.getNbObstacles(lig, col, direction) <3:
            if self.estPosR(lig+vx, col+vy):
                autorise = True
        return autorise

    # deplace un objet placé sur la case de position (lig,col) dans la direction direction
    # Attention la fonction doit "pousser" dans la même direction les objets qui trouvent devant.
    # On considère que lorsqu'on appelle la fonction le déplacement est possible
    # La fonction retourne la représentation du joueur qui se trouve sur la case d'arrivée
    # si il y en a un et None sinon
    def deplacer(self,lig,col,direction):
        joueur = None
        vx, vy = self.incDirectionGH(direction)

        if self.getContenuR(lig+vx, col+vy) == VIDE:
            self.setContenuR(lig+vx, col+vy, self.getContenuR(lig , col ))
            self.setContenuR(lig, col, VIDE)

        else:
            if self.getContenuR(lig+vx, col+vy) != ROCHER:
                #ce qu'il y a devant se deplace si il peut
                if self.deplacementAutorise(lig+vx, col+vy, direction):
                    self.deplacer(lig+vx, col+vy, direction)

        return joueur

    # Cette fonction retourne la position (lig,col) de l'objet qui se trouve sur
    # une case courant qui a le moins d'objet devant lui et qui se trouve le plus au
    # nord ouest possible
    # si aucun objet n'est à dans ce cas la fonction retourne (-1,-1)
    # def getMinADeplacer(r):
    #     pass


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
                r.setContenuR(lig, col, ROCHER)
        elif decomp[0] == 'tronc':
            for i in range(1, len(decomp), 2):
                lig = int(decomp[i])
                col = int(decomp[i + 1])
                r.setContenuR(lig, col, TRONC)
        elif decomp[0] in ["N", "S", "NO", "SO", "SE", "NE"]:
            for i in range(1, len(decomp), 2):
                lig = int(decomp[i])
                col = int(decomp[i + 1])
                r.setCourantR(lig, col, decomp[0])
        else:
            for i in range(1, len(decomp), 2):
                lig = int(decomp[i])
                col = int(decomp[i + 1])
                r.setContenuR(lig, col, decomp[0])

    fic.close()
    return r



# tests--------------------------------------------------------------------------
if __name__ == '__main__':

    print('TEST des fonctions de riviere.py : ')
    r_list = [lireRiviere('riviere1.txt'), lireRiviere('riviere2.txt')]
    for river in r_list:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
        print('RIVIERE 1 : ')



        print('getNbLigR() : ', river.getNbLigR())
        print('getNbColR() : ', river.getNbColR())
        print('estPaireR() : ', river.estPaireR())
        print('getColDepart() : ', river.getColDepart())
        print('estColArrivee() : ', river.getColArrivee())
        print('getGrille() : ', river.getGrille())


        for x in range(river.getNbLigR()):
            for y in range(river.getNbColR()):
                rannum = str(random.randint(0, 9))
                rancont = str(random.randint(0, 9))
                randir = random.choice(self.getDirections())
                print('estPosR() : ', river.estPosR(x, y), (x,y))

                if estPosR(river,x,y):
                    print('________________________________________________________________________________ ')

                    print('COORDS : ', (x, y))
                    print('setCase() : ', river.setCase(x, y, Case(rannum, 'X')), rannum)
                    print('getCase() : ', river.getCase(x, y))
                    print('setContenuR() : ', river.setContenuR(x, y, rancont), rancont)
                    print('getContenuR() : ', river.getContenuR(x, y))
                    print('setCourantR() : ', river.setCourantR(x, y, randir), randir)
                    print('getCourantR() : ', river.getCourantR(x, y))


                    print('On met une case Tronc sur arrivee => setCase() : ', river.setCase(river.getNbLigR()-1, river.getColDepart(), Case(TRONC, 'X')), river.getCase(river.getNbLigR()-1, river.getColDepart()))
                    print('viderArrivee() : ', river.viderArrivee(), river.getCase(river.getNbLigR()-1, river.getColArrivee()))
                    if river.estPaireR():
                        print('On met une case Joueur => setCase() : ', river.setCase(3, 3, Case('I', 'X')), river.getCase(3, 3))
                    else:
                        print('On met une case Joueur => setCase() : ', river.setCase(3, 4, Case('I', 'X')), river.getCase(3, 4))
                    print('getPositionJoueur() : ', river.getPositionJoueur('I'))
                    for dir in directions:
                        print('getNbObstacles() : ', river.getNbObstacles(x, y, dir))
                        print('deplacementAutorise() : ', river.deplacementAutorise(x, y, dir), dir)
                        print('deplacer() : ', river.deplacer(x, y, dir))
                    river.afficheRiviere()

        print('On met une case Joueur a la fin  => setCase() : ', river.setCase(river.getNbLigR() - 1, river.getColArrivee(), Case('I', 'X')))
        print('joueurArrive() : ', river.joueurArrive())

        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')
