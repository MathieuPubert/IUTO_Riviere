from riviere import *
from listeJoueurs import *
import random

# ces constantes servent à gérer le code retour de la fonction verifDirection
DIRECTION_OK=0
PAS_UNE_DIRECTION=1
DIRECTION_NON_AUTORISEE=2

# Cette fonction créer un nouveau jeu
# prefixe est le préfixe où est installer le jeu
# ficJoueurs est le nom du fichier où se trouvent les joueurs connus
# ficRiviere est le nom du fichier qui contient la configuration initiale de la rivière
# La fonction créée un nouveau jeu, initiatise le classement et la participants 
# à vide mais avec comme liste de joueurs connus celle contenu dans le fichier passé en
# paramètre
# la structure de jeu conserve aussi le nombre de coups restants au joueur courant
# Cette fonction initialise aussi le générateur de nombres aléatoires
def Jeu(prefixe,ficJoueurs,ficRiviere):
    pass

# permet de placer le premier joueur sur la case départ et de lui attribuer
# un nombre de déplacements entre 1 et 5
def initJeu(jeu):
    pass

# permet d'obtenir la rivière du jeu
def getRiviere(jeu):
    pass

# permet d'obtenir le classement actuel
def getClassement(jeu):
    pass

# permet d'ajouter un nouveau joueur participant à la course
def ajouterJoueurJ(jeu,joueur):
    pass

# permet d'obtenir la liste des joueurs participant à la course
def getJoueursJ(jeu):
    pass

# permet de connaitre le nombre joueurs participant à la course
def getNbJoueursJ(jeu):
    pass

# permet de connaitre le nom du joueur courant
def getJoueurCourantJ(jeu):
    pass


# permet de retrouver la position d'un joueur sur le plateau en fonction de son nom
def getPosJoueur(jeu,joueur):
    pass

# permet de retrouver la position du joueur courant
def getPosJoueurCourant(jeu):
    pass

# permet le nombre de coups restants au joueur courant
def getNbCoupsRestants(jeu):
    pass
   
# permet d'enlever un coup au joueur courant
def enleverCoupsRestants(jeu):
    pass

# permet d'enlever tout les coups restant du joueur courant
def enleverTousCoupsRestants(jeu):
    pass
    
# permet d'ajouter un joueur au classement et de l'enlever à la liste des 
# joueurs participants à la course
def ajouterClassement(jeu,nomJoueur):
    pass

# permet de passer au joueur suivant. Cela implique de lui attribuer un nombre
# de coups à jouer et de le positionner sur la case de départ s'il n'est pas sur
# le plateau
def joueurSuivantJ(jeu):
    pass

# permet de verifier si la direction passée en paramètre est bien une position
# et si c'est le cas, que le joueur courant a le droit de se déplacer dans cette
# direction
# Le code retour de cette fonction est soit PAS_UNE_DIRECTION, soit DIRECTION_NON_AUTORISEE
# soit DIRECTION_OK
def verifDirection(jeu,direction):
    pass

# pos est un couple de la forme (lig,col) représentant une position sur la grille
# la fonction calcule la direction entre la position du joueur courant et la position pos
# le résultat de la fonction est la direction telle que définie dans le fichier case.py ou
# le caractère 'W' si la position du joueur courant et pos ne sont pas deux cases voisines
# de la grille
def calculerDirection(jeu,pos):
    pass

# permet de verifier si le joueur courant est sur la grille
# si ce n'est pas le cas, on le place sur la case départ
def positionerJoueurCourant(jeu):
    pass

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
