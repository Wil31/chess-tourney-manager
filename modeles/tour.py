from modeles.match import Match


class Tour:
    """
    Représente un tour de tournoi
    """

    def __init__(self, nom, date_debut, heure_debut, tournoi):
        """
        Initialise une instance de Tour.
        :param nom: nom du tour
        :type nom: str
        :param date_debut: date de début du tour
        :type date_debut: str
        :param heure_debut: heure de début du tour
        :type heure_debut: str
        :param tournoi: le tournoi dont fait partit le tour
        :type tournoi: object [Tournoi]
        """
        self.nom = nom
        self.date_debut = date_debut
        self.heure_debut = heure_debut
        self.tournoi = tournoi
        self.date_fin = None
        self.heure_fin = None
        self.liste_matchs = []

    def __str__(self):
        return f"----Tour: {self.nom}----,\n" \
               f"date de début: {self.date_debut},\n" \
               f"heure de début: {self.heure_debut},\n" \
               f"nombre de matchs: {len(self.liste_matchs)}"

    def __repr__(self):
        return str(self)

    def trier_joueurs_classement(self):
        """
        Méthode pour trier les joueurs par classement.
        :return: liste des joueurs triée
        :rtype: list
        """
        liste_joueurs = self.tournoi.joueurs
        liste_joueurs_tri = sorted(liste_joueurs,
                                   key=lambda joueur: joueur.classement,
                                   reverse=True)
        return liste_joueurs_tri

    def generer_paires_initial(self):
        liste_joueurs_tri = self.trier_joueurs_classement()
        nombre_joueurs = len(liste_joueurs_tri)
        liste_joueurs_sup = liste_joueurs_tri[0:int(nombre_joueurs/2)]
        liste_joueurs_inf = liste_joueurs_tri[int(nombre_joueurs/2):]
        for joueur_1, joueur_2 in zip(liste_joueurs_sup, liste_joueurs_inf):
            match = Match(joueur_1, joueur_2)
            self.liste_matchs.append(match)

    def trier_joueurs_points(self):
        pass

    def generer_paires(self):
        pass
