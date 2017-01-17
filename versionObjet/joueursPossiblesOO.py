class JoueursPossibles(object):
    """
    # Cette structure de données gère les noms et les représentations des joueurs
    # le nom permet de connaitre le nom du fichier qui contient l'image représentant le
    # joueur en mode graphique et le caractère représentant le joueur sur la grille
    # Cette fonction retourne une nouvelle liste de joueurs vide dont les joueurs possibles
    # sont passés en paramètre. Il n'y a pas de joueur courant lorsque la liste est vide
    """

    def __init__(self):
        self.pions = {}

    def lire_joueurspossibles(self, nomFic):
        with open(nomFic, 'r') as fichier:
            for ligne in fichier:
                nom, representation = ligne.split(',')
                self.ajouter_nom(nom, representation.strip('\n'))

    def ajouter_nom(self, nom, representation):
        if nom not in self.pions and representation not in self.pions.values():
            self.pions[nom] = representation

    def get_listenomsjoueurs(self):
        return list(self.pions.keys())

    def get_nomjoueur(self, representation):

        joueur = ''
        for (nom, token) in self.pions.items():
            if representation == token:
                joueur = nom
        return joueur

    def get_representationjoueur(self, nom):
        """
        Recherche la représentation en fonction de son nom
        :param joueursPossibles: dictionnaire. retour de JoueursPossibles()
        :return: string. Représentation du joueur. Chaine vide si inexistant
        """
        return self.pions.get(nom, '')


########################################################################################################################
# TESTS
########################################################################################################################

if __name__ == '__main__':
    possibles = JoueursPossibles()
    possibles.lire_joueurspossibles('data/joueurs.txt')
    possibles.ajouter_nom('ErreurRepresentation', 'C')
    possibles.ajouter_nom('GEA', 'ErreurNom')

    # Parcours de la structure
    print('\n', 'PRESENTATION DES JOUEURS')
    for (nom, representation) in possibles.pions.items():
        print("Voici le joueur '{0}'. Il sera représenté par le symbole '{1}'.".format(
            possibles.get_nomjoueur(representation), possibles.get_representationjoueur(nom)))
