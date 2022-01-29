from controleurs import menu_controleur
from modeles import modele_joueur, modele_tournoi, modele_tour
from tests import tests
from vues import vue_principale
from operator import attrgetter
from collections import deque


class LancerTournoiControleur:
    """
    Lance un tournoi deja créé.
    """

    MATCHS_JOUES = []
    TOURS_JOUES = []

    def __init__(self):
        self.affiche_tournoi = None
        self.tournoi = None
        self.tour = modele_tour.Tour()
        self.liste_joueurs_trie = []
        self.menu_principal_controleur = \
            menu_controleur.MenuPrincipalControleur()
        self.vue_resultats = vue_principale.ResultatsTournoi()
        self.joueur = modele_joueur.Joueur()
        self.liste_joueurs_tournoi = []

    def __call__(self):
        self.tournoi_obj = self.selection_tournoi()
        self.liste_joueurs_trie = self.triage_initial(self.tournoi_obj)
        self.liste_joueurs_tournoi = self.liste_joueurs_trie.copy()

        self.tournoi_obj.liste_tours.append(
            self.tour.lancer_tour(self.liste_joueurs_trie, self.tournoi_obj))
        self.sauvegarde_tournoi(self.tournoi_obj)

        for tour in range(int(self.tournoi_obj.nombre_tours) - 1):
            for joueur in self.liste_joueurs_tournoi:
                print(
                    f"{joueur.nom_famille} --score: {joueur.total_points_tournoi}")
            self.liste_joueurs_trie_autre = self.triage_tours_suivants()
            self.tournoi_obj.liste_tours.append(
                self.tour.lancer_tour(self.liste_joueurs_trie_autre,
                                      self.tournoi_obj))
            self.sauvegarde_tournoi(self.tournoi_obj)

        self.vue_resultats(self.tournoi_obj, self.liste_joueurs_tournoi)
        self.menu_principal_controleur()

    def sauvegarde_tournoi(self, tournoi_obj):
        """
        Méthode de sauvegarde de tournoi dans la DB tournoi
        :type tournoi_obj: object Tournoi
        """
        tournoi_db = modele_tournoi.TOURNOI_DB
        table_tours = tournoi_db.table('tours')

        tour_obj = tournoi_obj.liste_tours[-1]
        tour_serialise = tour_obj.serialise()
        tour_serialise[
            'Liste matchs termines'] = tour_obj.liste_matchs_termines

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
            else:
                print("Entrée invalide (Y/N)")

    def selection_tournoi(self):
        """
        Méthode pour sélectionner un tournoi non démarré.
        :rtype: object Tournoi
        """
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

    def triage_initial(self, tournoi):
        """
        Méthode pour générer les paires (matchs) du premier tour
        :return: liste d'objets Joueur
        :rtype: list
        """
        ids_joueurs = tournoi.ids_joueurs
        instances_joueurs = []
        liste_joueurs_tri = []

        for id_joueur in ids_joueurs:
            joueur = modele_joueur.JOUEUR_DB.get(doc_id=id_joueur)
            joueur = self.joueur.creer_instance_joueur(joueur)
            instances_joueurs.append(joueur)

        for joueur in instances_joueurs:
            joueur_1 = joueur
            index_joueur_1 = instances_joueurs.index(joueur)

            if index_joueur_1 + len(ids_joueurs) / 2 < len(ids_joueurs):
                index_joueur_2 = index_joueur_1 + int(len(ids_joueurs) / 2)
                joueur_2 = instances_joueurs[index_joueur_2]
                liste_joueurs_tri.append(joueur_1)
                liste_joueurs_tri.append(joueur_2)
                self.MATCHS_JOUES.append(
                    {joueur_1.id_joueur, joueur_2.id_joueur})
            else:
                pass

        return liste_joueurs_tri

    def triage_tours_suivants(self):
        """
        Méthode pour générer les paires (matchs) des tours suivants
        :return: liste d'objets Joueur
        :rtype: list
        """
        test_match = set()
        liste_joueurs_par_score = []

        instances_joueurs_a_trier = self.liste_joueurs_tournoi.copy()
        instances_joueurs_a_trier.sort(
            key=attrgetter("total_points_tournoi", 'classement'), reverse=True)

        queue = deque(instances_joueurs_a_trier)
        while len(queue) > 1:
            joueur_1 = queue.popleft()
            joueur_2 = None
            for i in range(0, len(queue)):
                joueur_2_tmp = queue[i]

                test_match.add(joueur_1.id_joueur)
                test_match.add(joueur_2_tmp.id_joueur)

                if test_match not in self.MATCHS_JOUES:
                    joueur_2 = joueur_2_tmp
                    queue.remove(joueur_2_tmp)
                    break
                else:
                    if i == (len(queue) - 1):
                        joueur_2 = queue.popleft()
                    else:
                        continue

            print(f"Ajout du match {joueur_1} VS {joueur_2}")
            liste_joueurs_par_score.append(joueur_1)
            liste_joueurs_par_score.append(joueur_2)
            instances_joueurs_a_trier.pop(
                instances_joueurs_a_trier.index(joueur_2))
            self.MATCHS_JOUES.append(
                {joueur_1.id_joueur, joueur_2.id_joueur})
            test_match.clear()

        return liste_joueurs_par_score


class CreerTournoiControleur:
    """
    Crée un nouveau tournoi et l'enregistre dans la BD tournoi
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
