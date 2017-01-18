# Dictionnaire associant à chaque direction le caractère qui la représente
directions = {"X": " ", "N": "↑", "S": "↓", "NO": "↖", "NE": "↗", "SO": "↙", "SE": "↘"}

# Constantes représentant les rochers, les troncs, le vide
ROCHER = "#"
TRONC = "T"
VIDE = " "


# Création d'un case
class Case(object):
    def __init__(self, contenu, courant):
        self.contenu = contenu
        self.courant = courant

    # Retourne un booléen indiquant si la case contient un rocher ou non
    def estRocher(self):
        res = None
        if self.contenu == "#":
            res = True
        else:
            res = False
        return res

    # Retourne un booléen indiquant si la case contient un joueur ou non,
    # c'est à dire autre chose que ROCHER,VIDE ou TRONC
    def estJoueur(self):
        res = None
        if self.contenu not in ["#", "T", " "]:
            res = True
        else:
            res = False
        return res

    # Retourne un booléen indiquant si la cas est vide ou non
    def estVide(self):
        if self.contenu == " ":
            return True
        else:
            return False

        # Retourne le contenu de la case

    def getContenu(self):
        return self.contenu

    # Retourne la direction du courant de la case,
    # c'est-à-dire une des valeurs "X", "N", "S", "NO" etc.
    def getCourant(self):
        return self.courant

    # Retourne la direction du courant de la case sous la forme
    # d'une des flèches
    def getCourantChar(self):
        return directions[self.courant]

    # Place un courant sur la case le courant est une des valeurs
    # "X", "N", "S", "NO" etc.
    def setCourant(self, courant):
        self.courant = courant

    # Place un objet sur une case, contenu est un caractère
    # parmi VIDE, TRONC, ROCHER ou le caractère représentant un joueur
    def setContenu(self, contenu):
        self.contenu = contenu


# Permet simplement de récupérer la liste des directions possibles
# Il faut que votre fonction se réfère au dictionnaire directions
def getDirections():
    res = []
    for elem in directions.keys():
        res.append(elem)
    return res


# TESTS
if __name__ == '__main__':
    print('DIRECTIONS POSSIBLES :', getDirections())
    # Obtention des informations de cases
    l_case = [Case("#", "X"), Case("T", "N"), Case(" ", "NO"), Case("J1", "S"), Case("J2", "X")]
    for case in l_case:
        print('--------------------------------------------------------------------------------')
        print('VERIFICATION CONTENU :', 'Joueur' * case.estJoueur(), 'Rocher' * case.estRocher(),
              'Vide' * case.estVide())
        print('CONTENU : ', case.getContenu())
        print('COURANT : ', case.getCourant(), case.getCourantChar())
        case.setCourant('N')
        print('COURANT CHANGE POUR NORD: ', case.getCourant(), case.getCourantChar())
        case.setContenu(VIDE)
        print('CONTENU CHANGE POUR VIDE: ', case.getContenu())
