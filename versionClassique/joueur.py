def Joueur(nom, representation, humain=True):
    """
    Représentation d'un joueur.
    Choix du dictionnaire
    :param nom: string. Nom du joueur
    :param representation: string. Soit un caractère, soit un chemin vers un fichier image
    :param humain: bool. True si le joueur est manipulé par un utilisateur (présumé humain).
    :return: Dictionnaire. {'Nom':nom, 'Pion':'representation, 'Humain':humain}
    """
    joueur = None

    if type(nom) is str and type(representation) is str and type(humain) is bool:
        joueur = {'Nom': nom, 'Representation': representation, 'Humain': humain}
    return joueur


def getNom(joueur):
    """
    Donne le nom du joueur
    :param joueur: retour de la fonction Joueur()
    :return: string. Nom du joueur
    """
    nom = None
    if joueur is not None:
        nom = joueur['Nom']
    return nom


def getRepresentation(joueur):
    """
    Donne la representation du joueur
    :param joueur: retour de la fonction Joueur()
    :return: string. Représentation du joueur
    """
    rep = None
    if joueur is not None:
        rep = joueur['Representation']
    return rep


def estHumain(joueur):
    """
    Indique si le joueur est manipulé par un utilisateur
    :param joueur: retour de la fonction Joueur()
    :return: bool. True si le joueur est manipulé par un utilisateur
    """
    hum = None
    if joueur is not None:
        hum = joueur['Humain']
    return hum


########################################################################################################################
# TESTS
########################################################################################################################

if __name__ == '__main__':
    print('TEST des fonctions de joueur.py : ')
    l_noms = ['NOM_1', 'NOM_2', 'NOM_3', 'NOM_4', 'NOM_5', 'NOM_5', 'NOM_7']

    for representation in 'AZERTYUIOPQSDFGHJKLMWXCVBN':
        for nom in l_noms:
            for humain in (True, False):
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
                joueur = Joueur(nom, representation, humain)
                print('Joueur() : ', joueur)

                print('getNomr() : ', getNom(joueur))

                print('getRepresentation() : ', getRepresentation(joueur))

                print('estHumain() : ', estHumain(joueur))

                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')

    print('Test pour mauvais parametre :')
    joueur = None
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
    joueur = None
    print('Joueur() : ', joueur)

    print('getNomr() : ', getNom(joueur))

    print('getRepresentation() : ', getRepresentation(joueur))

    print('estHumain() : ', estHumain(joueur))

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')
