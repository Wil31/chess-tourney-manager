import sys

from vues import vue_principale
from controleurs.tournoi_controleur import TournoiTest, CreerTournoiControleur


class MenuManager:
    def __init__(self):
        self.vues = vue_principale.MenuPrincipal()
        self.choix = None

    def __call__(self):
        self.vues.afficher_menu()
        entry = self.choix_menu()

        if entry == '1':
            self.choix = CreerTournoiControleur()
            self.aller_vers_creer_tournoi()
        if entry == 'x':
            self.choix = FermerApplication()
            self.aller_vers_fermer_application()
        if entry == '9':
            self.choix = TournoiTest()
            self.aller_vers_tournoi_test()

    def aller_vers_creer_tournoi(self):
        return self.choix()

    def aller_vers_fermer_application(self):
        return self.choix()

    def aller_vers_tournoi_test(self):
        return self.choix()

    def choix_menu(self):
        while True:
            entry = input("==>")
            if entry == '1':
                return '1'
            if entry == 'x':
                return 'x'
            if entry == '9':
                return '9'
            else:
                print("Entrée non valide")


class FermerApplication:
    def __call__(self):
        print("______Fermeture______")
        sys.exit()
