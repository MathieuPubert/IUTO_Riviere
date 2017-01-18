def Joueur(nom, representation, humain=True):
    """
    Représentation d'un joueur.
    Choix du dictionnaire
    :param nom: string. Nom du joueur
    :param representation: string. Soit un caractère, soit un chemin vers un fichier image
    :param humain: bool. True si le joueur est manipulé par un utilisateur (présumé humain).
    :return: Dictionnaire. {'Nom':nom, 'Pion':'representation, 'Humain':humain}
    """
    return {'Nom': nom, 'Representation': representation, 'Humain': humain}


def getNom(joueur):
    """
    Donne le nom du joueur
    :param joueur: retour de la fonction Joueur()
    :return: string. Nom du joueur
    """
    return joueur['Nom']


def getRepresentation(joueur):
    """
    Donne la representation du joueur
    :param joueur: retour de la fonction Joueur()
    :return: string. Représentation du joueur
    """
    return joueur['Representation']


def estHumain(joueur):
    """
    Indique si le joueur est manipulé par un utilisateur
    :param joueur: retour de la fonction Joueur()
    :return: bool. True si le joueur est manipulé par un utilisateur
    """
    return joueur['Humain']


########################################################################################################################
# TESTS
########################################################################################################################

if __name__ == '__main__':
    l_joueurs = [Joueur('Luc', 'L', True),
                 Joueur('Marc', 'M', True),
                 Joueur('Jean', 'J', True),
                 Joueur('AI', 'A', False)]

    for joueur in l_joueurs:
        descriptif = "Le joueur {0} sera représenté par le symbole '{1}'. Il est manipulé par {2}".format(
            getNom(joueur), getRepresentation(joueur),
            ('un humain' * estHumain(joueur) + 'une IA' * (not estHumain(joueur))))
        print(descriptif)
