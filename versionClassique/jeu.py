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
    :return: dictionnaire.
     {"Classement": [],
      "Joueurs": ListeJoueurs(pions),
      "Riviere": lireRiviere(prefixe + ficRiviere),
      "Deplacements": 0,
      "RNG": random.randint}
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


def initJeu(jeu):
    """
    Permet de placer le premier joueur sur la case départ et de lui attribuer
    un nombre de déplacements entre 1 et 5
    :param jeu: retour de la fonction Jeu()
    :return: None. Modifie jeu
    """
    setContenuR(getRiviere(jeu), 0, getColDepart(getRiviere(jeu)), getJoueurCourant(getJoueursJ(jeu)))
    jeu["Deplacements"] = jeu["RNG"](1, 5)



def getRiviere(jeu):
    """
    Permet d'obtenir la rivière du jeu
    :param jeu: retour de la fonction Jeu()
    :return: retour de Riviere. Riviere utilisee par le jeu
    """
    return jeu["Riviere"]


def getClassement(jeu):
    """
    Permet d'obtenir le classement actuel
    :param jeu: retour de la fonction Jeu()
    :return: Liste[String]. Classement
    """
    return jeu["Classement"]


def ajouterJoueurJ(jeu,joueur):
    """
    Permet d'ajouter un nouveau joueur participant à la course
    :param jeu: retour de la fonction Jeu()
    :param joueur: retour de la fonction Joueu()
    :return: None. Modifie jeu
    """
    ajouterJoueur(getJoueursJ(jeu), getNom(joueur), estHumain(joueur))


def getJoueursJ(jeu):
    """
    Permet d'obtenir la liste des joueurs participant à la course
    :param jeu: retour de la fonction Jeu()
    :return: liste [Joueur()]. liste des joueurs actifs
    """
    return jeu["Joueurs"]["Actifs"]


def getNbJoueursJ(jeu):
    """
    Permet de connaitre le nombre joueurs participant à la course
    :param jeu: retour de la fonction Jeu()
    :return: Integer. nombre de joueurs actifs
    """
    return len(getJoueursJ(jeu))


def getJoueurCourantJ(jeu):
    """
    Permet de connaitre le nom du joueur courant
    :param jeu: retour de la fonction Jeu()
    :return: Sring. Nom du joueur courant
    """
    return getNom(getJoueurCourant(getJoueursJ(jeu)))


def getPosJoueur(jeu,joueur):
    """
    Permet de retrouver la position d'un joueur sur le plateau en fonction de son nom
    :param jeu: retour de la fonction Jeu()
    :param joueur : retour de la fonction Joueur()
    :return: tuple(int,int). coordonnées du joueur
    """
    return getPositionJoueur(getRiviere(jeu), getRepresentation(joueur))


def getPosJoueurCourant(jeu):
    """
    Permet de connaitre la position du joueur courant
    :param jeu: retour de la fonction Jeu()
    :return: tuple(int,int). coordonnées du joueur courant
    """
    return getPosJoueur(jeu, getJoueurCourantJ(jeu))


def getNbCoupsRestants(jeu):
    """
    Permet le nombre de coups restants au joueur courant
    :param jeu: retour de la fonction Jeu()
    :return: Integer. nombre de deplacements restant au joueur
    """
    return jeu["Deplacements"]


def enleverCoupsRestants(jeu):
    """
    Permet d'enlever un coup au joueur courant
    :param jeu: retour de la fonction Jeu()
    :return: None. Modifie jeu
    """
    jeu["Deplacements"] += -1


def enleverTousCoupsRestants(jeu):
    """
    Permet d'enlever tout les coups restant du joueur courant
    :param jeu: retour de la fonction Jeu()
    :return: None. Modifie jeu
    """
    jeu["Deplacements"] = 0


def ajouterClassement(jeu,nomJoueur):
    """
    Permet d'ajouter un joueur au classement et de l'enlever à la liste des
    joueurs participants à la course
    :param jeu: retour de la fonction Jeu()
    :param nomJoueur : string. nom d'un joueur
    :return: None. Modifie jeu
    """
    retirerJoueur(getJoueursJ(jeu), nomJoueur)


