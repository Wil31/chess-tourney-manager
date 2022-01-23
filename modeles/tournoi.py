class Tournoi:
    """
    Modèle de tournoi d'échecs
    """

    def __init__(self, nom=None, lieu=None, date=None, controle_temps=None,
                 description=None, nombre_tours=None, nombre_joueurs=None,
                 joueurs=None):
        """
        Initialise une instance de Tournoi.
        :param nom: nom du tournoi
        :type nom: str
        :param lieu: lieu du tournoi
        :type lieu: str
        :param date: date du tournoi, plusieurs jours possible
        :type date: str
        :param controle_temps: bullet, blitz ou coup rapide
        :type controle_temps: str
        :param description: description du tournoi
        :type description: str
        :param nombre_tours: 4 tours par défaut
        :type nombre_tours: int
        :param nombre_joueurs: nombre de joueurs participants
        :type nombre_joueurs: int
        :param joueurs: liste des objets joueurs participants
        :type joueurs: list [Joueur]
        """
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.controle_temps = controle_temps
        self.descritpion = description
        self.nombre_tours = nombre_tours
        self.nombre_joueurs = nombre_joueurs
        self.joueurs = joueurs
        self.tournees = []
        self.matchs_joues = []

    def __str__(self):
        return f"----Tournoi: {self.nom}----,\n" \
               f"Lieu: {self.lieu},\n" \
               f"Date: {self.date},\n" \
               f"Contrôle du temps: {self.controle_temps},\n" \
               f"Description: {self.descritpion},\n" \
               f"Nombre de tours: {self.nombre_tours},\n" \
               f"Nombre de joueurs: {len(self.joueurs)},\n" \
               f"Tour en cours: {len(self.tournees)}\n"

    def __repr__(self):
        return str(self)

    def vainqueur_tournoi(self):
        """
        Retourne le vainqueur du tournoi, plusieurs si égalité des points.
        Si plusieurs: ils sont classés du moins bon ELO au meilleur.
        """
        liste_joueurs = self.joueurs
        liste_joueurs_tri = sorted(liste_joueurs,
                                   key=lambda joueur: joueur.classement)
        liste_joueurs_par_points = sorted(liste_joueurs_tri,
                                          key=lambda
                                              joueur:
                                          joueur.total_points_tournoi,
                                          reverse=True)
        points = liste_joueurs_par_points[0].total_points_tournoi
        liste_vainqueurs = [v for v in liste_joueurs_par_points if
                            v.total_points_tournoi == points]
        if len(liste_vainqueurs) == 1:
            vainqueur = f"{liste_vainqueurs[0].nom_famille} " \
                        f"{liste_vainqueurs[0].prenom}"
        else:
            vainqueur = "Égalité: "
            for joueur in liste_vainqueurs:
                vainqueur += f"{joueur.nom_famille} {joueur.prenom}, "
        return vainqueur
