from datetime import datetime
from vues import vue_principale
from modeles import modele_match


class Tour:
    """
    Représente un tour de tournoi
    """

    def __init__(self, nom=None, date_debut=None, date_fin=None,
                 liste_matchs=None):
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
        self.liste_matchs_termines = None
        if liste_matchs is None:
            liste_matchs = []
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.liste_matchs = liste_matchs

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

    def lancement_tour(self, liste_joueurs_trie, tournoi_obj):
        """
        Méthode pour lancer le tour et enregistrer la date et l'heure de début
        """
        self.nom = f"Tour {len(tournoi_obj) + 1}"
        self.vue = vue_principale.AfficheTour()
        self.liste_matchs_termines = []

        self.date_debut, self.date_fin = self.vue.affiche_date_heure_tour()

        while len(liste_joueurs_trie) > 0:
            match = modele_match.Match(self.nom, liste_joueurs_trie[0],
                                       liste_joueurs_trie[1])
            self.liste_matchs.append(match)
            del liste_joueurs_trie[0:2]

        self.vue.affiche_tour(self.nom, self.liste_matchs)

        for match in self.liste_matchs:
            resultat_valide = False
            while not resultat_valide:
                resultat_joueur_1 = input(
                    f"Entrez le résultat de {match.joueur_1.nom_famille}"
                    f" {match.joueur_1.prenom}\n"
                    f"1: Victoire | 0: Défaire | N: Match nul "
                    f"==> ")
                resultat_joueur_2 = None
                if resultat_joueur_1 in ('0', '1', 'n', 'N'):
                    resultat_valide = True
                    match resultat_joueur_1:
                        case '0':
                            resultat_joueur_2 = 1
                        case '1':
                            resultat_joueur_2 = 0
                        case ('n' | 'N'):
                            resultat_joueur_2 = resultat_joueur_1 = 0.5
                    match.resultat_joueur_1 = resultat_joueur_1
                    match.joueur_1.total_points_tournoi += resultat_joueur_1
                    match.resultat_joueur_2 = resultat_joueur_2
                    match.joueur_2.total_points_tournoi += resultat_joueur_2
                else:
                    continue
            self.liste_matchs_termines.append(
                ([match.joueur_1.id_joueur, match.resultat_joueur_1],
                 [match.joueur_2.id_joueur, match.resultat_joueur_2]))

        return Tour(self.nom, self.date_debut, self.date_fin,
                    self.liste_matchs_termines)

    def fin_tour(self):
        """
        Méthode pour finir le tour et enregistrer la date et l'heure de début
        """
        date_heure = datetime.now()
        self.date_fin = date_heure.strftime("%H:%M:%S - %d/%m/%Y")
        print("\n=== Fin du tour===\n"
              f"DATE: {self.date_fin}\n")
