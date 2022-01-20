import sys

from vues import vue_principale
from controleurs import tournoi_controleur
from controleurs import joueur_controleur


def choix_menu():
    while True:
        entree = input("==>")
        if entree == '1':
            return '1'
        if entree == '2':
            return '2'
        if entree == 'X' or entree == 'x':
            return 'x'
        if entree == '9':
            return '9'
        else:
            print("Entrée non valide")


class MenuPrincipalControleur:
    def __init__(self):
        self.vues = vue_principale.MenuPrincipal()
        self.controleur_actuel = None

    def __call__(self):
        self.vues.afficher_menu()
        entree = choix_menu()

        if entree == '1':
            self.controleur_actuel = tournoi_controleur.CreerTournoiControleur()
            self.aller_vers_creer_tournoi()
        if entree == '2':
            self.controleur_actuel = MenuJoueurControleur()
            self.aller_vers_menu_joueurs()
        if entree == 'x':
            self.controleur_actuel = FermerApplication()
            self.aller_vers_fermer_application()
        if entree == '9':
            self.controleur_actuel = tournoi_controleur.TournoiTest()
            self.aller_vers_tournoi_test()

    def aller_vers_creer_tournoi(self):
        return self.controleur_actuel()

    def aller_vers_menu_joueurs(self):
        return self.controleur_actuel()

    def aller_vers_fermer_application(self):
        return self.controleur_actuel()

    def aller_vers_tournoi_test(self):
        return self.controleur_actuel()


class MenuTournoiControleur(MenuPrincipalControleur):
    def __init__(self):
        super().__init__()
        self.creer_tournoi = tournoi_controleur.CreerTournoiControleur()
        self.menu_principal_controleur = MenuPrincipalControleur()
        self.lancer_tournoi = tournoi_controleur.LancerTournoiControleur()

    def __call__(self, *args, **kwargs):
        self.vues.afficher_menu_gestion_tournoi()
        while True:
            entree = input("==>")
            if entree == '1':
                self.controleur_actuel = self.creer_tournoi()
            if entree == '2':
                print(tournoi_controleur.DATA_TOURNOI)
            if entree == '3':
                self.controleur_actuel = self.lancer_tournoi()
            if entree == 'x' or entree == 'X':
                self.controleur_actuel = self.menu_principal_controleur()


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
                print(joueur_controleur.DATA_JOUEURS)
            if entree == 'x' or entree == 'X':
                self.controleur_actuel = self.menu_principal_controleur()


class FermerApplication:
    def __call__(self):
        print("______Fermeture______")
        sys.exit()