def joueurSuivantJ(jeu):
    """
    Permet de passer au joueur suivant. Cela implique de lui attribuer un nombre
    de coups à jouer et de le positionner sur la case de départ s'il n'est pas sur
    le plateau
    :param jeu: retour de la fonction Jeu()
    :return:None. modifie jeu
    """
    joueurSuivant(getJoueursJ(jeu))


def verifDirection(jeu,direction):
    """
    Permet de verifier si la direction passée en paramètre est bien une position
    et si c'est le cas, que le joueur courant a le droit de se déplacer dans cette
    direction
    :param jeu: retour de la fonction Jeu()
    :param direction: string. Caractère etant clé du dictionnaire directions dans case.py
    :return: PAS_UNE_DIRECTION,soit DIRECTION_NON_AUTORISEE,soit DIRECTION_OK
    """
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


def calculerDirection(jeu,pos):
    """
    Calcule la direction entre la position du joueur courant et la position pos
    :param jeu: retour de la fonction Jeu()
    :param pos: tuple(int,int). couple de la forme (lig,col) représentant une position sur la grille
    :return: string. Caractère etant clé du dictionnaire directions dans case.py ou 'W'
    """
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


def positionerJoueurCourant(jeu):
    """

    Permet de verifier si le joueur courant est sur la grille
    si ce n'est pas le cas, on le place sur la case départ
    :param jeu: retour de la fonction Jeu()
    :return: None. modifie jeu
    """

    if getPosJoueurCourant(jeu) == (-1, -1):
        setContenuR(getRiviere(jeu), 0, getColDepart(getRiviere(jeu)), getJoueurCourant(getJoueursJ(jeu)))


def finirDeplacement(jeu):
    """
    Cette fonction permet de finir le tour d'un joueur en déplaçant les objets
    amovibles qui se trouve sur des cases où il y a du courant suivant les règles
    énoncé dans le sujet du projet
    La fonction effectue un déplacement si un objet est à déplacer
    Sinon elle ne fait rien
    Elle retourne un couple constitué d'un booléen et d'une chaine de caractères
    le booléen est True si aucun déplacement n'a été effectué et False sinon
    la chaine de caractères vaut
    'La partie est terminée'  si aucun déplacement n'a été effectué mais qu'il ne reste
                              plus aucun joueur sur la rivière
    'Le joueur xx est arrive' si il y a eu un déplacement qui a engendré l'arrivée
                              du joueur xx
    ''                        dans les autres cas

    :param jeu: retour de la fonction Jeu()
    :return: None. modifie jeu
    """


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


def jouerDirection(jeu,direction):
    """
    Cette fonction va essayer de déplacer le joueur courant dans la direction
    indiquée en paramètre. Le fonction verifDirection sera utilisée.
    le résultat de la fonction sera une chaine de caractères indiquant ce qu'il
    s'est passé lors du déplacement. Si le déplacement est valide il faut effectuer
    le déplacement et ses conséquences (par exemple si un objet est sur la case d'arrivée)
    penser à enlever un coup à jouer
    Les valeurs de retour possibles
    "le joueur xx renonce à ses derniers déplacements"
       -----> si la direction est 'X' dans ce cas le nombre de coups restants repasse à 0
    "Le tour se termine car le joueur xx est arrivé"
       -----> si une des conséquences du déplacement est que le joueur courant est arrivé
    "Le joueur xx est arrivé"
       -----> si une des conséquences du déplacement est qu'un joueur autre que le joueur
              courant est arrivé
    ""
       -----> si le déplacement n'a rien provoqué de spécial
    "Attention direction incorrecte"
       -----> si le déplacement n'est pas correct
    :param jeu: retour de la fonction Jeu()
    :param direction: string. Caractère etant clé du dictionnaire directions dans case.py ou 'W'
    :return: string. phrase d'informations
    """
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
