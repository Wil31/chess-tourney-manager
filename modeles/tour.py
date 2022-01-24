from modeles.match import Match
from collections import deque


class Tour:
    """
    Représente un tour de tournoi
    """

    def __init__(self, tournoi, nom=None, date_debut=None, heure_debut=None):
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
        self.nom = nom
        self.date_debut = date_debut
        self.heure_debut = heure_debut
        self.tournoi = tournoi
        self.date_fin = None
        self.heure_fin = None
        self.liste_matchs = []

    def __str__(self):
        if self.date_debut is not None and self.heure_debut is not None:
            return f"----Tour: {self.nom}----,\n" \
                   f"Date de début: {self.date_debut},\n" \
                   f"Heure de début: {self.heure_debut},\n" \
                   f"Nombre de matchs: {len(self.liste_matchs)}\n"
        else:
            return f"----Tour: {self.nom}----,\n" \
                   f"Nombre de matchs: {len(self.liste_matchs)}\n"

    def __repr__(self):
        return str(self)

    def trier_joueurs_classement(self):
        """
        Méthode pour trier les joueurs par classement.
        :return: liste des joueurs triée
        :rtype: list
        """
        liste_joueurs = self.tournoi.joueurs
        liste_joueurs_tri = sorted(liste_joueurs,
                                   key=lambda joueur: joueur.classement,
                                   reverse=True)
        return liste_joueurs_tri

    def generer_paires_initial(self):
        """
        Méthode pour générer les paires (match) du premier tour
        """
        liste_joueurs_tri = self.trier_joueurs_classement()
        nombre_joueurs = len(liste_joueurs_tri)
        liste_joueurs_sup = liste_joueurs_tri[:int(nombre_joueurs / 2)]
        liste_joueurs_inf = liste_joueurs_tri[int(nombre_joueurs / 2):]
        for joueur_1, joueur_2 in zip(liste_joueurs_sup, liste_joueurs_inf):
            match = Match(joueur_1, joueur_2)
            self.liste_matchs.append(match)

    def trier_joueurs_points(self):
        """
        Méthode pour trier les joueurs par points (par classement si égalité)
        """
        liste_joueurs_tmp = self.trier_joueurs_classement()
        liste_joueurs_tri = sorted(liste_joueurs_tmp, key=lambda
            joueur: joueur.total_points_tournoi, reverse=True)
        return liste_joueurs_tri

    def generer_paires(self):
        """
        Méthode pour générer les paires (matchs) des tours suivants
        """
        queue = deque(self.trier_joueurs_points())
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
                    if i == (len(queue)-1):
                        joueur_2 = queue.popleft()
                    else:
                        continue

            match = Match(joueur_1, joueur_2)
            self.liste_matchs.append(match)
            self.tournoi.matchs_joues.append(match)
