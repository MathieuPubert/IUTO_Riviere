from riviere import *
from listeJoueurs import *
import random

# ces constantes servent à gérer le code retour de la fonction verifDirection
DIRECTION_OK = 0
PAS_UNE_DIRECTION = 1
DIRECTION_NON_AUTORISEE = 2


def Jeu(prefixe, ficJoueurs, ficRiviere):
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
    setContenuR(getRiviere(jeu), 0, getColDepart(getRiviere(jeu)), getRepresentation(getJoueurCourant(getJoueursJ(jeu))))
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


def ajouterJoueurJ(jeu, joueur):
    """
    Permet d'ajouter un nouveau joueur participant à la course
    :param jeu: retour de la fonction Jeu()
    :param joueur: retour de la fonction Joueur()
    :return: None. Modifie jeu
    """
    ajouterJoueur(getJoueursJ(jeu), getNom(joueur), estHumain(joueur))


def getJoueursJ(jeu):
    """
    Permet d'obtenir la liste des joueurs participant à la course
    :param jeu: retour de la fonction Jeu()
    :return: structure listeJoueurs. liste des joueurs
    """
    return jeu["Joueurs"]


def getNbJoueursJ(jeu):
    """
    Permet de connaitre le nombre joueurs participant à la course
    :param jeu: retour de la fonction Jeu()
    :return: Integer. nombre de joueurs actifs
    """
    return getNbJoueurs(getJoueursJ(jeu))


def getJoueurCourantJ(jeu):
    """
    Permet de connaitre le nom du joueur courant
    :param jeu: retour de la fonction Jeu()
    :return: Structure Joueur(). Joueur courant
    """
    return getJoueurCourant(getJoueursJ(jeu))


def getPosJoueur(jeu, joueur):
    """
    Permet de retrouver la position d'un joueur sur le plateau en fonction de son nom
    :param jeu: retour de la fonction Jeu()
    :param joueur : string. nom du joueur
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
    nbcoups = jeu["Deplacements"]
    if nbcoups<0:
        nbcoups=0
    return nbcoups


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


def ajouterClassement(jeu, nomJoueur):
    """
    Permet d'ajouter un joueur au classement et de l'enlever à la liste des
    joueurs participants à la course
    :param jeu: retour de la fonction Jeu()
    :param nomJoueur : string. nom d'un joueur
    :return: None. Modifie jeu
    """
    jeu["Classement"].append(getJoueurI(getJoueursJ(jeu), indiceJoueur(getJoueursJ(jeu), nomJoueur)))

    retirerJoueur(getJoueursJ(jeu), nomJoueur)

    viderArrivee(getRiviere(jeu))

def joueurSuivantJ(jeu):
    """
    Permet de passer au joueur suivant. Cela implique de lui attribuer un nombre
    de coups à jouer et de le positionner sur la case de départ s'il n'est pas sur
    le plateau
    :param jeu: retour de la fonction Jeu()
    :return:None. modifie jeu
    """
    joueurSuivant(getJoueursJ(jeu))
    positionerJoueurCourant(jeu)
    jeu["Deplacements"] = jeu["RNG"](1,5)




def verifDirection(jeu, direction):
    """
    Permet de verifier si la direction passée en paramètre est bien une position
    et si c'est le cas, que le joueur courant a le droit de se déplacer dans cette
    direction
    :param jeu: retour de la fonction Jeu()
    :param direction: string. Caractère etant clé du dictionnaire directions dans case.py
    :return: PAS_UNE_DIRECTION,soit DIRECTION_NON_AUTORISEE,soit DIRECTION_OK
    """
    res = PAS_UNE_DIRECTION

    if direction in getDirections():
        x, y = getPosJoueurCourant(jeu)
        vx, vy = incDirectionGH(direction)

        dx,dy = (x+vx, y+vy)

        res = DIRECTION_NON_AUTORISEE
        if estPosR(getRiviere(jeu), dx, dy) :
            if deplacementAutorise(getRiviere(jeu), x, y, direction):
                # On a le feu vert, on peut y aller
                res = DIRECTION_OK
    return res


def calculerDirection(jeu, pos):
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
    if getJoueurCourantJ(jeu) is not None:
        jx, jy = getPosJoueurCourant(jeu)
        if not estPosR(getRiviere(jeu), jx, jy):
            setContenuR(getRiviere(jeu), 0, getColDepart(getRiviere(jeu)), getRepresentation(getJoueurCourantJ(jeu)))

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
    :return: tuple(bool,string).
    """
    est_stable=True
    chaine_bilan =""

    # Si il y a des trucs dans les courants
    if getMinADeplacer(getRiviere(jeu)) != (-1,-1):
        elemx,elemy = getMinADeplacer(getRiviere(jeu))
        direction = getCourantR(getRiviere(jeu), elemx, elemy)

        print('Gestion Courants : deplacement de ({0},{1}) vers {2} demandé'.format(elemx, elemy, direction))
        deplacer(getRiviere(jeu), elemx, elemy, direction)
        est_stable=False

        #si ça a fait arriver un joueur
        winner = joueurArrive(getRiviere(jeu))
        if winner is not None:
            chaine_bilan = 'Le joueur {0} est arrive'.format(winner)
            ajouterClassement(jeu, winner)

    # On passe au joueur suivant si il y en a un.
    if getNbJoueursJ(jeu)>0:
        joueurSuivantJ(jeu)

    else:
        chaine_bilan = "La partie est terminée"
        viderJoueurs(getJoueursJ(jeu))

    return (est_stable, chaine_bilan)


