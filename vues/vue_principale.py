from datetime import datetime
from operator import attrgetter

from modeles import modele_tournoi, modele_joueur, modele_match


class MenuPrincipal:
    """
    Classe pour l'affichage des menus principaux
    """

    def afficher_menu(self):
        """
        Menu principal
        """
        print("-------------------------------------------------\n"
              "------- GESTIONNAIRE DE TOURNOI D'ÉCHECS --------\n"
              "-------------------------------------------------\n"
              "-- Choisir une option: --------------------------\n"
              "1) Créer nouveau tournoi ------------------------\n"
              "2) Lancer un nouveau tournoi --------------------\n"
              "3) Reprendre un tournoi en cours ----------------\n"
              "-------------------------------------------------\n"
              "4) Créer un joueur ------------------------------\n"
              "5) Liste des joueurs ----------------------------\n"
              "6) Modifier classement joueur -------------------\n"
              "-------------------------------------------------\n"
              "x) Quitter --------------------------------------\n"
              "-------------------------------------------------\n"
              "")

    def menu_fin_tournoi(self):
        """
        Menu de fin de tournoi
        """
        print("-------------------------------------------------\n"
              "--------------- TOURNOI TERMINE -----------------\n"
              "-------------------------------------------------\n"
              "-- Choisir une option: --------------------------\n"
              "1) Voir résumé et vainqueur(s) du tournoi -------\n"
              "2) Voir le détail des joueurs -------------------\n"
              "-------------------------------------------------\n"
              "x) Retour menu ----------------------------------\n"
              "-------------------------------------------------\n"
              "")

    def menu_fin_modif_classement(self):
        """
        Menu après modification du classement d'un joueur
        """
        print("-------------------------------------------------\n"
              "-- Choisir une option: --------------------------\n"
              "1) Modifier un autre joueur ---------------------\n"
              "-------------------------------------------------\n"
              "x) Retour menu ----------------------------------\n"
              "-------------------------------------------------\n"
              "")


class AfficheJoueurRapport:
    """
    Classe pour l'affichage des joueurs enregistrés
    """

    def __call__(self):
        print("-------------------------------------------------\n"
              "------------------INFOS JOUEURS------------------\n"
              "-------------------------------------------------\n"
              "-- Choisir une option: --------------------------\n"
              "1) Joueurs par ordre alphabétique ---------------\n"
              "2) Joueurs par classement -----------------------\n"
              "-------------------------------------------------\n"
              "x) Retour menu ----------------------------------\n"
              )

    def par_alphabetique(self, liste_joueurs):
        """
        Affichage des joueurs enregistrés par ordre alphabétique
        """
        for joueur in liste_joueurs:
            print(
                f"Nom --- Prénom --- Date de naissance\n"
                f"{joueur.nom_famille} {joueur.prenom} "
                f"{joueur.date_naissance}\n"
                f"Sexe: {joueur.sexe} - Classement : {joueur.classement}")
        print("Appuyer sur une touche pour revenir")
        input()

    def par_classement(self, liste_joueurs):
        """
        Affichage des joueurs enregistrés par classement
        """
        for joueur in liste_joueurs:
            print(f"Classement :{joueur.classement} - {joueur.nom_famille}"
                  f" {joueur.prenom} - {joueur.date_naissance} - "
                  f"{joueur.sexe}")
        print("Appuyer sur une touche pour revenir")
        input()


class AfficheTournoi:
    """
    Affiche les tournois existants non commencés de la DB
    :return True si un tournoi existe et n'est pas commencé
    """

    def __call__(self, *args, **kwargs):
        tournoi_non_commence = False
        tournoi_db = modele_tournoi.TOURNOI_DB
        for tournoi in tournoi_db:
            if not tournoi['Tours']:
                print(f"ID Tournoi: {tournoi.doc_id}, Nom: "
                      f"{tournoi['Nom du tournoi']}, Lieu: {tournoi['Lieu']}")
                tournoi_non_commence = True
        return tournoi_non_commence


class AfficheChargementTournoi:
    """
    Affiche les tournois non terminés de la DB
    :return True si un tournoi existe et n'est pas terminé
    """

    def __call__(self):
        tournoi_non_termine = False
        tournoi_db = modele_tournoi.TOURNOI_DB
        for tournoi in tournoi_db:
            if tournoi["Tours"]:
                if len(tournoi["Tours"]) < int(tournoi["Nombre de tours"]):
                    print(f"ID Tournoi: {tournoi.doc_id}, Nom: "
                          f"{tournoi['Nom du tournoi']}, Lieu: {tournoi['Lieu']}")
                    tournoi_non_termine = True
        return tournoi_non_termine


class AfficheTour:
    """
    Affiche les informations pendant les tours
    """

    def __init__(self):
        self.match = modele_match.Match()

    def affiche_tour(self, tour_name, liste_matchs):
        """
        Affiche le nom du tour et la liste des matchs du tour
        :type tour_name: object Tour
        :param liste_matchs: liste d'objets Match
        :type liste_matchs: list
        """
        print(f"-------------{tour_name}---------------\n")
        for match in liste_matchs:
            print(match)

    def affiche_date_heure_tour(self):
        """
        Affiche le signal pour débuter et terminer un tour.
        Enregistre l'heure de début et de fin du tour.
        """
        print("Appuyez sur Y pour commencer le tour")
        while True:
            entree = input('==> ')
            if entree.upper() == 'Y':
                break
            else:
                print("Appuyez sur Y pour commencer le tour")
        date_heure = datetime.now()
        debut = date_heure.strftime("%H:%M:%S - %d/%m/%Y")
        print(f"Début du tour : {debut}\n")

        print("Appuyez sur Y lorsque le tour est terminé")
        while True:
            entree = input('==> ')
            if entree.upper() == 'Y':
                break
            else:
                print("Appuyez sur Y lorsque le tour est terminé")
        date_heure = datetime.now()
        fin = date_heure.strftime("%H:%M:%S - %d/%m/%Y")
        print(f"Fin du tour : {fin}\n")
        return debut, fin


class ResultatsTournoi:
    """
    Affiche les résultats du tournoi et le classement des joueurs par points.
    """

    def __call__(self, tournoi_obj, liste_joueurs_tournoi):
        print("-------------------------------------------------\n"
              "-------------- RESULTATS TOURNOI ----------------\n"
              "-------------------------------------------------\n")
        for tour in tournoi_obj.liste_tours:
            print(tour)

            for match in tour.liste_matchs_termines:
                joueur_1 = modele_joueur.JOUEUR_DB.get(doc_id=match[0][0])
                score_joueur_1 = match[0][1]
                joueur_2 = modele_joueur.JOUEUR_DB.get(doc_id=match[1][0])
                score_joueur_2 = match[1][1]
                print(f"{joueur_1['Nom']} {joueur_1['Prenom']} VS "
                      f"{joueur_2['Nom']} {joueur_2['Prenom']}\n"
                      f"RESULTAT: {score_joueur_1} VS {score_joueur_2}\n")

        liste_joueurs_tournoi.sort(
            key=attrgetter("total_points_tournoi"), reverse=True)
        print("Classement des joueurs par points: ")
        for joueur in liste_joueurs_tournoi:
            print(
                f"{joueur.nom_famille} {joueur.prenom} - Score: "
                f"{joueur.total_points_tournoi}")

        print("Appuyez sur X pour revenir au menu...")
        choix_valide = False
        while not choix_valide:
            choix = input("==> ")
            if choix.upper() == 'X':
                choix_valide = True
            else:
                print("Entrée invalide, X pour revenir")
