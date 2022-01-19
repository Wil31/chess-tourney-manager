from modeles.data_joueurs import DataJoueurs


class Joueur:
    """
    Représente un joueur d'échecs
    """

    def __init__(self, nom_famille=None, prenom=None, classement=None,
                 date_naissance=None, sexe=None):
        """
        Initialise une instance de Joueur.
        :param nom_famille: nom du joueur
        :type nom_famille: str
        :param prenom: prenom du joueur
        :type prenom: str
        :param date_naissance: date de naissance du joueur
        :type date_naissance: str
        :param sexe: M ou F
        :type sexe: str
        :param classement: nombre positif
        :type classement: int
        """
        self.nom_famille = nom_famille
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.total_points_tournoi = 0
        self.adversaires = []
        self.data_joueurs = DataJoueurs()

    def __str__(self):
        return f"----Joueur: {self.nom_famille} {self.prenom}----,\n" \
               f"date de naissance: {self.date_naissance},\n" \
               f"sexe: {self.sexe},\n" \
               f"classement: {self.classement},\n" \
               f"total points: {self.total_points_tournoi}"

    def __repr__(self):
        return str(self)

    def modifier_classement_joueur(self, nouveau_classement):
        """
        Méthode pour modifier le classement d'un joueur
        :param nouveau_classement: nombre positif
        :type nouveau_classement: int
        """
        self.classement = nouveau_classement

    def ajout_data_joueur(self, infos_joueur):
        joueur = Joueur(infos_joueur[0], infos_joueur[1], infos_joueur[2],
                        infos_joueur[3], infos_joueur[4])
        self.data_joueurs.data_joueurs.append(joueur)
