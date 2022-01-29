from vues import vue_principale
from modeles import modele_match


class Tour:
    """
    Représente un tour de tournoi
    """

    def __init__(self, nom_tour=None, date_debut=None, date_fin=None,
                 liste_matchs_termines=None):
        """
        Initialise une instance de Tour.
        :param nom_tour: nom du tour
        :type nom_tour: str
        :param date_debut: date et heure de début du tour
        :type date_debut: str
        :param date_fin: date et heure de fin du tour
        :type date_fin: str
        :param liste_matchs_termines: liste des matchs terminés du tour
        :type liste_matchs_termines: list
        """
        self.nom_tour = nom_tour
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.liste_matchs_termines = liste_matchs_termines
        self.liste_tours = []

    def __str__(self):
        return f"----Tour: {self.nom_tour}----,\n" \
               f"Date de début: {self.date_debut},\n" \
               f"Date de fin: {self.date_fin}\n"

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
        liste_matchs_termines = tour_sauve['Liste matchs termines']
        return Tour(nom, date_debut, date_fin, liste_matchs_termines)

    def serialise(self):
        """
        Méthode de sérialisation du modèle tour
        """
        tour_serialise = {'Nom': self.nom_tour,
                          'Debut': self.date_debut,
                          'Fin': self.date_fin,
                          'Liste matchs termines': self.liste_matchs_termines}
        return tour_serialise

    def lancer_tour(self, liste_joueurs_trie_autre, tournoi_obj):
        """
        Méthode de contrôle du tour avec entrée des résultats de matchs
        """
        self.nom_tour = f"Tour {len(tournoi_obj.liste_tours) + 1}"
        self.vue = vue_principale.AfficheTour()
        self.liste_tours = []
        self.liste_matchs_termines = []
        liste_joueurs_trie = liste_joueurs_trie_autre.copy()

        while len(liste_joueurs_trie) > 0:
            match = modele_match.Match(self.nom_tour, liste_joueurs_trie[0],
                                       liste_joueurs_trie[1])
            modele_match.Match.NUMERO_MATCH += 1
            self.liste_tours.append(match)
            del liste_joueurs_trie[0:2]

        self.vue.affiche_tour(self.nom_tour, self.liste_tours)

        self.date_debut, self.date_fin = self.vue.affiche_date_heure_tour()

        for match in self.liste_tours:
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
                            resultat_joueur_1 = 0
                            resultat_joueur_2 = 1
                        case '1':
                            resultat_joueur_1 = 1
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

        return Tour(self.nom_tour, self.date_debut, self.date_fin,
                    self.liste_matchs_termines)
