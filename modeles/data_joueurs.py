class DataJoueurs:
    """
    Représente la base de données des joueurs
    """

    def __init__(self):
        self.data_liste_joueurs = []

    def __str__(self):
        return f"----Base de données des joueurs----,\n" \
               f"nombre total de joueurs: {len(self.data_liste_joueurs)}"

    def __repr__(self):
        return str(self)
