# Cette structure de données gère les noms et les représentations des joueurs
# le nom permet de connaitre le nom du fichier qui contient l'image représentant le
# joueur en mode graphique et le caractère représentant le joueur sur la grille

# Cette fonction retourne une nouvelle liste de joueurs vide dont les joueurs possibles
# sont passés en paramètre. Il n'y a pas de joueur courant lorsque la liste est vide
def JoueursPossibles():
    pass

# Cette fonction retourne une nouvelle liste de joueurs vide dont les joueurs possibles
# sont contenus dans un fichier texte. Il n'y a pas de joueur courant lorsque la liste est vide
def lireJoueursPossibles(nomFic):
    pass

# Cette fonction permet d'ajouter un nouveau joueur possible à une liste de joueurs
# nom est une chaine de caractères
# representation est un caractère
def ajouterNom(joueursPossibles,nom,representation):
    pass

# Cette fonction retour,e la liste des noms de joueurs possibles 
# uniquement les noms pas les représentations
def getListeNomsJoueur(joueursPossibles):
    return list(joueursPossibles.keys())

# Cette fonction retourne le nom d'un joueur en fonction de sa représentation
def getNomJoueur(joueursPossibles,representation):
    pass
        
# retourne la representation d'un joueur en fonction de son nom
def getRepresentationJoueur(joueursPossibles,nom):
    pass
