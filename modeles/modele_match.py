class Match:
    """
    Représente un match d'échecs
    """
    NUMERO_MATCH = 1

    def __init__(self, nom_match=None, joueur_1=None, joueur_2=None,
                 resultat_joueur_1=None, resultat_joueur_2=None):
        """
        Initialise une instance de Match
        :param nom_match: nom du match
        :type nom_match: str
        :param joueur_1: L'objet joueur 1
        :type joueur_1: obj [Joueur]
        :param joueur_2: L'objet joueur 2
        :type joueur_2: obj [Joueur]
        :param resultat_joueur_1: résultat du joueur 1
        :type resultat_joueur_1: int
        :param resultat_joueur_2: résultat du joueur 2
        :type resultat_joueur_2: int
        """
        self.nom_match = nom_match
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.resultat_joueur_1 = resultat_joueur_1
        self.resultat_joueur_2 = resultat_joueur_2

    def __str__(self):
        if self.resultat_joueur_1 is not None and self.resultat_joueur_2 is not None:
            infos_match = f"Match: {self.joueur_1.nom_famille} " \
                          f"{self.joueur_1.prenom}" \
                          f" VS {self.joueur_2.nom_famille} " \
                          f"{self.joueur_2.prenom}\n"
            match self.resultat_joueur_1:
                case 1:
                    gagnant = f"VICTOIRE: {self.joueur_1.nom_famille} " \
                              f"{self.joueur_1.prenom}"
                    return infos_match + gagnant
                case 0:
                    gagnant = f"VICTOIRE: {self.joueur_2.nom_famille} " \
                              f"{self.joueur_2.prenom}"
                    return infos_match + gagnant
                case 0.5:
                    return infos_match + "MATCH NUL"
        else:
            return f"Match à jouer: {self.joueur_1.nom_famille}" \
                   f" {self.joueur_1.prenom} " \
                   f"VS {self.joueur_2.nom_famille} {self.joueur_2.prenom}"

    def __repr__(self):
        return str(self)
