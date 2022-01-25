import names
import random

from modeles.joueur import Joueur
from modeles.tour import Tour


def genere_resultats_alea(tour):
    """
    Génère des résultats aléatoires pour les matchs d'un tour
    :param tour: un tour du tournoi
    :type tour: object Tour
    """
    for match in tour.liste_matchs:
        resultat_j1 = random.randint(0, 2)
        if resultat_j1 == 0:
            resultat_j2 = 1
        elif resultat_j1 == 1:
            resultat_j2 = 0
        else:
            resultat_j1 = resultat_j2 = 0.5
        match.ajouter_resultats_match(resultat_j1, resultat_j2)


def cree_joueurs_alea(nombre):
    """
    Créer x joueurs aléatoires
    :param nombre: nombre de joueurs à créer
    :type nombre: int
    """
    liste_joueurs = []
    for i in range(nombre):
        liste_joueurs.append(Joueur(names.get_last_name(),
                                    names.get_first_name(),
                                    random.randint(1300, 2900)))
    return liste_joueurs


class Tests:
    def __init__(self, tournoi):
        self.tournoi = tournoi

    def affichage_tour(self, tour):
        """
        :type tour: object Tour
        """
        print("==========================================================")
        print(tour)
        print()
        # Affiche les infos des joueurs
        for joueur in self.tournoi.liste_joueurs:
            print(joueur)
        print()
        # Affiche les infos des matchs du tour 1
        for match in tour.liste_matchs:
            print(match)
        print()

    def run(self):
        self.tournoi.liste_joueurs = cree_joueurs_alea(8)
        # Créer un tour
        tour_1 = Tour("Tour n°1", "15 janvier", "17:11", self.tournoi)
        # Générer les paires et les premiers matchs
        tour_1.generer_paires_initial()
        genere_resultats_alea(tour_1)

        # Affiche les infos du tournoi
        print(self.tournoi)
        self.affichage_tour(tour_1)

        # Créer un tour 2
        tour_2 = Tour("Tour n°2", "15 janvier", "17:30", self.tournoi)
        tour_2.generer_paires()
        genere_resultats_alea(tour_2)
        self.affichage_tour(tour_2)

        # Créer un tour 3
        tour_3 = Tour("Tour n°3", "15 janvier", "17:40", self.tournoi)
        tour_3.generer_paires()
        genere_resultats_alea(tour_3)
        self.affichage_tour(tour_3)
