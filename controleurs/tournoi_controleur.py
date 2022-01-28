from controleurs import menu_controleur
from modeles import modele_joueur, modele_tournoi, modele_tour, modele_match
from tests import tests
from vues import vue_principale
from operator import itemgetter
from collections import deque


class LancerTournoiControleur:
    """
    Lance un tournoi deja créé.
    """

    MATCHS_JOUES = []
    TOURS_JOUES = []

    def __init__(self):
        """
        :type tournoi: object Tournoi
        """
        self.affiche_tournoi = None
        self.tournoi = None
        self.tour = modele_tour.Tour()
        self.liste_joueurs_trie = []
        self.menu_principal_controleur = \
            menu_controleur.MenuPrincipalControleur()
        self.vue_resultats = vue_principale.ResultatsTournoi()
        # self.tournoi_rapports = vue_principale.TournoiRapports(
        #     self.tournoi_obj)

    def __call__(self):
        self.tournoi_obj = self.selection_tournoi()
        self.liste_joueurs_trie = self.triage_initial(self.tournoi_obj)
        # for joueur in self.tournoi_actuel.liste_joueurs:
        #     joueur.reset_adversaires()

        self.tournoi_obj.tournees.append(
            self.tour.lancer_tour(self.liste_joueurs_trie, self.tournoi_obj))
        self.sauvegarde_tournoi(self.tournoi_obj)

        for tour in range(int(self.tournoi_obj.nombre_tours) - 1):
            self.liste_joueurs_trie.clear()
            self.liste_joueurs_trie = self.triage_tours_suivants(
                self.tournoi_obj)
            self.tournoi_obj.tournees.append(
                self.tour.lancer_tour(self.liste_joueurs_trie,
                                      self.tournoi_obj))
            self.sauvegarde_tournoi(self.tournoi_obj)

        self.vue_resultats(self.tournoi_obj)
        self.menu_principal_controleur()

    def sauvegarde_tournoi(self, tournoi_obj):

        tournoi_db = modele_tournoi.TOURNOI_DB
        table_tours = tournoi_db.table('tours')

        tour_obj = tournoi_obj.tournees[-1]
        tour_serialise = tour_obj.serialise()
        tour_serialise['Liste matchs'] = tour_obj.liste_matchs_termines

        id_tour = table_tours.insert(tour_serialise)
        LancerTournoiControleur.TOURS_JOUES.append(id_tour)
        tournoi_db.update({'Tours': LancerTournoiControleur.TOURS_JOUES},
                          doc_ids=[tournoi_obj.id_tournoi])

        print("Tournoi sauvegardé, voulez-vous quitter?\n")
        choix_valide = False
        while not choix_valide:
            choix = input("Y/N ==> ")
            if choix.upper() == 'Y':
                choix_valide = True
                self.menu_principal_controleur()
            elif choix.upper() == 'N':
                choix_valide = True
                break
            else:
                print("Entrée invalide (Y/N)")

    def selection_tournoi(self):
        self.affiche_tournoi = vue_principale.AfficheTournoi()
        self.tournoi = modele_tournoi.Tournoi()

        if self.affiche_tournoi():
            choix = None
            id_valide = False
            while not id_valide:
                choix = input("Choisir ID du tournoi ==> ")
                if choix.isdigit() and int(
                        choix) > 0 and int(choix) <= len(
                    modele_tournoi.TOURNOI_DB):
                    id_valide = True
                else:
                    print("Entrez un ID de tournoi valide !")

            tournoi_choisi = modele_tournoi.TOURNOI_DB.get(doc_id=int(choix))
            tournoi_obj = self.tournoi.creer_instance_tournoi(tournoi_choisi)
            return tournoi_obj

        else:
            print("Pas de tournoi non commencé.")
            self.menu_principal_controleur()

    def trier_joueurs_classement(self, tournoi):
        """
        Méthode pour trier les joueurs par classement.
        :return: liste des joueurs triée
        :rtype: list
        """
        self.joueur = modele_joueur.Joueur()
        ids_joueurs = tournoi.ids_joueurs
        liste_joueurs = []

        for id_joueur in ids_joueurs:
            joueur = modele_joueur.JOUEUR_DB.get(doc_id=id_joueur)
            joueur = self.joueur.creer_instance_joueur(joueur)
            liste_joueurs.append(joueur)

        liste_joueurs = sorted(liste_joueurs,
                               key=lambda joueur: joueur.classement,
                               reverse=True)
        return liste_joueurs

    def triage_initial(self, tournoi_obj):
        """
        Méthode pour générer la liste des joueurs trié du premier tour
        """

        liste_joueurs = self.trier_joueurs_classement(tournoi_obj)
        nombre_joueurs = len(liste_joueurs)
        liste_joueurs_sup = liste_joueurs[:int(nombre_joueurs / 2)]
        liste_joueurs_inf = liste_joueurs[int(nombre_joueurs / 2):]
        liste_joueurs_tri = []
        for joueur_1, joueur_2 in zip(liste_joueurs_sup, liste_joueurs_inf):
            liste_joueurs_tri.append(joueur_1)
            liste_joueurs_tri.append(joueur_2)
            self.MATCHS_JOUES.append({joueur_1.id_joueur, joueur_2.id_joueur})
        return liste_joueurs_tri

    def tours_suivants(self):
        """
        Contrôle les autres tours du tournoi
        """
        for tour in range(int(self.tournoi_actuel.nombre_tours) - 1):
            ce_tour = modele_tour.Tour(self.tournoi_actuel,
                                       f"Tour N°{tour + 2}")
            ce_tour.generer_paires(self.tournoi_actuel)
            self.tournoi_actuel.tournees.append(ce_tour)
            self.tournoi_rapports.preparation_tour(ce_tour)
            ce_tour.lancement_tour()

            entree_valide = False
            while not entree_valide:
                entree = input("Appuyez sur Y pour entrer les résultats ==> ")
                if entree == "Y" or entree == 'y':
                    entree_valide = True
                    ce_tour.fin_tour()
                    self.entrer_resultats_matchs(ce_tour)
                else:
                    continue
            self.tournoi_rapports.resultats_tour(ce_tour)

    def trier_joueurs_points(self, tournoi):
        """
        Méthode pour trier les joueurs par points (par classement si égalité)
        """
        liste_joueurs_classe = self.trier_joueurs_classement(tournoi)
        liste_joueurs_tri = sorted(liste_joueurs_classe, key=lambda
            joueur: joueur.total_points_tournoi, reverse=True)
        return liste_joueurs_tri

    def triage_tours_suivants(self, tournoi):
        """
        Méthode pour générer les paires (matchs) des tours suivants
        """
        liste_joueurs_par_points = []
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

            liste_joueurs_par_points.append(joueur_1)
            liste_joueurs_par_points.append(joueur_2)
            self.MATCHS_JOUES.append({joueur_1.id_joueur, joueur_2.id_joueur})

        return liste_joueurs_par_points

    def entrer_resultats_matchs(self, tour):
        """
        Méthode pour la saisie des scores des matchs d'un tour
        :type tour: object Tour
        """
        for match in tour.liste_matchs:
            resultat_valide = False
            while not resultat_valide:
                resultat_joueur_1 = input(
                    f"Entrez le résultat de "
                    f"{match.joueur_1.nom_famille}"
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
                    match.ajouter_resultats_match(float(resultat_joueur_1),
                                                  float(resultat_joueur_2))
                else:
                    continue


class CreerTournoiControleur:
    """
    Créé un nouveau tournoi
    """

    def __init__(self):
        self.menu_principal_controleur = \
            menu_controleur.MenuPrincipalControleur()
        self.infos_tournoi = []
        self.liste_joueurs_serial = []
        self.liste_id_joueurs = []
        self.objet_tournoi = None
        self.joueur_db = modele_joueur.JOUEUR_DB
        self.tournoi = modele_tournoi.Tournoi()

    def __call__(self):
        print("Creation de tournoi...\n")
        self.infos_tournoi.append(self.ajout_nom())
        self.infos_tournoi.append(self.ajout_lieu())
        self.infos_tournoi.append(self.ajout_date())
        self.infos_tournoi.append(self.ajout_controle_temps())
        self.infos_tournoi.append(self.ajout_description())
        self.infos_tournoi.append(self.ajout_nombre_tours())
        self.infos_tournoi.append(self.ajout_nombre_joueurs())
        entree_valide = False
        while not entree_valide:
            entree = input("Créer des joueurs aléatoires? (Y/N) ==> ")
            if entree in ('Y', 'y'):
                entree_valide = True
                self.infos_tournoi.append(self.ajout_joueurs_aleatoires())
            if entree in ('N', 'n'):
                entree_valide = True
                self.ajout_joueurs()
                self.infos_tournoi.append(self.liste_id_joueurs)
        self.tournoi.ajout_db(self.infos_tournoi)
        print("==========================================================\n"
              "==================Nouveau tournoi créé !==================\n"
              "==========================================================\n")
        self.menu_principal_controleur()

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
            if choix in ('Y', 'y'):
                nombre_tours = input("Entrer un nombre de tours: ")
                if nombre_tours.isdigit() and int(nombre_tours) > 0:
                    entree_valide = True
                else:
                    print("Entrez un nombre entier supérieur à 0!")
            if choix in ('N', 'n'):
                entree_valide = True
            if choix == "":
                print("Veuillez choisir Y/N")
        return int(nombre_tours)

    def ajout_controle_temps(self):
        controle_temps = None
        print("Choisir le contrôle du temps:\n"
              "1) Bullet\n"
              "2) Blitz\n"
              "3) Coup rapide")
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
        return int(nombre_joueurs)

    def ajout_joueurs_aleatoires(self):
        """
        Créé et retourne une liste de joueurs aléatoire.
        """
        nombre_joueurs = int(self.infos_tournoi[6])
        liste_joueurs = tests.cree_joueurs_alea(nombre_joueurs)
        print(f"{nombre_joueurs} joueurs aléatoires ont été créés")
        return liste_joueurs

    def ajout_joueurs(self):
        """
        Choix des joueurs depuis la DB et les ajoute à self.liste_id_joueurs
        """
        id_choisi = None
        choix_valide = False
        while not choix_valide:
            choix = input("Ajouter un joueur au tournoi? Y/N ==> ")
            if choix.upper() == 'Y':
                choix_valide = True
            elif choix.upper() == 'N':
                return

        for player in self.joueur_db:
            print(f"Joueur ID: {player.doc_id} - {player['Nom']} "
                  f"{player['Prenom']} - Classement : {player['Classement']}")

        id_valide = False
        while not id_valide:
            id_choisi = input("Entrer l'ID du joueur à ajouter au tournoi: ")
            if id_choisi.isdigit() and int(
                    id_choisi) > 0 and int(id_choisi) <= len(self.joueur_db):
                id_valide = True
            else:
                print("Entrez une ID de joueur existant")
        id_choisi = int(id_choisi)
        if id_choisi in self.liste_id_joueurs:
            print(f"Le joueur {id_choisi} est deja dans le tournoi !\n"
                  f"Joueurs inscrits: {self.liste_id_joueurs}\n")
            id_choisi = None
            self.ajout_joueurs()

        if id_choisi is not None:
            self.liste_id_joueurs.append(id_choisi)
            print(f"Joueurs inscrits: {self.liste_id_joueurs}\n")
            self.ajout_joueurs()


class TournoiTest:
    def __init__(self):
        self.menu_principal_controleur = \
            menu_controleur.MenuPrincipalControleur()

    def __call__(self):
        # Créer le tournoi test
        tournoi_rois = modele_tournoi.Tournoi("Tournoi des Rois", "Toulouse",
                                              "16 janvier",
                                              "Bullet",
                                              "Le premier tournoi de 2022")

        tournoi_test = tests.Tests(tournoi_rois)
        tournoi_test.run()
        self.menu_principal_controleur()
