#dictionnaire associant à chaque direction le caractère qui la représente
directions={"X":" ","N":"↑","S":"↓","NO":"↖","NE":"↗","SO":"↙","SE":"↘"}

#constantes représentant les rochers, les troncs, le vide
ROCHER="#"
TRONC="T"
VIDE=" "

# création d'un case
def Case(contenu,courant):
    pass
# retourne un booléen indiquant si la case contient un rocher ou non
def estRocher(case):
    pass
# retourne un booléen indiquant si la case contient un joueur ou non
# c'est à dire autre chose que ROCHER,VIDE ou TRONC
def estJoueur(val):
    pass

# retourne un booléen indiquant si la cas est vide ou non
def estVide(case):
    pass

# retourne le contenu de la case
def getContenu(case):
    pass

# retourne la direction du courant de la case
# c'est-à-dire une des valeurs "X", "N", "S", "NO" etc. 
def getCourant(case):
    pass


# retourne la direction du courant de la case sous la forme
# d'une des flèches
def getCourantChar(case):
    pass

# place un courant sur la case le courant est une des valeurs
# "X", "N", "S", "NO" etc. 
def setCourant(case,courant):
    pass

# place un objet sur une case, contenu est un caractère
# parmiVIDE, TRONC, ROCHER ou le caractère représentant un joueur
def setContenu(case,contenu):
    pass

# permet simplement de récupérer la liste des directions possibles
# il faut que votre fonction se réfère au dictionnaire directions
def getDirections():
    pass

