from modeles.tour import Tour
from modeles.tournoi import Tournoi
from tests.tests import Tests
from tests.tests import cree_joueurs_alea
from controleurs import menu_controleur, joueur_controleur


class LancerTournoiControleur:
    """
    Lance un tournoi deja créé.
    """

    def __init__(self, tournoi):
        self.tournoi_actuel = tournoi

    def __call__(self):
        premier_tour = Tour(self.tournoi_actuel, "Tour N°1")
        premier_tour.generer_paires_initial()

        test = Tests(self.tournoi_actuel)
        test.affichage_tour(premier_tour)

        entree_valide = False
        while not entree_valide:
            entree = input("Appuyez sur Y pour entrer les résultats ==> ")
            if entree == "Y" or entree == 'y':
                entree_valide = True
                for match in premier_tour.liste_matchs:
                    resultat_valide = False
                    while not resultat_valide:
                        resultat_joueur_1 = input(
                            f"Entrez le résultat de {match.joueur_1.nom_famille}"
                            f" {match.joueur_1.prenom}\n"
                            f"1: Victoire | 0: Défaire | N: Match nul ==> ")
                        match resultat_joueur_1:
                            case '0':
                                resultat_joueur_2 = 1
                                resultat_valide = True
                            case '1':
                                resultat_joueur_2 = 0
                                resultat_valide = True
                            case ('n' | 'N'):
                                resultat_joueur_2 = resultat_joueur_1 = 0.5
                                resultat_valide = True
                    match.ajouter_resultats_match(float(resultat_joueur_1),
                                                  float(resultat_joueur_2))
            else:
                pass
            test.affichage_tour(premier_tour)

        # for tour in range(int(self.tournoi_actuel.nombre_tours) - 1):
        #     print(f"tour {tour}")
        #     ce_tour = Tour(self.tournoi_actuel, f"Tour N°{tour + 1}")

    def ajout_nom(self):
        nom_joueur = None
        nom_valide = False
        while not nom_valide:
            nom_joueur = input("Entrez le NOM du tour: ")
            if nom_joueur != '' and nom_joueur.isalpha():
                nom_valide = True
            else:
                print("Un nom est obligatoire!")
        return nom_joueur

    def selection_tournoi(self):
        """
        Affiche les tournois existants et retourne un tournoi choisi.
        """
        pass


class RapportTournoi:
    """
    Affiche la liste des tournois.
    Affiche les détails d'un tournoi: les tours, les matchs et les joueurs (par
    ordre alphabétique ou par classement).
    """


