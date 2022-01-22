from controleurs import menu_controleur
from modeles.joueur import Joueur


class RapportJoueurs:
    """
    Affiche la liste des joueurs enregistrés.
    Trie par ordre alphabétique ou par classement.
    """


class CreerJoueurControleur:
    """
    Créé un nouveau joueur
    """

    def __init__(self):
        self.menu_principal_controleur = menu_controleur.MenuPrincipalControleur()
        self.infos_joueur = []
        self.objet_joueur = None

    def creer_obj_joueur(self):
        """
        Créé puis retourne un objet joueur
        """
        self.infos_joueur.append(self.ajout_nom())
        self.infos_joueur.append(self.ajout_prenom())
        self.infos_joueur.append(self.ajout_classement())
        self.infos_joueur.append(self.ajout_anniversaire())
        self.infos_joueur.append(self.ajout_sexe())
        self.objet_joueur = Joueur(self.infos_joueur[0], self.infos_joueur[1],
                        self.infos_joueur[2], self.infos_joueur[3],
                        self.infos_joueur[4])
        print("==========================================================\n"
              "===============Nouveau joueur enregistré !================\n"
              "==========================================================\n"
              "")
        return self.objet_joueur

    def ajout_nom(self):
        nom_joueur = None
        nom_valide = False
        while not nom_valide:
            nom_joueur = input("Entrez le NOM du joueur: ")
            if nom_joueur != '' and nom_joueur.isalpha():
                nom_valide = True
            else:
                print("Un nom est obligatoire!")
        return nom_joueur

    def ajout_prenom(self):
        prenom_joueur = None
        prenom_valide = False
        while not prenom_valide:
            prenom_joueur = input("Entrez le PRENOM du joueur: ")
            if prenom_joueur != '' and prenom_joueur.isalpha():
                prenom_valide = True
            else:
                print("Un prénom est obligatoire!")
        return prenom_joueur

    def ajout_anniversaire(self):
        date = []

        jour_valide = False
        while not jour_valide:
            jour = input("Entrez le JOUR de naissance: ")
            if jour.isdigit() and (0 < int(jour) < 32):
                jour_valide = True
                date.append(jour)
            else:
                print("Entrez un chiffre entre 1 et 31!")

        mois_valide = False
        while not mois_valide:
            mois = input("Entrez le MOIS de naissance: ")
            if mois.isdigit() and (0 < int(mois) < 13):
                mois_valide = True
                date.append(mois)
            else:
                print("Entrez un chiffre entre 1 et 12!")

        annee_valide = False
        while not annee_valide:
            annee = input("Entrez l'ANNÉE de naissance: ")
            if annee.isdigit() and len(annee) == 4:
                annee_valide = True
                date.append(annee)
            else:
                print("Entrez un nombre à 4 chiffres!")

        return f"{date[0]}/{date[1]}/{date[2]}"

    def ajout_sexe(self):
        while True:
            choix = input("Entrez les sexe: F ou M: ")
            if choix == 'M' or choix == 'm':
                sexe = 'M'
                break
            if choix == 'F' or choix == 'f':
                sexe = 'F'
                break
            else:
                print("Entrez un choix F ou M!")
        return sexe

    def ajout_classement(self):
        while True:
            classement = input("Entrez l'ELO du joueur: ")
            if classement.isdigit() and (1000 < int(classement) < 3000):
                return classement
            else:
                print("Entrez un ELO entre 1000 et 3000!")
