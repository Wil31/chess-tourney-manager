import sys

from controleurs import tournoi_controleur, joueur_controleur
from vues import vue_principale
from modeles import modele_joueur


def choix_menu():
    while True:
        entree = input("==>")
        match entree:
            case '1':
                return '1'
            case '2':
                return '2'
            case '3':
                return '3'
            case '4':
                return '4'
            case '5':
                return '5'
            case '6':
                return '6'
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
        self.modele_joueur = modele_joueur.Joueur()
        self.controleur_actuel = None

    def __call__(self):
        self.vues.afficher_menu()
        entree = choix_menu()

        if entree == '1':
            self.controleur_actuel = tournoi_controleur.CreerTournoiControleur()
            self.aller_vers_creer_tournoi()
        if entree == '2':
            self.controleur_actuel = tournoi_controleur.LancerTournoiControleur()
            self.aller_vers_lancer_tournoi()
        if entree == '3':
            self.controleur_actuel = tournoi_controleur.LancerTournoiControleur()
            self.aller_vers_reprendre_tournoi()
        if entree == '4':
            self.controleur_actuel = joueur_controleur.CreerJoueurControleur()
            self.aller_vers_creer_joueur()
        if entree == '5':
            self.controleur_actuel = joueur_controleur.JoueurRapport()
            self.aller_vers_rapport_joueur()
        if entree == '6':
            self.controleur_actuel = self.modele_joueur.modifier_classement_joueur()
            self.aller_vers_modifier_classement_joueur()
        if entree == 'x':
            self.controleur_actuel = FermerApplication()
            self.aller_vers_fermer_application()
        if entree == '9':
            self.controleur_actuel = tournoi_controleur.TournoiTest()
            self.aller_vers_tournoi_test()

    def aller_vers_creer_tournoi(self):
        return self.controleur_actuel()

    def aller_vers_lancer_tournoi(self):
        return self.controleur_actuel()

    def aller_vers_reprendre_tournoi(self):
        return self.controleur_actuel.chargement_tournoi()

    def aller_vers_creer_joueur(self):
        return self.controleur_actuel()

    def aller_vers_rapport_joueur(self):
        return self.controleur_actuel()

    def aller_vers_modifier_classement_joueur(self):
        return self.controleur_actuel()

    def aller_vers_fermer_application(self):
        return self.controleur_actuel()

    def aller_vers_tournoi_test(self):
        return self.controleur_actuel()


class FermerApplication:
    def __call__(self):
        print("______Fermeture______")
        sys.exit()
