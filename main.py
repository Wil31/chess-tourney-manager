import names
import random

from modeles.joueur import Joueur
from modeles.tournoi import Tournoi
from modeles.tour import Tour


def main():
    # Créer le tournoi
    tournoi_test = Tournoi("Tournoi des Rois", "Toulouse", "15 janvier",
                           "Bullet", "Le premier tournoi de 2022")
    # Créer 8 joueurs aléatoires
    for i in range(8):
        tournoi_test.joueurs.append(
            Joueur(names.get_last_name(), names.get_first_name(),
                   random.randint(1, 10)))

    # Créer un tour
    tour_1 = Tour("Tour n°1", "15 janvier", "17:11", tournoi_test)
    # Générer les paires et les premiers matchs
    tour_1.generer_paires_initial()

    # Affiche les infos du tournoi
    print(tournoi_test)
    print()
    print(tour_1)
    print()
    # Affiche les infos des joueurs
    for joueur in tournoi_test.joueurs:
        print(joueur)
    print()
    # Affiche les infos des matchs du tour 1
    for match in tour_1.liste_matchs:
        print(match)


if __name__ == "__main__":
    main()
