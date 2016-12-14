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
    pass

# retourne l'indice dans la liste du joueur qui porte ce nom
# -1 si le nom n'est pas dans la liste
def indiceJoueur(joueurs,nom):
    pass

# ajoute un nouveau joueur dans la liste à partir du nom et de son type
# la représentation est déduite de la structure joueursPossibles
def ajouterJoueur(joueurs,nom,humain=True):
    pass
        
# Cette fonction retire un joueur de la liste
# si le joueur n'y était pas elle ne fait rien
# Attention si la liste devient vide il n'y a plus de joueur courant
def retirerJoueur(joueurs,nom):
    pass

# Cette fonction retourne le nombre de joueurs dans la liste
def getNbJoueurs(joueurs):
    pass

# retourne la structure joueursPossibles associée à la liste de joueurs
def getJoueursPossibles(joueurs):
    pass

# Cette fonction retourne le joueur courant
def getJoueurCourant(joueurs):
    pass

# Cette fonction retourne le nom du joueur numéro i (dans l'ordre où ils ont été ajoutés)
# i est un entier entre 0 et le nombre de joueurs de la liste -1
def getJoueurI(joueurs,i):
    pass

# retourne le joueurs de la liste qui correspond à la représentation
def getJoueurRep(joueurs,representation):
    pass

# vide la liste de joueurs
def viderJoueurs(joueurs):
    pass

# passe au joueur suivant
def joueurSuivant(joueurs):
    pass

