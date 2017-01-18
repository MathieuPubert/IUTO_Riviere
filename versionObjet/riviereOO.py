import random
from grille import *
from case import *

# La rivière est une grille hexagonale qui stokera des cases (telles que définies dans
# le fichier case.py. En plus elle contient une colonne de départ sur la 1ere ligne
# et une colonne d'arrivée sur le dernière ligne

# cette fonction créer une rivière dont toutes les cases contiennent VIDE
# et n'ont pas de courant
class Riviere(object):
    def __init__(self,nbLig,nbCol,paire, colDepart=0,colArrivee=0):
        self.grille = None
        self.nbLig = nbLig
        self.nbCol = nbCol
        self.paire = paire
        self.colDepart = colDepart
        self.colArrivee = colArrivee
        self.initRiviere(nbLig, nbCol, paire)

    # Cette fonction initialise une rivière avec des cases vides et sans courant
    def initRiviere(self,nbLig,nbCol,paire):
        case = Case(VIDE,'X')
        self.grille = GrilleHexa(nbLig,nbCol,paire,valeur=case)
        print(self.grille)


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
        return self.grille["valeurs"][l][c]

    # met la case dans la rivière à la ligne l colonne c
    def setCase(self,l,c,case):
        self.grille["valeurs"][l][c] = case

    # retourne le contenu (l'objet) qui se trouve sur la case à la ligne l colonne c
    def getContenuR(self,l,c):
        return self.getCase(l,c)["contenu"]

    # met un objet (tronc, joueur, rocher) sur la case qui se trouve à la ligne l colonne c
    def setContenuR(self,l,c,contenu):
        self.getCase(l,c)["contenu"] = contenu

    # retourne le courant de la case qui se trouve sur la case à la ligne l colonne c
    def getCourantR(self,l,c):
        return self.getCase(l,c)["courant"]

    # met le courant sur la case qui se trouve à la ligne l colonne c
    def setCourantR(self,l,c,courant):
        self.getCase(l,c)["courant"] = courant

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
    def getPositionJoueur(r,repJoueur):
        for l in range(self.nbLig):
            for c in range(self.nbCol):
                if self.getContenuR(l,c) == repJoueur:
                    return (l,c)
                else:
                    return (-1,-1)

    # permet de compter combien il y a d'obstacles contigues devant la case lig,col
    # en allant dans la direction direction
    # n indique jusqu'à quelle distance on recherche les obstacles
    # un joueur est un obstacle
    def getNbObstacles(self,lig,col,direction,n=3):
        listeVal=self.grille.getNProchainsGH(lig,col,direction,n)
        i=0
        while i<n and listeVal[i] == " ":
            i+=1
        return i


    # retourne le nom du joueur qui se trouve sur la case d'arrivée et None si il n'y
    # a pas de joueur sur cette case
    def joueurArrive(self):
        arrivee = self.getContenuR((self.getNbLigR()-1),r["colArrivee"])
        if arrivee.estJoueur():
            return arrivee["contenu"]
        else:
            return None

    # cette fonction verifie que le déplacement partant de la case en position (lig,col)
    # en direction de direction est bien possible
    def deplacementAutorise(self,lig,col,direction):
        autorise=False
        if self.getNbObstacles(lig,col,direction,n) < n:
            if self.estPosR(lig,col):
                autorise=True
        return autorise

    # deplace un objet placé sur la case de position (lig,col) dans la direction direction
    # Attention la fonction doit "pousser" dans la même direction les objets qui trouvent devant.
    # On considère que lorsqu'on appelle la fonction le déplacement est possible
    # La fonction retourne la représentation du joueur qui se trouve sur la case d'arrivée
    # si il y en a un et None sinon
    def deplacer(self,lig,col,direction):
        joueur = None
        depx, depy = self.incDirectionGH(direction)

        if self.deplacementAutorise(lig, col, direction):
            listecontcase = self.getGrille().getNProchainsGH(lig, col, direction)

            for i in range(len(listecontcase) - 1, -1, -1):
                cx, cy = listecontcase[i]
                vx, vy = -depx, -depy
                self.setContenuR(cx, cy, getContenuR(riviere, cx + vx, cy + vy))

        if self.getContenuR(lig + depx, col + depy).estJoueur():
            joueur = self.getContenuR(lig + depx, col + depy)

        return joueur

    # Cette fonction retourne la position (lig,col) de l'objet qui se trouve sur
    # une case courant qui a le moins d'objet devant lui et qui se trouve le plus au
    # nord ouest possible
    # si aucun objet n'est à dans ce cas la fonction retourne (-1,-1)
    # def getMinADeplacer(r):
    #     pass



    # cette fonction affiche une rivière en mode texte
    # Attention! ne marche pas dans le terminal de Wing
    def afficheRiviere(self):
        grille=self.getGrille()
        paire=grille.estPaireGH()
        nbLig=grille.getNbLigGH()
        nbCol=grille.getNbColGH()
        colDep=self.getColDepart()
        colArr=self.getColArrivee()
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
                    print(c1+'\x1b[4m'+grille.getValGH(i-1,0).getCourantChar()+'\x1b[0m',end='')
            prem=''
            for j in range(debut,nbCol,2):
                c=grille.getValGH(i,j)
                print(prem+'/'+c.getContenu()+'\\',end='')
                if i==0 or j==grille.getNbColGH()-1:
                    prem="_"
                else:
                    prem='\x1b[4m'+grille.getValGH(i-1,j+1).getCourantChar()+'\x1b[0m'


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
                print('\x1b[4m'+grille.getValGH(nbLig-1,j).getCourantChar()+'\x1b[0m/ \\',end='')

        if j+2==colArr:
            print(' /')
        else:
            print('\x1b[4m'+grille.getValGH(nbLig-1,j+2).getCourantChar()+'\x1b[0m/')
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
                    self.setContenuR(lig,col,ROCHER)
            elif decomp[0]=='tronc':
                for i in range(1,len(decomp),2):
                    lig=int(decomp[i])
                    col=int(decomp[i+1])
                    self.setContenuR(lig,col,TRONC)
            elif decomp[0] in ["N","S","NO","SO","SE","NE"]:
                for i in range(1,len(decomp),2):
                    lig=int(decomp[i])
                    col=int(decomp[i+1])
                    self.setCourantR(lig,col,decomp[0])
            else:
                for i in range(1,len(decomp),2):
                    lig=int(decomp[i])
                    col=int(decomp[i+1])
                    self.setContenuR(lig,col,decomp[0])

        fic.close()
        return r

# tests--------------------------------------------------------------------------
if __name__ == '__main__':
     r=(Riviere(6,6,0,0))
     r.afficheRiviere
     print(r.getNbLigR())
     print(r.getCase(0,0))
     r.setCase(0,0,Case(TRONC,"N"))

     r.setContenuR(0,0,ROCHER)

     r.setCourantR(0,0,"N")
     r.viderArrivee()
     r.setContenuR(2,4,'I')
     print(r)
     print(getNbObstacles(r,0,0,"0",n=3))
     print(r.joueurArrive())
