import sys

from vues import vue_principale
from controleurs import tournoi_controleur
from controleurs import joueur_controleur
from modeles import data_tournois
from modeles import data_joueurs

class MenuPrincipalControleur:
    def __init__(self):
        self.vues = vue_principale.MenuPrincipal()
        self.controleur_actuel = None
        self.data_joueurs = data_joueurs.DataJoueurs()

    def __call__(self):
        self.vues.afficher_menu()
        entree = self.choix_menu()

        if entree == '1':
            self.controleur_actuel = MenuTournoiControleur()
            self.aller_vers_menu_tournoi()
        if entree == '2':
            self.controleur_actuel = MenuJoueurControleur()
            self.aller_vers_menu_joueurs()
        if entree == 'x':
            self.controleur_actuel = FermerApplication()
            self.aller_vers_fermer_application()
        if entree == '9':
            self.controleur_actuel = tournoi_controleur.TournoiTest()
            self.aller_vers_tournoi_test()

    def aller_vers_menu_tournoi(self):
        return self.controleur_actuel()

    def aller_vers_menu_joueurs(self):
        return self.controleur_actuel()

    def aller_vers_fermer_application(self):
        return self.controleur_actuel()

    def aller_vers_tournoi_test(self):
        return self.controleur_actuel()

    def choix_menu(self):
        while True:
            entree = input("==>")
            if entree == '1':
                return '1'
            if entree == '2':
                return '2'
            if entree == 'X' or 'x':
                return 'x'
            if entree == '9':
                return '9'
            else:
                print("Entrée non valide")


class MenuTournoiControleur(MenuPrincipalControleur):
    def __init__(self):
        super().__init__()
        self.creer_tournoi = tournoi_controleur.CreerTournoiControleur()
        self.menu_principal_controleur = MenuPrincipalControleur()

    def __call__(self, *args, **kwargs):
        self.vues.afficher_menu_gestion_tournoi()
        while True:
            entree = input("==>")
            if entree == '1':
                self.controleur_actuel = self.creer_tournoi()
            if entree == 'x' or 'X':
                self.controleur_actuel = self.menu_principal_controleur()
            else:
                print("Entrée non valide")


class MenuJoueurControleur(MenuPrincipalControleur):
    def __init__(self):
        super().__init__()
        self.creer_joueur = joueur_controleur.CreerJoueurControleur()
        self.menu_principal_controleur = MenuPrincipalControleur()

    def __call__(self, *args, **kwargs):
        self.vues.afficher_menu_gestion_joueurs()
        while True:
            entree = input("==>")
            if entree == '1':
                self.controleur_actuel = self.creer_joueur()
            if entree == '2':
                print(self.data_joueurs)
                print(self.data_joueurs.data_liste_joueurs)
            if entree == 'x' or 'X':
                self.controleur_actuel = self.menu_principal_controleur()
            else:
                print("Entrée non valide")


class FermerApplication:
    def __call__(self):
        print("______Fermeture______")
        sys.exit()
