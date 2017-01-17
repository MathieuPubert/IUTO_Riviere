from riviere import *
from listeJoueurs import *
import random

# ces constantes servent à gérer le code retour de la fonction verifDirection
DIRECTION_OK=0
PAS_UNE_DIRECTION=1
DIRECTION_NON_AUTORISEE=2


def Jeu(prefixe,ficJoueurs,ficRiviere):
    """
    Cette fonction abominable:
    - créée un nouveau jeu
    - initiatise le classement
    - initialise les participants à vide
    - initialise une liste joueurs connus contenue dans le fichier passé en paramètre
    - conserve aussi le nombre de coups restants au joueur courant
    - initialise aussi le générateur de nombres aléatoires
    :param prefixe: string. chemin vers le dossier du jeu
    :param ficJoueurs: string. nom du fichier contenant les noms et representations des joueurs (pour JoueursPossibles)
    :param ficRiviere: string. nom du fichier contenant une configuration initiale d'une riviere
    :return: None. Procedure principale du programme
    """

    ## On recupere les noms et representations
    pions = JoueursPossibles()

    lireJoueursPossibles(prefixe + ficJoueurs, pions)

    ## On fabrique la structure
    d_jeu = {"Classement": [],
             "Joueurs": ListeJoueurs(pions),
             "Riviere": lireRiviere(prefixe + ficRiviere),
             "Deplacements": 0}

    return d_jeu

# permet de placer le premier joueur sur la case départ et de lui attribuer
# un nombre de déplacements entre 1 et 5
def initJeu(jeu):
    setContenuR(jeu["Riviere"], 0, getColDepart(jeu["Riviere"]), jeu["Joueurs"]["Courant"])
    jeu["Deplacements"] = random.randint(1, 5)


# permet d'obtenir la rivière du jeu
def getRiviere(jeu):
    return jeu["Riviere"]

# permet d'obtenir le classement actuel
def getClassement(jeu):
    return jeu["Classement"]

# permet d'ajouter un nouveau joueur participant à la course
def ajouterJoueurJ(jeu,joueur):
    ajouterJoueur(jeu["Joueurs"], joueur["Nom"], joueur["Humain"])

# permet d'obtenir la liste des joueurs participant à la course
def getJoueursJ(jeu):
    return jeu["Joueurs"]["Actifs"]

# permet de connaitre le nombre joueurs participant à la course
def getNbJoueursJ(jeu):
    return len(getJoueursJ(jeu))

# permet de connaitre le nom du joueur courant
def getJoueurCourantJ(jeu):
    return jeu["Joueurs"]["Courant"]["Nom"]

# permet de retrouver la position d'un joueur sur le plateau en fonction de son nom
def getPosJoueur(jeu,joueur):
    getPositionJoueur(jeu["Riviere"], joueur["Representation"])

# permet de retrouver la position du joueur courant
def getPosJoueurCourant(jeu):
    return getPosJoueur(jeu, getJoueurCourantJ(jeu))

# permet le nombre de coups restants au joueur courant
def getNbCoupsRestants(jeu):
    return jeu["Deplacements"]
   
# permet d'enlever un coup au joueur courant
def enleverCoupsRestants(jeu):
    jeu["Deplacements"] += -1

# permet d'enlever tout les coups restant du joueur courant
def enleverTousCoupsRestants(jeu):
    jeu["Deplacements"] = 0
    
# permet d'ajouter un joueur au classement et de l'enlever à la liste des 
# joueurs participants à la course
def ajouterClassement(jeu,nomJoueur):
    retirerJoueur(jeu["Joueurs"], nomJoueur)

# permet de passer au joueur suivant. Cela implique de lui attribuer un nombre
# de coups à jouer et de le positionner sur la case de départ s'il n'est pas sur
# le plateau
def joueurSuivantJ(jeu):
    joueurSuivant(jeu["Joueurs"])

