class Match:
    """
    Représente un match d'échecs
    """

    def __init__(self, joueur_1, joueur_2):
        """
        Initialise une instance de Match
        :param joueur_1: L'objet joueur 1
        :type joueur_1: obj [Joueur]
        :param joueur_2: L'objet joueur 2
        :type joueur_2: obj [Joueur]
        """
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.resultat_joueur_1 = None
        self.resultat_joueur_2 = None
        self.liste_1 = []
        self.liste_2 = []
        self.resultat_match = ()
        self.joueur_1.adversaires.append(self.joueur_2)
        self.joueur_2.adversaires.append(self.joueur_1)

    def __str__(self):
        return f"----Match: {self.joueur_1.nom_famille} VS " \
               f"{self.joueur_2.nom_famille}----,\n" \
               f"Résultat J1: {self.resultat_joueur_1},\n" \
               f"Résultat J2: {self.resultat_joueur_2}"

    def __repr__(self):
        return str(self)

    def ajouter_resultats_match(self, resultat_joueur_1, resultat_joueur_2):
        """
        Méthode pour ajouter les résultats d'un match
        :param resultat_joueur_1: défaite: 0, nul: 0.5 ou victoire: 1
        :type resultat_joueur_1: float
        :param resultat_joueur_2:défaite: 0, nul: 0.5 ou victoire: 1
        :type resultat_joueur_2: float
        """
        self.resultat_joueur_1 = resultat_joueur_1
        self.joueur_1.total_points_tournoi += resultat_joueur_1
        self.resultat_joueur_2 = resultat_joueur_2
        self.joueur_2.total_points_tournoi += resultat_joueur_2
        self.liste_1 = [self.joueur_1, self.resultat_joueur_1]
        self.liste_2 = [self.joueur_2, self.resultat_joueur_2]
        self.resultat_match = (self.liste_1, self.liste_2)
