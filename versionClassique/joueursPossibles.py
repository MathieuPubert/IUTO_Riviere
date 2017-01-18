# Cette structure de données gère les noms et les représentations des joueurs
# le nom permet de connaitre le nom du fichier qui contient l'image représentant le
# joueur en mode graphique et le caractère représentant le joueur sur la grille

# Cette fonction retourne une nouvelle liste de joueurs vide dont les joueurs possibles
# sont passés en paramètre. Il n'y a pas de joueur courant lorsque la liste est vide

def JoueursPossibles():
    """
    Représente une liste d'informations sur des joueurs qui seront utilisées pour créer des Joueurs() en jeu.
    Elle est principalement alimentée par un fichier txt.
    :return: Dictionnaire vide. {}
    """
    return {}


def lireJoueursPossibles(nomFic, joueursPossibles):
    """
    modifie une structure joueursPossibles
    :param joueursPossibles: retour de JoueursPossibles()
    :param nomFic: string. Chemin vers le fichier contenant les joueurs
    :return: None. Modifie la structure
    """
    with open(nomFic, 'r') as fichier:
        for ligne in fichier:
            nom, representation = ligne.split(',')
            ajouterNom(joueursPossibles, nom, representation.strip('\n'))


def ajouterNom(joueursPossibles, nom, representation):
    """
    Ajoute un joueur à la liste des joueurs possibles UNIQUEMENT si son nom ET sa representation n'existent pas.
    Sinon, il ne se produira rien
    :param joueursPossibles: dictionnaire. retour de JoueursPossibles()
    :param nom: string. Nom du joueur
    :param representation: string. Caractère ou chaine contenant le chemin vers le fichier image
    :return: None. Modifie joueursPossibles
    """
    if nom not in joueursPossibles and representation not in joueursPossibles.values():
        joueursPossibles[nom] = representation


def getListeNomsJoueur(joueursPossibles):
    """
    Cette fonction retourne la liste des noms de joueurs possibles
    uniquement les noms pas les représentations
    :param joueursPossibles: dictionnaire. retour de JoueursPossibles()
    :return: liste. Clés du dictionnaire
    """
    return list(joueursPossibles.keys())


def getNomJoueur(joueursPossibles, representation):
    """
    Recherche un joueur par sa représentation
    :param joueursPossibles: dictionnaire. retour de JoueursPossibles()
    :param representation: string.Caractère ou chaine contenant le chemin vers le fichier image
    :return: string. Nom du joueur, None si joueur inexistant
    """
    joueur = None
    for (nom, token) in joueursPossibles.items():
        if representation == token:
            joueur = nom
    return joueur


def getRepresentationJoueur(joueursPossibles, nom):
    """
    Recherche la représentation en fonction de son nom
    :param nom: string. nom du joueur
    :param joueursPossibles: dictionnaire. retour de JoueursPossibles()
    :return: string. Représentation du joueur. Chaine vide si inexistant
    """
    return joueursPossibles.get(nom, '')


########################################################################################################################
# TESTS
########################################################################################################################

if __name__ == '__main__':
    possibles = JoueursPossibles()
    lireJoueursPossibles('data/joueurs.txt', possibles)
    ajouterNom(possibles, 'ErreurRepresentation', 'C')
    ajouterNom(possibles, 'GEA', 'ErreurNom')

    # Parcours de la structure
    print('\n', 'PRESENTATION DES JOUEURS')
    for (nom, representation) in possibles.items():
        print("Voici le joueur '{0}'. Il sera représenté par le symbole '{1}'.".format(
            getNomJoueur(possibles, representation), getRepresentationJoueur(possibles, nom)))
