# Dictionnaire associant à chaque direction le caractère qui la représente
directions={"X":" ","N":"↑","S":"↓","NO":"↖","NE":"↗","SO":"↙","SE":"↘"}

# Constantes représentant les rochers, les troncs, le vide
ROCHER="#"
TRONC="T"
VIDE=" "

# Création d'un case
def Case(contenu,courant):
    return {"contenu":contenu,"courant":courant}

# Retourne un booléen indiquant si la case contient un rocher ou non
def estRocher(case):
    res = None
    if case["contenu"] == "#" :
        res = True
    else :
        res = False
    return res

# Retourne un booléen indiquant si la case contient un joueur ou non,
# c'est à dire autre chose que ROCHER,VIDE ou TRONC
def estJoueur(val):
    res = None
    if val["contenu"] not in ["#","T"," "] :
        res = True
    else : 
        res = False
    return res

# Retourne un booléen indiquant si la cas est vide ou non
def estVide(case):
    if case["contenu"] == " " :
        return True
    else :
        return False

# Retourne le contenu de la case
def getContenu(case):
    return case["contenu"]

# Retourne la direction du courant de la case,
# c'est-à-dire une des valeurs "X", "N", "S", "NO" etc. 
def getCourant(case):
    return case["courant"]

# Retourne la direction du courant de la case sous la forme
# d'une des flèches
def getCourantChar(case):
    return directions[case["courant"]]

# Place un courant sur la case le courant est une des valeurs
# "X", "N", "S", "NO" etc. 
def setCourant(case,courant):
    case["courant"]=courant

# Place un objet sur une case, contenu est un caractère
# parmi VIDE, TRONC, ROCHER ou le caractère représentant un joueur
def setContenu(case,contenu):
    case["contenu"]=contenu

# Permet simplement de récupérer la liste des directions possibles
# Il faut que votre fonction se réfère au dictionnaire directions
def getDirections():
    res=[]
    for elem in directions.keys() :
        res.append(elem)
    return res

