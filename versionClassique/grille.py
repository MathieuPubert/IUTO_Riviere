# construit une nouvelle grille hexagonale.
# Cette grille contiendra nbLig lignes, nbCol colonnes.
# si paire est à True la grille sera paire sinon elle sera impaire
# valeur sera la valeur par défaut stockée dans chaque case de la grille
def GrilleHexa(nbLig,nbCol,paire=True,valeur=None):
    pass

# retourne le nombre de lignes de la grille
def getNbLigGH(grille):
    pass

# retourne le nombre de colonnes de la grille
def getNbColGH(grille):
    pass

# indique si la grille est paire ou impaire
def estPaireGH(grille):
    pass

# vérifie si une position est bien une position de la grille
# par exemple si la grille est paire, lig vaut 2 et col vaut 3 
# la fonction retourne False car il n'y a pas de colonne 3 dans une ligne
# de numéro paire d'une grille paire
def estPosGH(grille,lig,col):
    pass

# retourne la valeur qui se trouve dans la grille à la ligne lig, colonne col
def getValGH(grille,lig,col):
    pass

# met la valeur val dans la grille à la la ligne lig, colonne col
def setValGH(grille,lig,col,val):
    pass

# retourne un couple d'entier qui indique de combien de ligne et de combien
# de colonnes il faut se déplacer pour aller dans une direction.
# par exemple si direction vaut 'S' le retour sera (2,0) car pour se déplacer
# vers le sud, on ne change pas de colonne par contre on passe 2 lignes
# Si la direction est 'NE' le resultat sera (-1,1) car pour aller dans cette direction
# il faut remonter d'une ligne et aller une colonne vers la droite
# Cette fonction vous sera utile pour la fonction suivante.
def incDirectionGH(direction):
    pass

# permet de retourner la liste des n valeurs qui se trouvent dans le grille
# dans une direction donnée à partir de la position lig,col
# si il y a moins n celulles dans la grille dans la direction données on retourne
# toutes le cellules trouvées
def getNProchainsGH(grille,lig,col,direction,n=3):
    pass

# fonction d'initiation d'une grille avec des caractères pour faire des tests
# la grille doit être créée
def initAlphaGH(grille):
    possibles='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    grille["laGrille"]
    nbLig=getNbLigGH(grille)
    nbCol=getNbColGH(grille)
    if estPaireGH(grille):
        dec=0
    else:
        dec=1
    k=0
    for i in range(nbLig):
        for j in range(dec,nbCol,2):
            setValGH(i,j,possible[k])
            k=(k+1)%len(l)
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
