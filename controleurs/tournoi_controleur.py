from modeles.tournoi import Tournoi
from tests.tests import Tests
from tests.tests import cree_joueurs_alea
from controleurs import menu_controleur


class LancerTournoiControleur:
    def __init__(self):
        pass


class CreerTournoiControleur:
    def __init__(self):
        self.menu_principal_controleur = menu_controleur.MenuPrincipalControleur()
        self.infos_tournoi = []

    def __call__(self, *args, **kwargs):
        self.infos_tournoi.append(self.ajout_nom())
        self.infos_tournoi.append(self.ajout_lieu())
        self.infos_tournoi.append(self.ajout_date())
        self.infos_tournoi.append(self.ajout_controle_temps())
        self.infos_tournoi.append(self.ajout_description())
        self.infos_tournoi.append(self.ajout_nombre_tours())
        self.infos_tournoi.append(self.ajout_joueurs())
        self.menu_principal_controleur()
        print("==========================================================\n"
              "==================Nouveau tournoi créé !==================\n"
              "==========================================================\n"
              "")

    def ajout_nom(self):
        nom_valide = False
        while not nom_valide:
            nom_tournoi = input("Entrez le NOM du Tournoi: ")
            if nom_tournoi != '':
                nom_valide = True
            else:
                print("Un nom est obligatoire!")
        return nom_tournoi

    def ajout_lieu(self):
        lieu_valide = False
        while not lieu_valide:
            lieu_tournoi = input("Entrer le LIEU du Tournoi: ")
            if lieu_tournoi != '':
                lieu_valide = True
            else:
                print("Un lieu est obligatoire!")
        return lieu_tournoi

    def ajout_date(self):
        date = []

        jour_valide = False
        while not jour_valide:
            jour = input("Entrer le JOUR du Tournoi: ")
            if jour.isdigit() and (0 < int(jour) < 32):
                jour_valide = True
                date.append(jour)
            else:
                print("Entrez un chiffre entre 1 et 31!")

        mois_valide = False
        while not mois_valide:
            mois = input("Entrer le MOIS du Tournoi: ")
            if mois.isdigit() and (0 < int(mois) < 12):
                mois_valide = True
                date.append(mois)
            else:
                print("Entrez un chiffre entre 1 et 12!")

        annee_valide = False
        while not annee_valide:
            annee = input("Entrer l'ANNEE du Tournoi: ")
            if annee.isdigit() and len(annee) == 4:
                annee_valide = True
                date.append(annee)
            else:
                print("Entrez un nombre à 4 chiffres!")

        return f"{date[0]}/{date[1]}/{date[2]}"

    def ajout_nombre_tours(self):
        nombre_tours = 4
        print("4 tours par défaut.\n"
              "Voulez-vous modifier?")

        nombre_valide = False
        while not nombre_valide:
            print("Y pour changer / N pour garder 4 tours")
            choix = input("==> ")
            if choix == 'Y' or 'y':
                nombre_tours = input("Entrer un nombre de tours: ")
                if nombre_tours.isdigit() and int(nombre_tours) > 0:
                    nombre_valide = True
                else:
                    print("Entrez un nombre entier supérieur à 0!")
            if choix == 'N' or 'n':
                nombre_valide = True
            else:
                print("Veuillez choisir Y/N")
        return nombre_tours

    def ajout_controle_temps(self):
        controle_temps = None
        print("Choisir le contrôle du temps:\n"
              "1) Bullet\n"
              "2) Blitz\n"
              "3) Coup rapide\n")
        choix_valide = False
        while not choix_valide:
            choix = input("==> ")
            if choix == '1':
                controle_temps = "Bullet"
                choix_valide = True
            if choix == '2':
                controle_temps = "Blitz"
                choix_valide = True
            if choix == '3':
                controle_temps = "Coup rapide"
                choix_valide = True
            else:
                print("Choix invalide!")
        return controle_temps

    def ajout_description(self):
        print("Entrez la DESCRIPTION du tournoi: ")
        description = input("==> ")
        return description

    def ajout_joueurs(self):
        liste_joueurs = cree_joueurs_alea(8)
        print("8 Joueurs aléatoires ont été créés")
        return liste_joueurs


class TournoiTest:
    def __init__(self):
        self.menu_principal_controleur = menu_controleur.MenuPrincipalControleur()

    def __call__(self):
        # Créer le tournoi test
        tournoi_rois = Tournoi("Tournoi des Rois", "Toulouse", "16 janvier",
                               "Bullet", "Le premier tournoi de 2022")

        tournoi_test = Tests(tournoi_rois)
        print("ici!!")
        tournoi_test.run()
        self.menu_principal_controleur()
