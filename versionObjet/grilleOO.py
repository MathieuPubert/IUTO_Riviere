# coding=utf-8
# construit une nouvelle grille hexagonale.
# Cette grille contiendra nbLig lignes, nbCol colonnes.
# si paire est à True la grille sera paire sinon elle sera impaire
# valeur sera la valeur par défaut stockée dans chaque case de la grille
class GrilleHexa(object):
    def __init__(self,nbLig,nbCol,paire=True,valeur=''):
        self.nbLig = nbLig
        self.nbCol = nbCol
        self.paire = paire
        self.grille=[]

        i=0
        for i in range(nbLig):
            valeurNone=[valeur,None]*(nbCol//2)
            noneValeur=[None,valeur]*(nbCol//2)
            if nbCol%2 == 0 :                                         # si le nb de colonnes est paire
                if i%2 == 0  :                                              #si l'indice de la ligne est paire
                    self.grille.append(valeurNone)
                else:                                                       #si l'indice de la ligne est impair
                    self.grille.append(noneValeur)

            elif nbCol%2!=0:
                noneValeur.append(None)
                valeurNone.append(valeur)                                        #si le nb de colonnes est impaire
                if not paire:                                           #si la grille est impaire
                    if i%2 == 0:
                        self.grille.append(noneValeur)
                    else:
                        self.grille.append(valeurNone)
                else:
                    if paire:
                        if i%2 == 0:  #si la ligne est paire
                            self.grille.append(valeurNone)
                        else:
                            self.grille.append(noneValeur)

    # retourne le nombre de lignes de la grille
    def getNbLigGH(self):
        return self.nbLig

    # retourne le nombre de colonnes de la grille
    def getNbColGH(self):
        return self.nbCol

    # indique si la grille est paire ou impaire
    def estPaireGH(self):
        return self.paire

    # vérifie si une position est bien une position de la grille
    # par exemple si la grille est paire, lig vaut 2 et col vaut 3
    # la fonction retourne False car il n'y a pas de colonne 3 dans une ligne
    # de numéro paire d'une grille paire
    def estPosGH(self,lig,col):
        estPos=False
        if self.grille[lig][col] != None:
            estPos=True
        return estPos
    # retourne la valeur qui se trouve dans la grille à la ligne lig, colonne col
    def getValGH(self,lig,col):
        if self.estPosGH(lig,col):

            return self.grille[lig][col]

    # met la valeur val dans la grille à la la ligne lig, colonne col
    def setValGH(self,lig,col,val):
        if self.estPosGH(lig,col):
            self.grille[lig][col]=val

    # retourne un couple d'entier qui indique de combien de ligne et de combien
    # de colonnes il faut se déplacer pour aller dans une direction.
    # par exemple si direction vaut 'S' le retour sera (2,0) car pour se déplacer
    # vers le sud, on ne change pas de colonne par contre on passe 2 lignes
    # Si la direction est 'NE' le resultat sera (-1,1) car pour aller dans cette direction
    # il faut remonter d'une ligne et aller une colonne vers la droite
    # Cette fonction vous sera utile pour la fonction suivante.
    def incDirectionGH(self,direction):
        orientation={   'N': (-2,0),
                        'S': (2,0),
                        'E': (0,2),
                        'O': (0,-2),
                        'NE': (-1,1),
                        'NO': (-1,-1),
                        'SE': (1,1),
                        'SO': (1,-1) }
        return orientation[direction]

    # permet de retourner la liste des n valeurs qui se trouvent dans la grille
    # dans une direction donnée à partir de la position lig,col
    # si il y a moins n celulles dans la grille dans la direction données on retourne
    # toutes le cellules trouvées
    def getNProchainsGH(self,lig,col,direction,n=3):
        liste_NProchains=[]

        direction=self.incDirectionGH(direction)
        for i in range(n):
            valeur=self.grille[lig+(direction[0]*i)][col+(direction[1]*i)]
            liste_NProchains.append(valeur)
        return liste_NProchains


    # fonction d'initiation d'une grille avec des caractères pour faire des tests
    # la grille doit être créée
    def initAlphaGH(self):
        possibles='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        nbLig=self.getNbLigGH()
        nbCol=self.getNbColGH()
        if self.estPaireGH():
            dec=0
        else:
            dec=1
        k=0
        for i in range(nbLig):
            for j in range(dec,nbCol,2):
                self.setValGH(i,j,possibles[k])
                k=(k+1)%len(possibles)
            dec=(dec+1)%2

    # affichage en mode texte d'une grille hexagonale
    def afficheGH(self):
        nbLig=self.getNbLigGH()
        nbCol=self.getNbColGH()
        if self.estPaireGH():
            print(" ",end='')
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
                print(prem+'/'+str(self.getValGH(i,j))+'\\',end='')
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
        for j in range(debut,self.getNbColGH()-2,2):
            print('_/ \\',end='')
        print('_/')


#tests-------------------------------------------------
if __name__ == '__main__':

    gh=(GrilleHexa(4,5,2))

    gh.initAlphaGH()

    gh.setValGH(0,1,'D')
    gh.setValGH(1,0,'B')
    print(gh)
    gh.afficheGH()

    print('estPosGH(grilleHexa,3,3)--True :', gh.estPosGH(3,3))
    print('estPosGH(grilleHexa,3,2)--False :', gh.estPosGH(3,2))
    print('le nb de lignes est :', gh.getNbLigGH())
    print('le nb de colonnes est :', gh.getNbColGH())
    gh.setValGH(3,3,7)
    print(gh)
    print('getValGH(grilleHexa,3,3) :', gh.getValGH(3,3))
    print('direction : ', gh.incDirectionGH('SE'))
    print(gh.getNProchainsGH(0,0,'SE',n=3))
