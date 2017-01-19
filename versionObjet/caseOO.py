# Dictionnaire associant à chaque direction le caractère qui la représente
directions = {"X": " ", "N": "↑", "S": "↓", "NO": "↖", "NE": "↗", "SO": "↙", "SE": "↘"}

# Constantes représentant les rochers, les troncs, le vide
ROCHER = "#"
TRONC = "T"
VIDE = " "


# Création d'un case
class Case(object):
    def __init__(self,contenu,courant):
        self.contenu=contenu
        self.courant=courant


    # Retourne un booléen indiquant si la case contient un rocher ou non
    def estRocher(self):
        res = False
        if self.getContenu() == ROCHER:
            res = True
        return res


    def estTronc(self):
        res = False
        if self.getContenu() == TRONC:
            res = True
        return res

    # Retourne un booléen indiquant si la case contient un joueur ou non,
    # c'est à dire autre chose que ROCHER,VIDE ou TRONC
    def estJoueur(self):
        res = False
        if not self.estRocher() and not self.estVide() and not self.estTronc():
            res = True
        return res


    # Retourne un booléen indiquant si la cas est vide ou non
    def estVide(self):
        res = False
        if self.getContenu() == VIDE:
            res = True
        return res



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
        courchar = directions[self.getCourant()]
        return courchar


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
    def getDirections(self):
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
            c = Case(contenu, courant)
            print('Case() : ', c)

            print('estRocher() : ', c.estRocher())

            print('estTronc() : ', c.estTronc())

            print('estVide() : ', c.estVide())

            print('estJoueur() : ', c.estJoueur())

            print('getContenu() : ', c.getContenu())

            print('getCourant() : ', c.getCourant())

            print('getCourantChar() : ', c.getCourantChar())

            print('setContenu() : ', c.setContenu('$'))

            print('setCourant() : ', c.setCourant('N'))

            print('getDirections() : ', c.getDirections())

            print('RE - getContenu() : ', c.getContenu())
            print('RE - getCourant() : ', c.getCourant())
            print('RE - getCourantChar() : ', c.getCourantChar())
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')

    print('Mauvaises Valeurs: ')
    for contenu in [1, True, [], ()]:
        for courant in 'AZRTYUIP':
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
            c = Case(contenu, courant)
            print('Case() : ', c)

            print('estRocher() : ', c.estRocher())

            print('estTronc() : ', c.estTronc())

            print('estVide() : ', c.estVide())

            print('estJoueur() : ', c.estJoueur())

            print('getContenu() : ', c.getContenu())

            print('getCourant() : ', c.getCourant())

            print('getCourantChar() : ', c.getCourantChar())

            print('setContenu() : ', c.setContenu('$'))

            print('setCourant() : ', c.setCourant('X'))

            print('getDirections() : ', c.getDirections())

            print('RE - getContenu() : ', c.getContenu())
            print('RE - getCourant() : ', c.getCourant())
            print('RE - getCourantChar() : ', c.getCourantChar())
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')
