class Joueur(object):
    def __init__(self,nom, representation, humain=True):
        """
        Représentation d'un joueur.
        Choix du dictionnaire
        :param nom: string. Nom du joueur
        :param representation: string. Soit un caractère, soit un chemin vers un fichier image
        :param humain: bool. True si le joueur est manipulé par un utilisateur (présumé humain).
        :return: Dictionnaire. {'Nom':nom, 'Pion':'representation, 'Humain':humain}
        """
        self.nom = nom
        self.representation = representation
        self.humain = humain
        self.joueur = None

        #type(self.nom) is str and type(self.representation) is str and type(self.humain) is bool

    def getNom(self):
        """
        Donne le nom du joueur
        :param joueur: retour de la fonction Joueur()
        :return: string. Nom du joueur
        """
        return self.nom


    def getRepresentation(self):
        """
        Donne la representation du joueur
        :param joueur: retour de la fonction Joueur()
        :return: string. Représentation du joueur
        """
        return self.representation


    def estHumain(self):
        """
        Indique si le joueur est manipulé par un utilisateur
        :param joueur: retour de la fonction Joueur()
        :return: bool. True si le joueur est manipulé par un utilisateur
        """
        if humain is not None:
            return self.humain
        else:
            return None


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
                joueur = Joueur(nom, representation)
                print('Joueur() : ', joueur)

                print('getNomr() : ', joueur.getNom())

                print('getRepresentation() : ', joueur.getRepresentation())

                print('estHumain() : ', joueur.estHumain())

                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')

    print('Test pour mauvais parametre :')
    joueur = None
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
    joueur = None
    print('Joueur() : ', joueur)

    print('getNomr() : ', joueur.getNom())

    print('getRepresentation() : ', joueur.getRepresentation())

    print('estHumain() : ', joueur.estHumain())

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')
