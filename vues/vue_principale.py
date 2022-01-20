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

    def afficher_menu_gestion_tournoi(self):
        """
        Menu gestion des tournois
        """
        print("-------------------------------------------------\n"
              "----------------- MENU TOURNOI ------------------\n"
              "-------------------------------------------------\n"
              "-- Choisir une option: --------------------------\n"
              "1) Créer un tournoi -----------------------------\n"
              "2) Afficher les tournois en cours ---------------\n"
              "3) Lancer un tournoi ----------------------------\n"
              "-------------------------------------------------\n"
              "x) Retour menu principal ------------------------\n"
              "-------------------------------------------------\n"
              "")

    def afficher_menu_gestion_joueurs(self):
        """
        Menu gestion des joueurs
        """
        print("-------------------------------------------------\n"
              "------------------ MENU JOUEUR ------------------\n"
              "-------------------------------------------------\n"
              "-- Choisir une option: --------------------------\n"
              "1) Créer un joueur ------------------------------\n"
              "2) Afficher liste des joueurs -------------------\n"
              "3) Mettre à jour classement ---------------------\n"
              "-------------------------------------------------\n"
              "x) Retour menu principal ------------------------\n"
              "-------------------------------------------------\n"
              "")
