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
             "Deplacements": 0,
             "RNG": random.randint}

    return d_jeu

# permet de placer le premier joueur sur la case départ et de lui attribuer
# un nombre de déplacements entre 1 et 5
def initJeu(jeu):
    setContenuR(getRiviere(jeu), 0, getColDepart(getRiviere(jeu)), getJoueurCourant(getJoueursJ(jeu)))
    jeu["Deplacements"] = jeu["RNG"](1, 5)


# permet d'obtenir la rivière du jeu
def getRiviere(jeu):
    return jeu["Riviere"]

# permet d'obtenir le classement actuel
def getClassement(jeu):
    return jeu["Classement"]

# permet d'ajouter un nouveau joueur participant à la course
def ajouterJoueurJ(jeu,joueur):
    ajouterJoueur(getJoueursJ(jeu), getNom(joueur), estHumain(joueur))

# permet d'obtenir la liste des joueurs participant à la course
def getJoueursJ(jeu):
    return jeu["Joueurs"]["Actifs"]

# permet de connaitre le nombre joueurs participant à la course
def getNbJoueursJ(jeu):
    return len(getJoueursJ(jeu))

# permet de connaitre le nom du joueur courant
def getJoueurCourantJ(jeu):
    return getNom(getJoueurCourant(getJoueursJ(jeu)))

# permet de retrouver la position d'un joueur sur le plateau en fonction de son nom
def getPosJoueur(jeu,joueur):
    getPositionJoueur(getRiviere(jeu), getRepresentation(joueur))

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
    retirerJoueur(getJoueursJ(jeu), nomJoueur)

# permet de passer au joueur suivant. Cela implique de lui attribuer un nombre
# de coups à jouer et de le positionner sur la case de départ s'il n'est pas sur
# le plateau
def joueurSuivantJ(jeu):
    joueurSuivant(getJoueursJ(jeu))

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

    if estPosR(getRiviere(jeu), x + vx, y + vy):

        # On ne sait pas si cette case est occupée
        res = DIRECTION_NON_AUTORISEE

        if deplacementAutorise(getRiviere(jeu), x, y, direction):
            # On a le feu vert, on peut y aller
            res = DIRECTION_OK

    return res

# pos est un couple de la forme (lig,col) représentant une position sur la grille
# la fonction calcule la direction entre la position du joueur courant et la position pos
# le résultat de la fonction est la direction telle que définie dans le fichier case.py ou
# le caractère 'W' (!!! WTF !!!) si la position du joueur courant et pos ne sont pas deux cases voisines
# de la grille

def calculerDirection(jeu,pos):
    jx, jy = getPosJoueurCourant(jeu)
    x, y = pos

    vx = x - jx
    vy = y - jy

    d_cardinals = {(0, 0): 'X',
                   (0, 2): 'E',
                   (0, -2): 'O',
                   (2, 0): 'S',
                   (-2, 0): 'N',
                   (-1, -1): 'NO',
                   (1, 1): 'SE',
                   (-1, 1): 'NE',
                   (1, -1): 'SO'}

    return d_cardinals.get((vx, vy), 'W')


# permet de verifier si le joueur courant est sur la grille
# si ce n'est pas le cas, on le place sur la case départ
def positionerJoueurCourant(jeu):

    if getPosJoueurCourant(jeu) == (-1, -1):
        setContenuR(getRiviere(jeu), 0, getColDepart(getRiviere(jeu)), getJoueurCourant(getJoueursJ(jeu)))

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
    # pour chaque (x,y)
    for x in range(getNbLigR(getRiviere(jeu))):
        for y in range(getNbColR(getRiviere(jeu))):

            # si on a un courant autre que fixe dans la case
            if getCourantR(getRiviere(jeu), x, y) != 'X':

                # et que la case contient un element mobile
                if not estRocher(getContenuR(getRiviere(jeu), x, y)):
                    # alors on le bouge
                    deplacer(getRiviere(jeu), x, y, getCourantR(getRiviere(jeu, x, y)))
                    # setContenuR(getRiviere(jeu),nouvx,nouvy, getContenuR(getRiviere(jeu, x, y)))
                    # setContenuR(getRiviere(jeu), x, y, "VIDE")



# Cette fonction va essayer de déplacer le joueur courant dans la direction
# indiquée en paramètre. Le fonction verifDirection sera utilisée.
# le résultat de la fonction sera une chaine de caractères indiquant ce qu'il
# s'est passé lors du déplacement. Si le déplacement est valide il faut effectuer
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
    sumstr = 'ATTENTION DIRECTION INCORRECTE'

    # Si on peut se deplacer
    if verifDirection(jeu, direction) == DIRECTION_OK:

        # Si le joueur decide de ne pas bouger
        if direction == 'X':
            sumstr = "le joueur xx renonce à ses derniers déplacements"
            enleverTousCoupsRestants(jeu)

        # Si le joueur bouge
        else:
            # On lui enleve un coup
            enleverCoupsRestants(jeu)

            # si il est arrivé :
            if joueurArrive(getRiviere(jeu)):
                sumstr = "Le joueur xx est arrivé"

                print("Le tour se termine car le joueur xx est arrivé")

            # On vire tout ce qui se trouve sur l'arrivée
            else:
                viderArrivee(getRiviere(jeu))

    return sumstr
