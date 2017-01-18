from joueur import *
from joueursPossibles import *


# Cette structure de données gère une liste de joueurs, une liste de joueursPossibles
# et un joueur courant. La liste des joueurs possibles permet de connaitre les noms
# des joueurs qui peuvent participer à la descente de la rivière ainsi que leur représentation
# sur la grille (sous la forme d'un seul caractère)
# la liste de joueurs doit préserver l'ordre d'ajout (pour permettre de gérer le classement)

# Cette fonction retourne une nouvelle liste de joueurs vide dont les joueurs possibles
# sont passés en paramètre. Il n'y a pas de joueur courant lorsque la liste est vide

def ListeJoueurs(joueursPossibles={}):
    """
    Structure présentant une liste de joueurs.
    :param joueursPossibles: dictionnaire. retour de la fonction JoueursPossibles()
    :return: dictionnaire :
    {
    'Possibles':joueursPossibles, => Structure JoueursPossibles()
    'Actifs':[], => Liste
    'Courant':None => None s'il n'y a aucun joueur courant. Structure Joueur() sinon.
    }
    """

    return {'Possibles': joueursPossibles, 'Actifs': [], 'Courant': None}


def indiceJoueur(joueurs, nom):
    """
    Donne l'indice du joueur actif indentifié par nom
    :param joueurs: dictionnaire. Retour de la fonction ListeJoueurs()
    :param nom: string. nom du joueur
    :return: integer. Indice du joueur dans joueurs['Actifs'] ou -1 si joueur non présent.
    """
    indice = -1
    i = 0
    while i < len(joueurs['Actifs']) and indice == -1:
        if getNom(joueurs['Actifs'][i]) == nom:
            indice = i
        i += 1
    return indice


def ajouterJoueur(joueurs, nom, humain=True):
    """
    Ajoute un nouveau Joueur() dans les joueurs actifs s'il fait partie des joueurs possibles
    et le place en joueur courant si c'est le  premier joueur actif
    :param joueurs: dictionnaire. Retour de la fonction ListeJoueurs()
    :param nom: string. nom du joueur
    :param humain: bool. True si le joueur est manipulé par un utilisateur
    :return: None. Modifie joueurs
    """
    if nom in joueurs['Possibles']:
        joueurs['Actifs'].append(Joueur(nom, joueurs['Possibles'][nom], humain))
        if len(joueurs['Actifs']) == 1:
            joueurs['Courant'] = joueurs['Actifs'][0]


def retirerJoueur(joueurs, nom):
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
    while i < len(joueurs['Actifs']):
        if getNom(getJoueurCourant(joueurs)) == nom:
            joueurSuivant(joueurs)
        if getNom(joueurs['Actifs'][i]) == nom:
            joueurs['Actifs'].pop(i)
        i += 1
    if joueurs['Actifs'] == []:
        joueurs['Courant'] = None


def getNbJoueurs(joueurs):
    """
    Cette fonction retourne le nombre de joueurs dans la liste
    :param joueurs: retour de la fonction ListeJoueurs()
    :return: integer. nombre de joueurs actifs
    """
    return len(joueurs['Actifs'])


def getJoueursPossibles(joueurs):
    """
    Retourne la structure joueursPossibles associée à la liste de joueurs
    :param joueurs: retour de la fonction ListeJoueurs()
    :return: structure JoueursPossibles()
    """
    return joueurs['Possibles']


def getJoueurCourant(joueurs):
    """
    Cette fonction retourne le joueur courant
    :param joueurs: retour de la fonction ListeJoueurs()
    :return: structure Joueur() ou None si aucun joueur courant
    """
    return joueurs['Courant']


def getJoueurI(joueurs, i):
    """
    Cette fonction retourne le nom du joueur numéro i (dans l'ordre où ils ont été ajoutés)
    i est un entier entre 0 et le nombre de joueurs de la liste -1
    :param joueurs: retour de la fonction ListeJoueurs()
    :param i: integer. Indice du joueur dans joueurs['Actifs']
    :return: structure Joueur()
    """
    return joueurs['Actifs'][i]


def getJoueurRep(joueurs, representation):
    """
    Recherche d'un joueur en fonction de sa representation
    :param joueurs: retour de la fonction ListeJoueurs()
    :param representation: string. Caratère représentant le joueur ou chemin vers fichier image
    :return: tuple de même structure que le retour de la fonction Joueur()
    """
    player = None
    for joueur in joueurs['Actifs']:
        if getRepresentation(joueur) == representation:
            player = joueur
    return player


def viderJoueurs(joueurs):
    """
    Vide la liste de joueurs
    :param joueurs: retour de la fonction ListeJoueurs()
    :return: None. Modifie joueurs
    """
    joueurs['Actifs'] = []
    joueurs['Courant'] = None


def joueurSuivant(joueurs):
    """
    Passe au joueur suivant. Si fin de la liste des joueurs actifs, retourne à l'indice 0
    :param joueurs: retour de la fonction ListeJoueurs()
    :return: None. Modifie joueurs
    """
    indice_courant = indiceJoueur(joueurs, getNom(joueurs['Courant']))
    joueurs['Courant'] = joueurs['Actifs'][(indice_courant + 1) % getNbJoueurs(joueurs)]


########################################################################################################################
# TESTS
########################################################################################################################

if __name__ == '__main__':
    possibles = JoueursPossibles()
    lireJoueursPossibles('data/joueurs.txt', possibles)
    d_joueurs = ListeJoueurs(possibles)

    # Affichage du résultat de l'import
    print("Resultat de l'import:", getJoueursPossibles(d_joueurs))

    # Ajout de l'ensemble des joueurs possibles dans les joueurs actifs
    for (nom, representation) in d_joueurs['Possibles'].items():
        ajouterJoueur(d_joueurs, nom)
        print("Ajout du joueur actif '{0}'".format(nom, representation))

    # Affichage de diverses infos

    print('Nombre de joueurs actifs : ', getNbJoueurs(d_joueurs))
    for (nom, representation) in d_joueurs["Possibles"].items():
        # chaque nom correspond a sa representation ?
        assert (Joueur(nom, representation, True) == getJoueurRep(d_joueurs, representation))
        # chaque joueur à l'indice a t-il le bon nom ?
        print("joueur à l'indice : ", indiceJoueur(d_joueurs, nom), getJoueurI(d_joueurs, indiceJoueur(d_joueurs, nom)))

    for i in range(getNbJoueurs(d_joueurs)):
        courant = getJoueurCourant(d_joueurs)
        # Le joueur courant est-il l'actif à l'indice correspondant?
        assert (getJoueurI(d_joueurs, i) == courant)
        # Puis on les fait cycler
        joueurSuivant(d_joueurs)
        print(i, getJoueurI(d_joueurs, i), getJoueurCourant(d_joueurs))

    retirerJoueur(d_joueurs, 'INFORMATIQUE')

    print(d_joueurs)

    viderJoueurs(d_joueurs)

    print(d_joueurs)
