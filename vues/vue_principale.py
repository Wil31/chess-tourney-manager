from datetime import datetime

from modeles import modele_tournoi


class TournoiRapports:
    """
    Classe pour l'affichage des rapports du tournoi
    """

    def __init__(self, tournoi):
        """
        :type tournoi: object Tournoi
        """
        self.tournoi = tournoi

    def preparation_premier_tour(self, tour):
        """
        :type tour: object Tour
        """
        print("==================PREPARATION TOUR==================")
        print(tour)
        print("==================INFOS JOUEURS==================")
        for joueur in self.tournoi.ids_joueurs:
            print(joueur)
        # Affiche les infos des matchs du tour 1
        for match in tour.liste_matchs:
            print(match)
            print("   ------------------------------------")

    def preparation_tour(self, tour):
        """
        :type tour: object Tour
        """
        print("\n==================PREPARATION TOUR==================")
        print(tour)
        # Affiche les infos des matchs du tour
        for match in tour.liste_matchs:
            print(match)
            print("       --------------------------")
        print()

    def resultats_tour(self, tour):
        """
        :type tour: object Tour
        """
        print(f"\n========RESULTATS {tour.nom}========")
        for match in tour.liste_matchs:
            print(match)
            print("       --------------------------")
        print()

    def resulats_tournoi(self):
        vainqueur = self.tournoi.vainqueur_tournoi()
        print(f"\n========RESULTATS {self.tournoi.nom}========"
              f"Lieu: {self.tournoi.lieu},\n"
              f"Date: {self.tournoi.date},\n"
              f"Contrôle du temps: {self.tournoi.controle_temps},\n"
              f"Description: {self.tournoi.description},\n"
              f"Nombre de tours: {self.tournoi.nombre_tours},\n"
              f"Nombre de joueurs: {len(self.tournoi.ids_joueurs)},\n"
              f"VAINQUEUR(S) DU TOURNOI: {vainqueur}")

    def details_resultats(self):
        liste_joueurs = sorted(self.tournoi.ids_joueurs,
                               key=lambda joueur: joueur.classement)
        liste_joueurs_par_points = sorted(liste_joueurs,
                                          key=lambda
                                              joueur:
                                          joueur.total_points_tournoi,
                                          reverse=True)
        print("=====DETAIL RESULATS JOUEURS=====")
        for joueur in liste_joueurs_par_points:
            print(f"----Joueur: {joueur.nom_famille} {joueur.prenom}----,\n"
                  f"Classement: {joueur.classement},\n"
                  f"Total points tournoi: {joueur.total_points_tournoi}\n")


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
              "1) Nouveau tournoi ------------------------------\n"
              "2) Reprendre un tournoi -------------------------\n"
              "3) Créer un joueur ------------------------------\n"
              "4) Liste des joueurs ----------------------------\n"
              "5) Modifier classement joueur -------------------\n"
              "-------------------------------------------------\n"
              "x) Quitter --------------------------------------\n"
              "-------------------------------------------------\n"
              "9) Tournoi TEST ---------------------------------\n"
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
        print("-------------------------------------------------\n"
              "-- Choisir une option: --------------------------\n"
              "1) Modifier un autre joueur ---------------------\n"
              "-------------------------------------------------\n"
              "x) Retour menu ----------------------------------\n"
              "-------------------------------------------------\n"
              "")


class AfficheJoueurRapport:
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
        for joueur in liste_joueurs:
            print(
                f"Nom --- Prénom --- Date de naissance\n"
                f"{joueur.nom_famille} {joueur.prenom} "
                f"{joueur.date_naissance}\n"
                f"Sexe: {joueur.sexe} - Classement : {joueur.classement}")
        print("Appuyer sur une touche pour revenir")
        input()

    def par_classement(self, liste_joueurs):
        for joueur in liste_joueurs:
            print(f"Classement :{joueur.classement} - {joueur.nom_famille}"
                  f" {joueur.prenom} - {joueur.date_naissance} - "
                  f"{joueur.sexe}")
        print("Appuyer sur une touche pour revenir")
        input()


class AfficheTournoi:
    """
    Affiche les tournois existants non commencés dans la DB
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


class AfficheTour:
    def affiche_tour(self, tour_name, liste_matchs):
        print(f"-------------{tour_name}---------------\n")
        for match in liste_matchs:
            print(match)
            print()

    def affiche_date_heure_tour(self):
        print()
        input("Appuyez sur une touche pour commencer le tour\n")
        date_heure = datetime.now()
        debut = date_heure.strftime("%H:%M:%S - %d/%m/%Y")
        print(f"Début du tour : {debut}\n")
        input("Appuyez sur une touche lorsque le tour est terminé\n")
        date_heure = datetime.now()
        fin = date_heure.strftime("%H:%M:%S - %d/%m/%Y")
        print(f"Fin du tour : {fin}\n")
        return debut, fin
