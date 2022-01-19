class DataTournois:
    """
    Représente la base de données des tournois
    """

    def __init__(self):
        self.data_tournois = []

    def __str__(self):
        return f"----Base de données des tournois----,\n" \
               f"nombre de tournois dans la base: {len(self.data_tournois)}"

    def __repr__(self):
        return str(self)
