from tinydb import TinyDB

from controleurs import menu_controleur
from vues import vue_principale

JOUEUR_DB = TinyDB("modeles/joueur_db.json")


class Joueur:
    """
    Représente un joueur d'échecs
    """

    def __init__(
        self,
        nom_famille=None,
        prenom=None,
        classement=None,
        date_naissance=None,
        sexe=None,
        total_points_tournoi=0,
        id_joueur=0,
    ):
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
        :param total_points_tournoi: score total du joueur
        :type total_points_tournoi: int
        :param id_joueur: ID du joueur
        :type id_joueur: int
        """
        self.nom_famille = nom_famille
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.total_points_tournoi = total_points_tournoi
        self.id_joueur = id_joueur

    def __str__(self):
        return f"{self.nom_famille} {self.prenom}"

    def __repr__(self):
        return f"{self.nom_famille} {self.prenom}, Classé : {self.classement}"

    def creer_instance_joueur(self, joueur_sauve):
        """
        Méthode d'instanciation de joueur à partir de données texte
        :param joueur_sauve: dictionnaire contenant les informations d'un joueur
        :type joueur_sauve: dict
        :return: un Joueur
        :rtype: object Joueur
        """
        nom_famille = joueur_sauve["Nom"]
        prenom = joueur_sauve["Prenom"]
        date_naissance = joueur_sauve["Date de naissance"]
        sexe = joueur_sauve["Sexe"]
        classement = joueur_sauve["Classement"]
        total_points_tournoi = joueur_sauve["Score"]
        id_joueur = joueur_sauve["ID joueur"]
        return Joueur(
            nom_famille,
            prenom,
            classement,
            date_naissance,
            sexe,
            total_points_tournoi,
            id_joueur,
        )

    def serialise(self):
        """
        Méthode de sérialisation du modèle joueur
        :return: dictionnaire contenant les informations d'un joueur
        :rtype: dict
        """
        joueur_sauve = {
            "Nom": self.nom_famille,
            "Prenom": self.prenom,
            "Date de naissance": self.date_naissance,
            "Sexe": self.sexe,
            "Classement": self.classement,
            "Score": self.total_points_tournoi,
            "ID joueur": self.id_joueur,
        }
        return joueur_sauve

    def ajout_db(self, infos_joueur):
        """
        Méthode d'ajout d'un joueur à la DB joueur
        :param infos_joueur: liste des informations du joueur
        :type infos_joueur: list
        """
        joueur = Joueur(
            infos_joueur[0],
            infos_joueur[1],
            infos_joueur[2],
            infos_joueur[3],
            infos_joueur[4],
        )
        id_joueur = JOUEUR_DB.insert(joueur.serialise())
        JOUEUR_DB.update({"ID joueur": id_joueur}, doc_ids=[id_joueur])

    def modifier_classement_joueur(self):
        """
        Méthode pour modifier le classement d'un joueur de la BD joueur
        """
        joueur_db = JOUEUR_DB
        self.menu_principal_controleur = menu_controleur.MenuPrincipalControleur()
        self.vues = vue_principale.MenuPrincipal()

        for player in joueur_db:
            print(
                f"Joueur ID: {player.doc_id} - {player['Nom']} "
                f"{player['Prenom']} - Classement : {player['Classement']}"
            )

        id_joueur = None
        id_valide = False
        while not id_valide:
            id_joueur = input("Entrer l'ID à modifier: ")
            if (
                id_joueur.isdigit()
                and int(id_joueur) > 0
                and int(id_joueur) <= len(joueur_db)
            ):
                id_valide = True
            else:
                print("Entrez une ID de joueur existant")

        classement = None
        classement_valide = False
        while not classement_valide:
            classement = input("Entrez nouveau classement: ")
            if classement.isdigit() and int(classement) > 0:
                classement_valide = True
            else:
                print("Le classement doit être un nombre positif")

        joueur_cible = joueur_db.get(doc_id=int(id_joueur))
        joueur_cible["Classement"] = classement
        joueur_db.update({"Classement": int(classement)}, doc_ids=[int(id_joueur)])
        print(
            f"Joueur: {joueur_cible['Nom']} {joueur_cible['Prenom']} "
            f"a été modifié, Classement = {joueur_cible['Classement']}\n"
        )
        while True:
            self.vues.menu_fin_modif_classement()
            entree = input("==> ")
            match entree:
                case "1":
                    self.modifier_classement_joueur()
                case ("X" | "x"):
                    self.menu_principal_controleur()
                case _:
                    print("Entrée non valide")
