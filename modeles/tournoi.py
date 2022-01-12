class Tournoi:
    """
    Représente un tournoi d'échecs
    """

    def __init__(self, nom, lieu, date, controle_temps, description,
                 nombre_tours=4):
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
        """
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.controle_temps = controle_temps
        self.descritpion = description
        self.nombre_tours = nombre_tours
        self.joueurs = []
        self.tournees = []

    def __str__(self):
        return f"----Tournoi: {self.nom}----,\n" \
               f"lieu: {self.lieu},\n" \
               f"date: {self.date},\n" \
               f"contrôle du temps: {self.controle_temps},\n" \
               f"description: {self.descritpion},\n" \
               f"nombre de tours: {self.nombre_tours},\n" \
               f"nombre de joueurs: {len(self.joueurs)},\n" \
               f"tour en cours: {len(self.tournees)}"

    def __repr__(self):
        return str(self)
