import sys

from controleurs import tournoi_controleur
from vues import vue_principale


def choix_menu():
    while True:
        entree = input("==>")
        match entree:
            case '1':
                return '1'
            case '2':
                return '2'
            case ('X' | 'x'):
                return 'x'
            case '9':
                return '9'
            case _:
                print("Entrée non valide")


class MenuPrincipalControleur:
    """
    Contrôleur du menu principal
    """

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
            # self.aller_vers_continuer_tournoi()
            pass
        if entree == 'x':
            self.controleur_actuel = FermerApplication()
            self.aller_vers_fermer_application()
        if entree == '9':
            self.controleur_actuel = tournoi_controleur.TournoiTest()
            self.aller_vers_tournoi_test()

    def aller_vers_creer_tournoi(self):
        return self.controleur_actuel()

    # def aller_vers_continuer_tournoi(self):
    #     return self.controleur_actuel()

    def aller_vers_fermer_application(self):
        return self.controleur_actuel()

    def aller_vers_tournoi_test(self):
        return self.controleur_actuel()


class FermerApplication:
    def __call__(self):
        print("______Fermeture______")
        sys.exit()
