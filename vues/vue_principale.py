class Rapports:
    """
    Classe pour l'affichage des rapports du tournoi
    """

    def __init__(self, tournoi):
        self.tournoi = tournoi

    def preparation_premier_tour(self, tour):
        print("==================PREPARATION TOUR==================")
        print(tour)
        print("==================INFOS JOUEURS==================")
        for joueur in self.tournoi.joueurs:
            print(joueur)
        # Affiche les infos des matchs du tour 1
        for match in tour.liste_matchs:
            print(match)
            print("   ------------------------------------")
        print()

    def preparation_tour(self, tour):
        print("==================PREPARATION TOUR==================")
        print(tour)
        # Affiche les infos des matchs du tour
        for match in tour.liste_matchs:
            print(match)
            print("       --------------------------")
        print()

    def resultats_tour(self, tour):
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
              f"Description: {self.tournoi.descritpion},\n"
              f"Nombre de tours: {self.tournoi.nombre_tours},\n"
              f"Nombre de joueurs: {len(self.tournoi.joueurs)},\n"
              f"VAINQUEUR(S) DU TOURNOI: {vainqueur}")

    def details_resultats(self):
        liste_joueurs = sorted(self.tournoi.joueurs,
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
              "2) Voir le détails de joueurs -------------------\n"
              "-------------------------------------------------\n"
              "x) Quitter --------------------------------------\n"
              "-------------------------------------------------\n"
              "")
