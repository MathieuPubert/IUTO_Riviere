
# Cette structure de données gère les noms et les représentations des joueurs
# le nom permet de connaitre le nom du fichier qui contient l'image représentant le
# joueur en mode graphique et le caractère représentant le joueur sur la grille

# Cette fonction retourne une nouvelle liste de joueurs vide dont les joueurs possibles
# sont passés en paramètre. Il n'y a pas de joueur courant lorsque la liste est vide

def JoueursPossibles():
    """
    Représente une liste d'informations sur des joueurs qui seront utilisées pour créer des Joueurs() en jeu.
    Elle est principalement alimentée par un fichier txt.
    :return: Dictionnaire. {'Nom Joueur': représentation}
    """
    return {}


def lireJoueursPossibles(nomFic):
    """
    retourne une liste des joueurs possibles
    :param nomFic: string. Chemin vers le fichier contenant les joueurs
    :return: liste de tuples (nom, representation)
    """
    l_joueurs = []
    with open(nomFic, 'r') as fichier:
        for ligne in fichier:
            nom, representation = ligne.split(',')
            l_joueurs.append((nom, representation.strip('\n')))
    return l_joueurs


def ajouterNom(joueursPossibles,nom,representation):
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


def getNomJoueur(joueursPossibles,representation):
    """
    Recherche un joueur par sa représentation
    :param joueursPossibles: dictionnaire. retour de JoueursPossibles()
    :param representation: string.Caractère ou chaine contenant le chemin vers le fichier image
    :return: string. Nom du joueur, chaine vide si joueur inexistant
    """
    joueur = ''
    for (nom, token) in joueursPossibles.items():
        if representation == token:
            joueur = nom
    return joueur


        

def getRepresentationJoueur(joueursPossibles,nom):
    """
    Recherche la représentation en fonction de son nom
    :param joueursPossibles: dictionnaire. retour de JoueursPossibles()
    :return: string. Représentation du joueur. Chaine vide si inexistant
    """
    return joueursPossibles.get(nom, '')


########################################################################################################################
# TESTS
########################################################################################################################

if __name__ == '__main__':
    joueursfichier = lireJoueursPossibles('data/joueurs.txt')
    joueursfichier.append(('ErreurRepresentation', 'A'))
    joueursfichier.append(('GEA', 'ErreurNom'))
    possibles = JoueursPossibles()

    # Ajout des joueurs
    print('\n', 'AJOUT DES JOUEURS')
    for (nom, representation) in joueursfichier:
        ajouterNom(possibles, nom, representation)
        print("Ajout de '{0}' représenté par un symbole '{1}'".format(nom, representation))

    # Parcours de la structure
    print('\n', 'PRESENTATION DES JOUEURS')
    for (nom, representation) in possibles.items():
        print("Voici le joueur '{0}'. Il sera représenté par le symbole '{1}'.".format(
            getNomJoueur(possibles, representation), getRepresentationJoueur(possibles, nom)))
