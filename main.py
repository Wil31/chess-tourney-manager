from tests.tests import Tests
from modeles.tournoi import Tournoi


def main():
    # Créer le tournoi
    tournoi_rois = Tournoi("Tournoi des Rois", "Toulouse", "16 janvier",
                           "Bullet", "Le premier tournoi de 2022")

    tournoi_test = Tests(tournoi_rois)
    tournoi_test.run()


if __name__ == "__main__":
    main()
