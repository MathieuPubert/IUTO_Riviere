# Dictionnaire associant à chaque direction le caractère qui la représente
directions = {"X": " ", "N": "↑", "S": "↓", "NO": "↖", "NE": "↗", "SO": "↙", "SE": "↘"}

# Constantes représentant les rochers, les troncs, le vide
ROCHER = "#"
TRONC = "T"
VIDE = " "


# Création d'un case
def Case(contenu, courant):
    case = None
    if courant in directions:
        case = {"contenu": contenu, "courant": courant}
    return case


# Retourne un booléen indiquant si la case contient un rocher ou non
def estRocher(case):
    res = False
    if getContenu(case) == ROCHER:
        res = True
    return res


def estTronc(case):
    res = False
    if getContenu(case) == TRONC:
        res = True
    return res

# Retourne un booléen indiquant si la case contient un joueur ou non,
# c'est à dire autre chose que ROCHER,VIDE ou TRONC
def estJoueur(case):
    res = False
    if not estRocher(case) and not estVide(case) and not estTronc(case) and case is not None:
        res = True
    return res


# Retourne un booléen indiquant si la cas est vide ou non
def estVide(case):
    res = False
    if getContenu(case) == VIDE:
        res = True
    return res



# Retourne le contenu de la case
def getContenu(case):
    contenu = None
    if case is not None:
        contenu = case["contenu"]
    return contenu


# Retourne la direction du courant de la case,
# c'est-à-dire une des valeurs "X", "N", "S", "NO" etc. 
def getCourant(case):
    courant = None
    if case is not None:
        courant = case["courant"]
    return courant


# Retourne la direction du courant de la case sous la forme
# d'une des flèches
def getCourantChar(case):
    courchar = None
    if case is not None:
        courchar = directions[getCourant(case)]
    return courchar


# Place un courant sur la case le courant est une des valeurs
# "X", "N", "S", "NO" etc. 
def setCourant(case, courant):
    if case is not None:
        case["courant"] = courant


# Place un objet sur une case, contenu est un caractère
# parmi VIDE, TRONC, ROCHER ou le caractère représentant un joueur
def setContenu(case, contenu):
    if case is not None:
        case["contenu"] = contenu


# Permet simplement de récupérer la liste des directions possibles
# Il faut que votre fonction se réfère au dictionnaire directions
def getDirections():
    res = []
    for elem in directions.keys():
        res.append(elem)
    return res


# TESTS
if __name__ == '__main__':
    print('TEST des fonctions de case.py : ')

    print('Bonnes Valeurs: ')
    for contenu in 'AZERTYUIOPQSDFGHJKLMLWXCVBN' + ROCHER + VIDE + TRONC:
        for courant in directions:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
            case = Case(contenu, courant)
            print('Case() : ', case)

            print('estRocher() : ', estRocher(case))

            print('estTronc() : ', estTronc(case))

            print('estVide() : ', estVide(case))

            print('estJoueur() : ', estJoueur(case))

            print('getContenu() : ', getContenu(case))

            print('getCourant() : ', getCourant(case))

            print('getCourantChar() : ', getCourantChar(case))

            print('setContenu() : ', setContenu(case, '$'))

            print('setCourant() : ', setCourant(case, 'X'))

            print('getDirections() : ', getDirections())

            print('RE - getContenu() : ', getContenu(case))
            print('RE - getCourant() : ', getCourant(case))
            print('RE - getCourantChar() : ', getCourantChar(case))
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')

    print('Mauvaises Valeurs: ')
    for contenu in [1, True, [], ()]:
        for courant in 'AZRTYUIP':
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
            case = Case(contenu, courant)
            print('Case() : ', case)

            print('estRocher() : ', estRocher(case))

            print('estTronc() : ', estTronc(case))

            print('estVide() : ', estVide(case))

            print('estJoueur() : ', estJoueur(case))

            print('getContenu() : ', getContenu(case))

            print('getCourant() : ', getCourant(case))

            print('getCourantChar() : ', getCourantChar(case))

            print('setContenu() : ', setContenu(case, '$'))

            print('setCourant() : ', setCourant(case, 'X'))

            print('getDirections() : ', getDirections())

            print('RE - getContenu() : ', getContenu(case))
            print('RE - getCourant() : ', getCourant(case))
            print('RE - getCourantChar() : ', getCourantChar(case))
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')
