#dictionnaire associant à chaque direction le caractère qui la représente
directions={"X":" ","N":"↑","S":"↓","NO":"↖","NE":"↗","SO":"↙","SE":"↘"}

#constantes représentant les rochers, les troncs, le vide
ROCHER="#"
TRONC="T"
VIDE=" "


def Case(contenu,courant):
    """
    Case de la grille.
    :param contenu: string. L'une des constantes ROCHER, TRONC, VIDE. Ou Joueur()
    :param courant: string. L'une des clés du dictionnaire directions
    :return: tuple. (contenu, courant)
    """
    case = None
    if courant in directions:
        case = (contenu, courant)
    return case


def estRocher(case):
    """
    Indique si la case contient un rocher
    :param case: tuple. Retour de la fonction Case(contenu,courant)
    :return: bool. True si ROCHER est le contenu de case
    """
    contenu, _ = case
    return contenu == ROCHER


def estTronc(case):
    """
    Indique si la case contient un tronc
    :param case: tuple. Retour de la fonction Case(contenu,courant)
    :return: bool. True si VIDE est le contenu de case
    """
    contenu, _ = case
    return contenu == TRONC

def estVide(case):
    """
    Indique si la case contient un rocher
    :param case: tuple. Retour de la fonction Case(contenu,courant)
    :return: bool. True si VIDE est le contenu de case
    """
    contenu, _ = case
    return contenu == VIDE


def estJoueur(case):
    """
    Indique si la case contient un Joueur
    :param case: tuple. Retour de la fonction Case(contenu,courant)
    :return: bool. True si le contenu de case n'est ni VIDE, ROCHER ou TRONC
    """
    contenu, _ = case
    return contenu != ROCHER and contenu != VIDE and contenu != TRONC


def getContenu(case):
    """
    Donne le contenu de la case
    :param case: tuple. Retour de la fonction Case(contenu,courant)
    :return: string ou retour de la fonction Joueur()
    """
    contenu = None
    if case is not None:
        contenu, _ = case
    return contenu


def getCourant(case):
    """
    Donne la direction du courant de la case.
    :param case: tuple. Retour de la fonction Case(contenu,courant)
    :return: string. Une des clés du dictionnaire directions
    """
    courant = None
    if case is not None:
        _, courant = case
    return courant



def getCourantChar(case):
    """
    Retourne la direction du courant de la case sous la forme
    d'une des flèches
    :param case: tuple. Retour de la fonction Case(contenu,courant)
    :return: string. Valeur de directions[courant]
    """
    _, courant = case
    return directions[courant]

def setCourant(case,courant):
    """
    Affecte un courant à une Case
    :param case: tuple. Retour de la fonction Case(contenu,courant)
    :param courant: string. Une des clés de directions
    :return: tuple. case
    """
    contenu, ancien_courant = case
    if courant in directions:
        case = (contenu, courant)
    return case

def setContenu(case,contenu):
    """
    Place un objet sur une case
    :param case: tuple. Retour de la fonction Case(contenu,courant)
    :param contenu: string. Caractère parmi VIDE, TRONC, ROCHER ou le caractère représentant un joueur
    :return: tuple. case
    """
    ancien_contenu, courant = case
    if type(contenu) is str:
        case = (contenu, courant)
    return case


def getDirections():
    """
    permet simplement de récupérer la liste des directions possibles
    il faut que votre fonction se réfère au dictionnaire directions
    :return: liste. clés du dictionnaire directions
    """
    return list(directions.keys())


########################################################################################################################
# TESTS
########################################################################################################################

if __name__ == '__main__':  # Si le module est éxécuté tout seul, c'est a dire s'il n'est pas importé
    l_contenu = [ROCHER, VIDE, TRONC, 'A', 'B', 'C']
    l_case = []

    # Directions possibles du courant
    print('DIRECTIONS POSSIBLES', getDirections())

    # Création de cases
    for contenu in l_contenu:
        for courant in directions.keys():
            l_case.append(Case(contenu, courant))

    # Obtention des informations de cases
    for case in l_case:
        print('--------------------------------------------------------------------------------')
        print('CONTENU : ', getContenu(case))
        print('VERIFICATION CONTENU :', 'Joueur' * estJoueur(case), 'Tronc' * estTronc(case),
              'Rocher' * estRocher(case), 'Vide' * estVide(case))
        print('COURANT : ', getCourant(case), getCourantChar(case))
        case = setContenu(case, VIDE)
        case = setCourant(case, 'N')
        print('CONTENU CHANGE POUR VIDE: ', getContenu(case))
        print('VERIFICATION CONTENU :', 'Joueur' * estJoueur(case), 'Tronc' * estTronc(case),
              'Rocher' * estRocher(case),
              'Vide' * estVide(case))
        print('COURANT CHANGE POUR NORD: ', getCourant(case), getCourantChar(case))
