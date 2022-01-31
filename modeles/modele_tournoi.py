from tinydb import TinyDB

TOURNOI_DB = TinyDB('modeles/tournoi_db.json')


class Tournoi:
    """
    Modèle de tournoi d'échecs
    """

    def __init__(self, nom_tournoi=None, lieu=None, date=None,
                 controle_temps=None, description=None, nombre_tours=None,
                 nombre_joueurs=None, ids_scores_joueurs=None,
                 liste_tours=None, id_tournoi=None):
        """
        Initialise une instance de Tournoi.
        :param nom_tournoi: nom du tournoi
        :type nom_tournoi: str
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
        :param ids_scores_joueurs: dictionnaire des ID et scores des joueurs
        du tournoi
        :type ids_scores_joueurs: dict
        :param liste_tours: liste des object Tour
        :type liste_tours: list
        :param id_tournoi: ID du tournoi
        :type id_tournoi: int
        """
        if ids_scores_joueurs is None:
            ids_scores_joueurs = []
        if liste_tours is None:
            liste_tours = []
        self.nom = nom_tournoi
        self.lieu = lieu
        self.date = date
        self.controle_temps = controle_temps
        self.description = description
        self.nombre_tours = nombre_tours
        self.nombre_joueurs = nombre_joueurs
        self.ids_scores_joueurs = ids_scores_joueurs
        self.liste_tours = liste_tours
        self.id_tournoi = id_tournoi

    def __str__(self):
        return f"----Tournoi: {self.nom}----,\n" \
               f"ID: {self.id_tournoi}\n" \
               f"Lieu: {self.lieu},\n" \
               f"Date: {self.date},\n" \
               f"Contrôle du temps: {self.controle_temps},\n" \
               f"Description: {self.description},\n" \
               f"Nombre de tours: {self.nombre_tours},\n" \
               f"Nombre de joueurs: {len(self.ids_scores_joueurs)},\n"

    def __repr__(self):
        return str(self)

    def creer_instance_tournoi(self, tournoi_sauve):
        """
        Méthode d'instanciation de tournoi à partir de données texte
        :type tournoi_sauve: dict
        """
        nom = tournoi_sauve['Nom du tournoi']
        lieu = tournoi_sauve['Lieu']
        date = tournoi_sauve['Date']
        nombre_tours = tournoi_sauve['Nombre de tours']
        controle_temps = tournoi_sauve['Controle du temps']
        description = tournoi_sauve['Description']
        liste_joueurs = tournoi_sauve["Liste joueurs"]
        nombre_joueurs = tournoi_sauve['Nombre de joueurs']
        tournees = tournoi_sauve["Tours"]
        id_tournoi = tournoi_sauve['ID Tournoi']
        return Tournoi(nom, lieu, date, controle_temps, description,
                       nombre_tours, nombre_joueurs, liste_joueurs, tournees,
                       id_tournoi)

    def serialise(self):
        """
        Méthode de sérialisation du modèle tournoi
        """
        tournoi_serialise = {'Nom du tournoi': self.nom, 'Lieu': self.lieu,
                             'Date': self.date,
                             'Nombre de tours': self.nombre_tours,
                             'Controle du temps': self.controle_temps,
                             'Description': self.description,
                             'Nombre de joueurs': self.nombre_joueurs,
                             'Liste joueurs': self.ids_scores_joueurs,
                             'Tours': self.liste_tours}
        return tournoi_serialise

    def ajout_db(self, infos_tournoi):
        """
        Méthode d'ajout d'un tournoi à la DB tournoi
        :param infos_tournoi: liste des informations du tournoi
        :type infos_tournoi: list
        """
        tournoi = Tournoi(infos_tournoi[0], infos_tournoi[1],
                          infos_tournoi[2], infos_tournoi[3],
                          infos_tournoi[4], infos_tournoi[5],
                          infos_tournoi[6], infos_tournoi[7])
        id_tournoi = TOURNOI_DB.insert(tournoi.serialise())
        TOURNOI_DB.update({"ID Tournoi": id_tournoi}, doc_ids=[id_tournoi])
