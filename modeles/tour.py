from collections import deque
from datetime import datetime

from modeles.match import Match


class Tour:
    """
    Représente un tour de tournoi
    """

    def __init__(self, nom=None, date_debut=None, date_fin=None,
                 liste_match=None):
        """
        Initialise une instance de Tour.
        :param nom: nom du tour
        :type nom: str
        :param date_debut: date de début du tour
        :type date_debut: str
        :param heure_debut: heure de début du tour
        :type heure_debut: str
        :param tournoi: le tournoi dont fait partit le tour
        :type tournoi: object Tournoi
        """
        if liste_match is None:
            liste_match = []
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.liste_matchs = liste_match

    def __str__(self):
        if self.date_debut is not None:
            return f"----Tour: {self.nom}----,\n" \
                   f"Date de début: {self.date_debut},\n" \
                   f"Nombre de matchs: {len(self.liste_matchs)}\n"
        else:
            return f"----Tour: {self.nom}----,\n" \
                   f"Nombre de matchs: {len(self.liste_matchs)}\n"

    def __repr__(self):
        return str(self)

    def creer_instance_tour(self, tour_sauve):
        """
        Méthode d'instanciation de tour à partir de données texte
        :type tour_sauve: dict
        """
        nom = tour_sauve['Nom']
        date_debut = tour_sauve['Debut']
        date_fin = tour_sauve['Fin']
        liste_matchs = tour_sauve['Liste matchs']
        return Tour(nom, date_debut, date_fin, liste_matchs)

    def save(self):
        """
        Méthode de sérialisation du modèle tour
        """
        tour_sauve = {'Nom': self.nom,
                      'Debut': self.date_debut,
                      'Fin': self.date_fin,
                      'Liste matchs': self.liste_matchs}
        return tour_sauve

    def trier_joueurs_classement(self, tournoi):
        """
        Méthode pour trier les joueurs par classement.
        :return: liste des joueurs triée
        :rtype: list
        """
        liste_joueurs = tournoi.liste_joueurs
        liste_joueurs_tri = sorted(liste_joueurs,
                                   key=lambda joueur: joueur.classement,
                                   reverse=True)
        return liste_joueurs_tri

    def generer_paires_initial(self, tournoi):
        """
        Méthode pour générer les paires (match) du premier tour
        """
        liste_joueurs_tri = self.trier_joueurs_classement(tournoi)
        nombre_joueurs = len(liste_joueurs_tri)
        liste_joueurs_sup = liste_joueurs_tri[:int(nombre_joueurs / 2)]
        liste_joueurs_inf = liste_joueurs_tri[int(nombre_joueurs / 2):]
        for joueur_1, joueur_2 in zip(liste_joueurs_sup, liste_joueurs_inf):
            match = Match(joueur_1, joueur_2)
            self.liste_matchs.append(match)

    def trier_joueurs_points(self, tournoi):
        """
        Méthode pour trier les joueurs par points (par classement si égalité)
        """
        liste_joueurs_tmp = self.trier_joueurs_classement(tournoi)
        liste_joueurs_tri = sorted(liste_joueurs_tmp, key=lambda
            joueur: joueur.total_points_tournoi, reverse=True)
        return liste_joueurs_tri

    def generer_paires(self, tournoi):
        """
        Méthode pour générer les paires (matchs) des tours suivants
        """
        queue = deque(self.trier_joueurs_points(tournoi))
        while len(queue) > 1:
            joueur_1 = queue.popleft()
            joueur_2 = None
            for i in range(0, len(queue)):
                joueur_2_tmp = queue[i]
                if joueur_2_tmp not in joueur_1.adversaires:
                    joueur_2 = joueur_2_tmp
                    queue.remove(joueur_2_tmp)
                    break
                else:
                    if i == (len(queue) - 1):
                        joueur_2 = queue.popleft()
                    else:
                        continue

            match = Match(joueur_1, joueur_2)
            self.liste_matchs.append(match)

    def lancement_tour(self):
        """
        Méthode pour lancer le tour et enregistrer la date et l'heure de début
        """
        while True:
            entree = input(f"Appuyer sur Y pour lancer le TOUR '{self.nom}' "
                           f"==> ")
            if entree in ('Y', 'y'):
                date_heure = datetime.now()
                self.date_debut = date_heure.strftime("%H:%M:%S - %d/%m/%Y")
                print("\n=== Début du tour===\n"
                      f"DATE: {self.date_debut}\n")
                break

    def fin_tour(self):
        """
        Méthode pour finir le tour et enregistrer la date et l'heure de début
        """
        date_heure = datetime.now()
        self.date_fin = date_heure.strftime("%H:%M:%S - %d/%m/%Y")
        print("\n=== Fin du tour===\n"
              f"DATE: {self.date_fin}\n")
