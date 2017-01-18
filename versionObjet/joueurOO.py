class Joueur(object):
    """"""

    def __init__(self, nom, representation, humain=True):
        self.nom = nom
        self.representation = representation
        self.humain = humain

    def get_nom(self):
        return self.nom

    def get_representation(self):
        return self.representation

    def est_humain(self):
        return self.humain


########################################################################################################################
# TESTS
########################################################################################################################

if __name__ == '__main__':
    l_joueurs = [Joueur('Luc', 'L', True),
                 Joueur('Marc', 'M', True),
                 Joueur('Jean', 'J', True),
                 Joueur('AI', 'A', False)]

    for joueur in l_joueurs:
        descriptif = "Le joueur {0} sera représenté par le symbole '{1}'. Il est manipulé par {2}".format(
            joueur.get_nom(), joueur.get_representation(),
            ('un humain' * joueur.est_humain() + 'une IA' * (not joueur.est_humain())))
        print(descriptif)