# permet de verifier si la direction passée en paramètre est bien une position
# et si c'est le cas, que le joueur courant a le droit de se déplacer dans cette
# direction
# Le code retour de cette fonction est soit PAS_UNE_DIRECTION, soit DIRECTION_NON_AUTORISEE
# soit DIRECTION_OK
def verifDirection(jeu,direction):
    x, y = getPosJoueurCourant(jeu)
    vx, vy = incDirectionGH(direction)

    # Par defaut
    res = PAS_UNE_DIRECTION

    if estPosR(jeu["Riviere"], x + vx, y + vy):

        # On ne sait pas si cette case est occupée
        res = DIRECTION_NON_AUTORISEE

        if deplacementAutorise(jeu["Riviere"], x, y, direction):
            # On a le feu vert, on peut y aller
            res = DIRECTION_OK

    return res

# pos est un couple de la forme (lig,col) représentant une position sur la grille
# la fonction calcule la direction entre la position du joueur courant et la position pos
# le résultat de la fonction est la direction telle que définie dans le fichier case.py ou
# le caractère 'W' si la position du joueur courant et pos ne sont pas deux cases voisines
# de la grille

def calculerDirection(jeu,pos):
    ## ATTENTION CANCER !!! CE MONTAGE PEUT FAIRE VOMIR !
    xjc, yjc = getPosJoueurCourant(jeu)
    x, y = pos
    cardinals = {}
    cardinals.keys = directions.values()
    cardinals.values = directions.keys()
    vx = -((xjc - x) % 3)
    vy = -((yjc - y) % 3)

    return cardinals[(vx, vy)]


# permet de verifier si le joueur courant est sur la grille
# si ce n'est pas le cas, on le place sur la case départ
def positionerJoueurCourant(jeu):
    if getPosJoueurCourant(jeu) == (-1, -1):
        setContenuR(jeu["Riviere"], 0, getColDepart(jeu["Riviere"]), jeu["Joueurs"]["Courant"])

# Cette fonction permet de finir le tour d'un joueur en déplaçant les objets
# amovibles qui se trouve sur des cases où il y a du courant suivant les règles
# énoncé dans le sujet du projet
# La fonction effectue un déplacement si un objet est à déplacer
# Sinon elle ne fait rien
# Elle retourne un couple constitué d'un booléen et d'une chaine de caractères
# le booléen est True si aucun déplacement n'a été effectué et False sinon
# la chaine de caractères vaut
# 'La partie est terminée'  si aucun déplacement n'a été effectué mais qu'il ne reste
#                           plus aucun joueur sur la rivière
# 'Le joueur xx est arrive' si il y a eu un déplacement qui a engendré l'arrivée
#                           du joueur xx
# ''                        dans les autres cas
def finirDeplacement(jeu):
    pass
    
# Cette fonction va essayer de déplacer le joueur courant dans la direction
# indiquée en paramètre. Le fonction verifDirection sera utilisée.
# le résultat de la fonction sera une chaine de caractères indiquant ce qu'il
# s'est passé leur du déplacement. Si le déplacement est valide il faut effectuer
# le déplacement et ses conséquences (par exemple si un objet est sur la case d'arrivée)
# penser à enlever un coup à jouer
# Les valeurs de retour possibles
# "le joueur xx renonce à ses derniers déplacements" 
#    -----> si la direction est 'X' dans ce cas le nombre de coups restants repasse à 0
# "Le tour se termine car le joueur xx est arrivé"
#    -----> si une des conséquences du déplacement est que le joueur courant est arrivé
# "Le joueur xx est arrivé"
#    -----> si une des conséquences du déplacement est qu'un joueur autre que le joueur 
#           courant est arrivé
# ""
#    -----> si le déplacement n'a rien provoqué de spécial
# "Attention direction incorrecte"
#    -----> si le déplacement n'est pas correct
def jouerDirection(jeu,direction):
    pass
