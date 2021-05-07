#! /usr/bin/env python3
# coding: utf-8

class Navigation:

    def __init__(self):
        pass

    """Possible classe abstraite 
    Arrive à cette page
    Demande un input
    Récupère cet input
    Effectue une action
    Recommence
    """

class Menu:
    
    def __init__(self):
        pass

    @classmethod
    def show_menu(cls):
        print("\n\n ")
        print(r"###############MENU###############")
        print("\nBienvenue sur la page de menu, quelle action souhaitez-vous \
effectuer?")
        print("Pour effectuer une action, tapez son numéro dans la console et appuyez \
sur ENTRÉE.\n")
        print("Option '1' = Créer un tournoi / Afficher rapport tournoi")
        print("Option '2' = Créer un joueur / Afficher rapport joueur ")
        print("Option '3' = Mettre à jour le classement")
        print("Option '4' = Sauvegarder / Charger les Données")
        print("Option '5' = Quitter le programme")
        print("\nEntrez votre commande ...")

class ShowTournament:

    def __init__(self):
        pass

    @classmethod
    def show_tournament(cls):
        print("\n\n ")
        print(r"###############TOURNOI###############")
        print("\nBienvenue sur la page de création, de modification et de création \
de tournoi, matches et tours, quelle action souhaitez-vous effectuer?")
        print("Pour effectuer une action, tapez son numéro dans la console et appuyez \
sur ENTRÉE.\n")
        print("Option '1' = Créer un tournoi")
        print("Option '2' = Afficher la liste des tournois")
        print("Option '3' = Choisir un tournoi particulier")
        print("Option '4' = Revenir au menu")
        print("Option '5' = Aller à la page de sauvegarde/chargement")
        print("Option '6' = Quitter le programme")
        print("\nEntrez votre réponse ci-dessous:")

    @classmethod
    def show_createT(self):
        print("Entrez les informations de votre nouveau tournoi")
"""---On a l'option 1 Créer un tournoi
------Les nouvelles options s'affichent
------"Entrez les informations de votre nouveau tournoi"
------Nom & Date & Lieu & Nb Tours & Tournée & Joueurs & Temps & Description
------"Ces informations sont-elles incorrectes ou voulez-vous générer les 1eres paires de joueurs?"
------Génération de la 1ère paire de joueur
------"Entrez maintenant le résultat des matchs"
------Option Quitter
------Option Sauvegarder
------Option Rentrer le match 1
---------"Qui débute la partie ? Option 1 pour {Joueur1} Option 2 pour {Joueur2}
---------"Entrez maintenant le résultat des tours"
------------Option 1 Cette pièce s'est déplace en cette position (et a possiblement pris ce pion?) (datedébut et fin automatique)
------------Option 2 Modifier un tour
------------Option 3 Partie finie
------Option Rentrer le match 2
------Option Rentrer le match 3
------Option Rentrer le match 4
------Si les 4 matches sont rentrés, générer les prochaines paires de joueur et recommencer la boucle jusqu'au dernier match
------Si le nouveau tournoi a le même nom et est à la même date qu'un autre tournoi, alors ne pas l'ajouter et afficher 
message d'erreur."""
    

class ShowPlayer :
    
    def __init__(self):
        pass
    
    @classmethod
    def show_player(self):
        print("\n\n ")
        print(r"###############JOUEUR&CLASSEMENT###############")
        print("\nBienvenue sur la page de création de joueur quelle action \
souhaitez-vous effectuer?")
        print("Pour effectuer une action, tapez son numéro dans la console et appuyez \
sur ENTRÉE.\n")
        print("Option '1' = Créer un joueur")
        print("Option '2' = Afficher le classement des joueurs")
        print("Option '3' = Mettre à jour le classement")
        print("Option '4' = Revenir au menu")
        print("Option '5' = Aller à la page de sauvegarde/chargement")
        print("Option '6' = Quitter le programme")

class SaveAndLoad :

    def __init__(self):
        pass

    @classmethod
    def show_save_and_load(self):
        print("\n\n ")
        print(r"###############SAUVEGARDE&CHARGEMENT###############")
        print("\nBienvenue sur la page de sauvegarde et de chargement des données, \
quelle action souhaitez-vous effectuer?")
        print("Pour effectuer une action, tapez son numéro dans la console et appuyez \
sur ENTRÉE.\n")
        print("Option '1' = Créer une nouvelle sauvegarde")
        print("Option '2' = Afficher les sauvegardes précédentes / Charger \
une sauvegarde")
        print("Option '3' = Revenir au menu")
        print("Option '4' = Quitter le programme")

def show_error_message():
    pass

def show_exit():
    pass


#SaveAndLoad.show_save_and_load()