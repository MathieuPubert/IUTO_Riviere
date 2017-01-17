# coding=utf-8
# construit une nouvelle grille hexagonale.
# Cette grille contiendra nbLig lignes, nbCol colonnes.
# si paire est à True la grille sera paire sinon elle sera impaire
# valeur sera la valeur par défaut stockée dans chaque case de la grille
def GrilleHexa(nbLig,nbCol,paire=True,valeur=None):
    grille={}
    grille["nombre de lignes"]=nbLig
    grille["nombre de colonnes"]=nbCol
    grille["paire"]=paire
    grille["valeurs"]=[]

    i=0
    for i in range(nbLig):
        valeurNone=[valeur,None]*(nbCol//2)
        noneValeur=[None,valeur]*(nbCol//2)
        if nbCol%2 == 0 :                                         # si le nb de colonnes est paire
            if i%2 == 0  :                                              #si l'indice de la ligne est paire
                grille["valeurs"].append(valeurNone)
            else:                                                       #si l'indice de la ligne est impair
                grille["valeurs"].append(noneValeur)

        elif nbCol%2!=0:
            noneValeur.append(None)
            valeurNone.append(valeur)                                        #si le nb de colonnes est impaire
            if not paire:                                           #si la grille est impaire
                if i%2 == 0:
                    grille["valeurs"].append(noneValeur)
                else:
                    grille["valeurs"].append(valeurNone)
            else:
                if paire:
                    if i%2 == 0:  #si la ligne est paire
                        grille["valeurs"].append(valeurNone)
                    else:
                        grille["valeurs"].append(noneValeur)
    return grille

# retourne le nombre de lignes de la grille
def getNbLigGH(grille):
    return grille["nombre de lignes"]

# retourne le nombre de colonnes de la grille
def getNbColGH(grille):
    return grille["nombre de colonnes"]

# indique si la grille est paire ou impaire
def estPaireGH(grille):
    return grille["paire"]

# vérifie si une position est bien une position de la grille
# par exemple si la grille est paire, lig vaut 2 et col vaut 3
# la fonction retourne False car il n'y a pas de colonne 3 dans une ligne
# de numéro paire d'une grille paire
def estPosGH(grille,lig,col):
    estPos=False
    if grille["valeurs"][lig][col] != None:
        estPos=True
    return estPos
# retourne la valeur qui se trouve dans la grille à la ligne lig, colonne col
def getValGH(grille,lig,col):
    if estPosGH(grille,lig,col):
        return grille["valeurs"][lig][col]

# met la valeur val dans la grille à la la ligne lig, colonne col
def setValGH(grille,lig,col,val):
    if estPosGH(grille,lig,col):
        grille["valeurs"][lig][col]=val

# retourne un couple d'entier qui indique de combien de ligne et de combien
# de colonnes il faut se déplacer pour aller dans une direction.
# par exemple si direction vaut 'S' le retour sera (2,0) car pour se déplacer
# vers le sud, on ne change pas de colonne par contre on passe 2 lignes
# Si la direction est 'NE' le resultat sera (-1,1) car pour aller dans cette direction
# il faut remonter d'une ligne et aller une colonne vers la droite
# Cette fonction vous sera utile pour la fonction suivante.
def incDirectionGH(direction):
    if direction=='N':
        return (-2,0)
    elif direction=='S':
        return (2,0)
    elif direction=='E':
        return (0,2)
    elif direction=='O':
        return (0,-2)
    elif direction=='NE':
        return (-1,1)
    elif direction=='NO':
        return (-1,-1)
    elif direction=='SE':
        return (1,1)
    elif direction=='SO':
        return (1,-1)

# permet de retourner la liste des n valeurs qui se trouvent dans la grille
# dans une direction donnée à partir de la position lig,col
# si il y a moins n celulles dans la grille dans la direction données on retourne
# toutes le cellules trouvées
def getNProchainsGH(grille,lig,col,direction,n=3):
    liste_NProchains=[]

    direction=incDirectionGH(direction)
    for i in range(n):
        valeur=grille['valeurs'][lig+(direction[0]*i)][col+(direction[1]*i)]
        print(valeur)
        liste_NProchains.append(valeur)
    return liste_NProchains



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
            setValGH(grille,i,j,possibles[k])
            k=(k+1)%len(possibles)
        dec=(dec+1)%2

# affichage en mode texte d'une grille hexagonale
def afficheGH(grille):
    nbLig=getNbLigGH(grille)
    nbCol=getNbColGH(grille)
    if estPaireGH(grille):
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


#tests-------------------------------------------------
# print(GrilleHexa(4,5,paire=False,valeur=2))
# print('GrilleHexa(4,5,paire=True,valeur=2)',GrilleHexa(4,5,paire=True,valeur=2))
# print(GrilleHexa(6,10,paire=False,valeur=2))
grilleHexa=(GrilleHexa(4,5,paire=True,valeur=2))

initAlphaGH(grilleHexa)

setValGH(grilleHexa,0,1,'D')
setValGH(grilleHexa,1,0,'B')
print(grilleHexa)
afficheGH(grilleHexa)

# print('estPosGH(grilleHexa,3,3)--True :', estPosGH(grilleHexa,3,3))
# print('estPosGH(grilleHexa,3,2)--False :', estPosGH(grilleHexa,3,2))
# print('le nb de lignes est :', getNbLigGH(grilleHexa))
# print('le nb de colonnes est :', getNbColGH(grilleHexa))
# setValGH(grilleHexa,3,3,7)
# print(grilleHexa)
# print('getValGH(grilleHexa,3,3) :', getValGH(grilleHexa,3,3))
# print('direction : ', incDirectionGH('SE'))
print(getNProchainsGH(grilleHexa,0,0,'SE',n=3))
