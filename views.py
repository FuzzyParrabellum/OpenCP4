#! /usr/bin/env python3
# coding: utf-8

class Navigation:

    def __init__(self):
        pass

    @classmethod
    def navigate(cls, response=False):
        if not response:
            Menu.show_menu()
            response = input()
            return response
        elif response == "1" or response == 1:
            ShowTournament.show_tournament()
            response = input()
            return ["Menu", "Tournament",response]
        elif response == "2" or response == 2:
            ShowPlayer.show_player()
            response = input()
            return ["Menu", "Player",response]
        elif response == "3" or response == 3:
            pass
        elif response == "4" or response == 4:
            SaveAndLoad.show_save_and_load()
            response = input()
            return ["Menu", "SaveAndLoad",response]
        elif response == "5" or response == 5:
            quit()
        else:
            print("Veuillez uniquement entrer une des options proposées")
            cls.navigate()
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
        print("\nEntrez votre commande ci-dessous...")


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
        print("\nEntrez votre commande ci-dessous...")

    @classmethod
    def show_create_tournament(cls):
        print("Entrez les informations de votre nouveau tournoi")
        Tournament_Name = input("Quel est le nom de ce nouveau tournoi?")
        Tournament_Date = input("Quelle est la date de ce nouveau tournoi?")
        # Si un tournoi porte déjà la même nom à la même date, message d'erreur
        Tournament_Location = input("Où se déroule ce nouveau tournoi?")
        Tournament_Player1 = input("Quel est le nom du 1er joueur?")
        Tournament_player2 = input("Quel est le nom du 2e joueur?")
        Tournament_player3 = input("Quel est le nom du 3e joueur?")
        Tournament_player4 = input("Quel est le nom du 4e joueur?")
        Tournament_Player5 = input("Quel est le nom du 5e joueur?")
        Tournament_player6 = input("Quel est le nom du 6e joueur?")
        Tournament_player7 = input("Quel est le nom du 7e joueur?")
        Tournament_player8 = input("Quel est le nom du 8e joueur?")
        Time_Preference = input("'Bullet', 'Blitz' ou 'Coup rapide'?")
        Description = input("Comment décrire ce tournoi de manière brève?")
        return [Tournament_Name, Tournament_Date, Tournament_Location, \
            Tournament_Player1, Tournament_Player2, Tournament_Player3, \
            Tournament_Player4, Tournament_Player5, Tournament_Player6, \
            Tournament_Player7, Tournament_Player8, Time_Preference, \
            Description]

    @classmethod
    def show_create_matches(cls): 
        print("Les informations de votre nouveau tournoi ont été enregistrées, elles \
restent modifiables en choisissant l'option 'Modifier les informations de ce tournoi'")
        print("Les paires de joueurs crées pour ce round sont {1}, {2}, {3}, {4}\
".format(1=None, 2=None, 3=None, 4=None))
        print("\nVos options sont: \n")
        print("Option '1' = Entrer le résultat des matchs")
        print("Option '2' = Modifier les informations de ce tournoi")
        print("Option '3' = Revenir à la page de création et d'affichage de tournoi")

    @classmethod
    def show_enter_matches(cls):
        rounds = []
        winner = False
        i = 1
        for match in range(4): 
            #adapter ce qu'il y en-dessous en fonction et voir sous quel format les rounds doivent être enregistrés
            match = input("Rentrez maintenant le résultat du match n°1: ")
            while not winner:
                result = input("Rentrez maintenant le résultat du tour n°{}".format(i))
                i++
                rounds.append(result)
                if result == "checkmate" :
                    winner = True
             
        sure_match1 = input("Voulez-vous modifier ce résultat ? 'Oui'/'Non'")
        match2 = input("Rentrez maintenant le résultat du match n°2: ")
        sure_match2 = input("Voulez-vous modifier ce résultat ? 'Oui'/'Non'")
        match3 = input("Rentrez maintenant le résultat du match n°3: ")
        sure_match3 = input("Voulez-vous modifier ce résultat ? 'Oui'/'Non'")
        match4 = input("Rentrez maintenant le résultat du match n°4: ")
        sure_match4 = input("Voulez-vous modifier ce résultat ? 'Oui'/'Non'")
        
"""     

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
        print("\nEntrez votre commande ci-dessous...")


class ShowSaveAndLoad :

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
        print("\nEntrez votre commande ci-dessous...")


def show_error_message():
    pass

def show_exit():
    pass


#SaveAndLoad.show_save_and_load()