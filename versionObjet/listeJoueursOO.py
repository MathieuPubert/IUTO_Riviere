from joueurOO import *
from joueursPossiblesOO import *


class ListeJoueurs(object):
    """
    # Cette structure de données gère une liste de joueurs, une liste de joueursPossibles
    # et un joueur courant. La liste des joueurs possibles permet de connaitre les noms
    # des joueurs qui peuvent participer à la descente de la rivière ainsi que leur représentation
    # sur la grille (sous la forme d'un seul caractère)
    # la liste de joueurs doit préserver l'ordre d'ajout (pour permettre de gérer le classement)
    """

    def __init__(self, joueurspossibles):
        self.possibles = joueurspossibles
        self.actifs = []
        self.courant = None

    def indice_joueur(self, nom):

        indice = -1
        i = 0
        while i < len(self.actifs) and indice == -1:
            if self.actifs[i].get_nom() == nom:
                indice = i
            i += 1
        return indice

    def ajouter_joueur(self, nom, humain=True):
        """
        Ajoute un nouveau Joueur() dans les joueurs actifs s'il fait partie des joueurs possibles
        et le place en joueur courant si c'est le  premier joueur actif
        :param joueurs: dictionnaire. Retour de la fonction ListeJoueurs()
        :param nom: string. nom du joueur
        :param humain: bool. True si le joueur est manipulé par un utilisateur
        :return: None. Modifie joueurs
        """
        if nom in self.possibles.pions:
            self.actifs.append(Joueur(nom, self.possibles.get_representationjoueur(nom), humain))
            if len(self.actifs) == 1:
                self.courant = self.actifs[0]

    def retirer_joueur(self, nom):
        """
        Cette fonction retire un joueur de la liste
        Si le joueur n'y était pas elle ne fait rien
        Si je joueur etait lejoueur courant, passe son tour au suivant.
        Attention si la liste devient vide il n'y a plus de joueur courant
        :param joueurs: dictionnaire. Retour de la fonction ListeJoueurs()
        :param nom:  string. nom du joueur
        :return: None. Modifie joueurs
        """
        i = 0
        while i < len(self.actifs):
            if self.get_joueurcourant() == nom:
                self.joueur_suivant()
            if self.actifs[i].get_nom() == nom:
                self.actifs.pop(i)
            i += 1
        if self.actifs == []:
            self.courant = None

    def get_nbjoueurs(self):
        """
        Cette fonction retourne le nombre de joueurs dans la liste
        :param joueurs: retour de la fonction ListeJoueurs()
        :return: integer. nombre de joueurs actifs
        """
        return len(self.actifs)

    def get_joueurspossibles(self):
        """
        Retourne la structure joueursPossibles associée à la liste de joueurs
        :param joueurs: retour de la fonction ListeJoueurs()
        :return: structure JoueursPossibles()
        """
        return self.possibles

    def get_joueurcourant(self):
        """
        Cette fonction retourne le joueur courant
        :param joueurs: retour de la fonction ListeJoueurs()
        :return: structure Joueur() ou None si aucun joueur courant
        """
        return self.courant

    def get_joueuri(self, i):
        """
        Cette fonction retourne le nom du joueur numéro i (dans l'ordre où ils ont été ajoutés)
        i est un entier entre 0 et le nombre de joueurs de la liste -1
        :param joueurs: retour de la fonction ListeJoueurs()
        :param i: integer. Indice du joueur dans self.actifs
        :return: string. nom du joueur
        """
        return self.actifs[i].get_nom()

    def get_joueurrep(self, representation):
        """
        Recherche d'un joueur en fonction de sa representation
        :param joueurs: retour de la fonction ListeJoueurs()
        :param representation: string. Caratère représentant le joueur ou chemin vers fichier image
        :return: tuple de même structure que le retour de la fonction Joueur()
        """
        player = None
        for joueur in self.actifs:
            if joueur.get_representation() == representation:
                player = joueur
        return player

    def vider_joueurs(self):
        """
        Vide la liste de joueurs
        :param joueurs: retour de la fonction ListeJoueurs()
        :return: None. Modifie joueurs
        """
        self.actifs = []
        self.courant = None

    def joueur_suivant(self):
        """
        Passe au joueur suivant. Si fin de la liste des joueurs actifs, retourne à l'indice 0
        :param joueurs: retour de la fonction ListeJoueurs()
        :return: None. Modifie joueurs
        """
        indice_courant = self.indice_joueur(self.courant.get_nom())
        self.courant = self.actifs[(indice_courant + 1) % self.get_nbjoueurs(self)]


########################################################################################################################
# TESTS
########################################################################################################################

if __name__ == '__main__':
    possibles = JoueursPossibles()
    possibles.lire_joueurspossibles('data/joueurs.txt')
    joueurs = ListeJoueurs(possibles)

    # Affichage du résultat de l'import
    print("Resultat de l'import:", joueurs.get_joueurspossibles())

    # Ajout de l'ensemble des joueurs possibles dans les joueurs actifs
    for (nom, representation) in joueurs.get_joueurspossibles().pions.items():
        joueurs.ajouter_joueur(nom, True)
        print("Ajout du joueur actif '{0}'".format(nom, representation))

    # Affichage de diverses infos

    print('Nombre de joueurs actifs : ', joueurs.get_nbjoueurs())
    for (nom, representation) in joueurs.possibles.pions.items():
        # chaque joueur à l'indice a t-il le bon nom ?
        print("joueur à l'indice : ", joueurs.indice_joueur(nom), joueurs.get_joueuri(joueurs.indice_joueur(nom)))

    for i in range(joueurs.get_nbjoueurs()):
        courant = joueurs.get_joueurcourant()
        # Le joueur courant est-il l'actif à l'indice correspondant?
        assert (joueurs.get_joueuri(i) == courant)
        # Puis on les fait cycler
        joueurs.joueur_suivant()
        print(i, joueurs.get_joueuri(i), joueurs.get_joueurcourant())

    joueurs.retirer_joueur('INFORMATIQUE')

    print(joueurs.actifs)

    joueurs.vider_joueurs()

    print(joueurs.actifs)