def jouerDirection(jeu, direction):
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
    sumstr = ""
    verif = verifDirection(jeu, direction)
    enleverCoupsRestants(jeu) # De base, le joueur depense un point de deplacement
    jx, jy= getPosJoueurCourant(jeu)

    # Si on peut se deplacer
    if verif == DIRECTION_OK:

        # Si le joueur decide de ne pas bouger
        if direction == 'X':
            sumstr = "le joueur {0} renonce à ses derniers déplacements".format(getNom(getJoueurCourantJ(jeu)))

            enleverTousCoupsRestants(jeu)


        # Si le joueur bouge
        else:

            deplacer(getRiviere(jeu),jx, jy,direction)

            # si il est arrivé :
            if joueurArrive(getRiviere(jeu)) is not None:

                sumstr = "Le joueur {0} est arrivé".format(getNom(getJoueurCourantJ(jeu)))
                print("Le tour se termine car le joueur {0} est arrivé".format(getNom(getJoueurCourantJ(jeu))))
                ajouterClassement(jeu, getNom(getJoueurCourantJ(jeu)))
                joueurSuivantJ(jeu)

    elif verif == DIRECTION_NON_AUTORISEE :
        sumstr="Attention direction incorrecte"

    elif verif == PAS_UNE_DIRECTION:
        sumstr = "Ceci n'est pas une direction"


    # On vire tout ce qui se trouve sur l'arrivée
    viderArrivee(getRiviere(jeu))

    return sumstr


###########################  TESTS

if __name__ == '__main__':

    game = Jeu('./data/', 'joueurs.txt', 'riviere1.txt')

    print('ajouterJoueurJ() : ')
    for (nom, representation) in getJoueursPossibles(getJoueursJ(game)).items():
        ajouterJoueurJ(game, Joueur(nom, representation, True))

    initJeu(game)

    print('TEST des fonctions de jeu.py : ')

    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
    print('Jeu() : ', game)

    print('getRiviere() : ', getRiviere(game))
    print('getClassement() : ', getClassement(game))
    print('getJoueursJ() : ', getJoueursJ(game))
    print('getNbjoueursJ() : ', getNbJoueursJ(game))
    print('getJoueurCourantJ() : ', getJoueurCourantJ(game))
    print('getPosJoueur() : ', getPosJoueur(game,getJoueurCourantJ(game) ))
    print('AVANT PLACEMENT => getPosJoueurCourant() : ', getPosJoueurCourant(game))
    print('positionerJoueurCourant()')
    positionerJoueurCourant(game)
    print('APRES PLACEMENT => getPosJoueurCourant() : ', getPosJoueurCourant(game))

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')