class CreerTournoiControleur:
    """
    Créé un nouveau tournoi
    """

    def __init__(self):
        self.menu_principal_controleur = menu_controleur.MenuPrincipalControleur()
        self.infos_tournoi = []
        self.objet_tournoi = None
        self.creer_joueur_controleur = joueur_controleur.CreerJoueurControleur()
        # self.lancer_tournoi_controleur = LancerTournoiControleur()

    def __call__(self):
        print("Creation de tournoi...\n")
        self.infos_tournoi.append(self.ajout_nom())
        self.infos_tournoi.append(self.ajout_lieu())
        self.infos_tournoi.append(self.ajout_date())
        self.infos_tournoi.append(self.ajout_controle_temps())
        self.infos_tournoi.append(self.ajout_description())
        self.infos_tournoi.append(self.ajout_nombre_tours())
        self.infos_tournoi.append(self.ajout_nombre_joueurs())
        entree = input("Joueurs aléatoires? (Y/N) ==> ")
        if entree == 'y' or entree == 'Y':
            self.infos_tournoi.append(self.ajout_joueurs_aleatoires())
        else:
            self.infos_tournoi.append(self.ajout_joueurs())
        self.objet_tournoi = self.creer_obj_tournoi(self.infos_tournoi)
        print("==========================================================\n"
              "==================Nouveau tournoi créé !==================\n"
              "==========================================================\n"
              "")
        print(self.objet_tournoi)
        print("Voulez-vous maintenant lancer ce tournoi ?")
        choix_valide = False
        while not choix_valide:
            choix = input("Y / N ? ==> ")
            if choix == 'y' or choix == 'Y':
                lancer_tournoi = LancerTournoiControleur(self.objet_tournoi)
                lancer_tournoi()
                choix_valide = True
            if choix == 'n' or choix == 'N':
                # il faudrait enregistrer le tournoi pour plus tard
                choix_valide = True

    def creer_obj_tournoi(self, infos_tournoi):
        """
        Créé un objet Tournoi à partir de la liste infos_tournoi
        :type infos_tournoi: list
        """
        tournoi = Tournoi(infos_tournoi[0], infos_tournoi[1], infos_tournoi[2],
                          infos_tournoi[3], infos_tournoi[4], infos_tournoi[5],
                          infos_tournoi[6], infos_tournoi[7])
        return tournoi

    def ajout_nom(self):
        nom_tournoi = None
        nom_valide = False
        while not nom_valide:
            nom_tournoi = input("Entrez le NOM du Tournoi: ")
            if nom_tournoi != '':
                nom_valide = True
            else:
                print("Un nom est obligatoire!")
        return nom_tournoi

    def ajout_lieu(self):
        lieu_tournoi = None
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
            if mois.isdigit() and (0 < int(mois) < 13):
                mois_valide = True
                date.append(mois)
            else:
                print("Entrez un chiffre entre 1 et 12!")

        annee_valide = False
        while not annee_valide:
            annee = input("Entrer l'ANNÉE du Tournoi: ")
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
        entree_valide = False
        while not entree_valide:
            print("Y pour changer / N pour garder 4 tours")
            choix = input("==> ")
            if choix == 'Y' or choix == 'y':
                nombre_tours = input("Entrer un nombre de tours: ")
                if nombre_tours.isdigit() and int(nombre_tours) > 0:
                    entree_valide = True
                else:
                    print("Entrez un nombre entier supérieur à 0!")
            if choix == 'N' or choix == 'n':
                entree_valide = True
            if choix == "":
                print("Veuillez choisir Y/N")
        return nombre_tours

    def ajout_controle_temps(self):
        controle_temps = None
        print("Choisir le contrôle du temps:\n"
              "1) Bullet\n"
              "2) Blitz\n"
              "3) Coup rapide\n")
        while True:
            choix = input("==> ")
            if choix == '1':
                controle_temps = "Bullet"
                break
            if choix == '2':
                controle_temps = "Blitz"
                break
            if choix == '3':
                controle_temps = "Coup rapide"
                break
            else:
                print("Choix invalide!")
                continue
        return controle_temps

    def ajout_description(self):
        print("Entrez la DESCRIPTION du tournoi: ")
        description = input("==> ")
        return description

    def ajout_nombre_joueurs(self):
        nombre_joueurs = None
        entree_valide = False
        while not entree_valide:
            nombre_joueurs = input(
                "Entrez le nombre de participants au tournoi: ")
            if nombre_joueurs.isdigit() and int(nombre_joueurs) > 1 \
                    and (int(nombre_joueurs) % 2) == 0:
                entree_valide = True
            else:
                print("Entrez un nombre pair et positif!")
        return nombre_joueurs

    def ajout_joueurs_aleatoires(self):
        nombre_joueurs = int(self.infos_tournoi[6])
        liste_joueurs = cree_joueurs_alea(nombre_joueurs)
        print(f"{nombre_joueurs} joueurs aléatoires ont été créés")
        return liste_joueurs

    def ajout_joueurs(self):
        nombre_joueurs = int(self.infos_tournoi[6])
        liste_joueurs = []
        for i in range(nombre_joueurs):
            print(f"Création du joueur N°{i + 1}...\n")
            joueur = self.creer_joueur_controleur()
            liste_joueurs.append(joueur)
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
