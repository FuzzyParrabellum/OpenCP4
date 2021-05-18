#! /usr/bin/env python3
# coding: utf-8
import re
import model
from sre_constants import error

class ShowMenu:
    
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
        Tournament_Name = input("Quel est le nom de ce nouveau tournoi?\n")
        Tournament_Date = input("Quelle est la date de ce nouveau tournoi? \
JJ/MM/AAAA\n")
        found_date = re.compile(r"\d\d/\d\d/\d\d\d\d").search(Tournament_Date)
        while not found_date:
            print("Veuillez entrer une date au bon format svp")
            Tournament_Date = input("Quelle est la date de ce nouveau tournoi? \
JJ/MM/AAAA\n")
            found_date = re.compile(r"\d\d/\d\d/\d\d\d\d").search(Tournament_Date)
        # Si un tournoi porte déjà la même nom à la même date, message d'erreur
        Tournament_Location = input("Où se déroule ce nouveau tournoi?\n")
        player_dictionnary = {}
        for player_index in range(1,9):
            player_first_name = input("Quel est le prénom du joueur n°{} à \
ajouter?\n".format(player_index))
            player_last_name = input("Quel est le nom du joueur n°{} à \
ajouter?\n".format(player_index))
            player_found = False
            while player_found == False:
                for player in model.Player.PLAYERS:
                    if player_first_name == player.first_name and \
player_last_name == player.last_name:
                        print("\nCe joueur a bien été rajouté à la liste\n")
                        player_dictionnary[player_index] = [player_first_name, player_last_name]
                        player_found = True
                if player_found == True:
                    pass
                else:
                    print("Il n'existe pas encore de joueur portant ce nom\n")
                    response = input("Souhaitez-vous retourner au menu ? O/N\n")
                    if response == "O":
                        return "Tournament_menu"
                    player_first_name = input("Quel est le prénom du joueur n°{} à \
ajouter?\n".format(player_index))
                    player_last_name = input("Quel est le nom du joueur n°{} à \
ajouter?\n".format(player_index))
        Time_Preference = input("'Bullet', 'Blitz' ou 'Coup rapide'?\n")
        while Time_Preference not in ['Bullet', 'Blitz', 'Coup rapide']:
            print("Veuillez entrer un mode de temps au bon format svp")
            Time_Preference = input("'Bullet', 'Blitz' ou 'Coup rapide'?\n")
        Description = input("Comment décrire ce tournoi de manière brève?\n")
        print("Les informations de votre nouveau tournoi ont été enregistrées, elles \
restent modifiables en choisissant l'option 'Modifier les informations de ce tournoi'\n")
        return [Tournament_Name, Tournament_Date, Tournament_Location, \
player_dictionnary, Time_Preference, Description]


    @classmethod
    def show_create_matches(cls, Tournament_name):
        for tournament in model.Tournament.TOURNAMENTS:
            if tournament.name == Tournament_name:
                our_tournament = tournament
                break
        for round_index in range(len(our_tournament.Rounds)):
            if our_tournament.Rounds[round_index].matches_results == []:
                our_round_index = round_index
                break
        our_tournament.Rounds[round_index].begin_round()
        if our_round_index == 0:
            pairs = our_tournament.generate_pairs_of_players(our_tournament.players)
            pairs_names = []
            for pair in pairs:
                new_pair = "{} {} contre {} {}".format(pair[0].first_name, pair[0].last_name, \
    pair[1].first_name, pair[1].last_name)
                pairs_names.append(new_pair)
        else:
            pairs = our_tournament.generate_new_pairs()
            pairs_names = []
            for pair in pairs:
                new_pair = "{} {} contre {} {}".format(pair[0].first_name, pair[0].last_name, \
    pair[1].first_name, pair[1].last_name)
                pairs_names.append(new_pair)

        print("Les paires de joueurs crées pour ce round sont: \n")
        print("{0}\n{1}\n{2}\n{3}".format(pairs_names[0], pairs_names[1], pairs_names[2], \
pairs_names[3]))
        print("\nVos options sont: \n")
        print("Option '1' = Entrer le résultat des matchs")
        print("Option '2' = Modifier les informations de ce tournoi")
        print("Option '3' = Revenir à la page de création et d'affichage de tournoi")

    @classmethod
    def show_enter_matches(cls, Tournament_name):
        for tournament in model.Tournament.TOURNAMENTS:
            if tournament.name == Tournament_name:
                our_tournament = tournament
                break
        for round_index in range(len(our_tournament.Rounds)):
            if our_tournament.Rounds[round_index].matches_results == []:
                our_round_index = round_index
                break
        current_round_pairs = our_tournament.Pairs[our_round_index]
        for index_of_pair in range(len(current_round_pairs)):
            print("Rentrez maintenant le résultat du match n°{}:\n".format(index_of_pair+1))
            player1 = current_round_pairs[index_of_pair][0]
            player2 = current_round_pairs[index_of_pair][1]
            player1_name = "{} {}".format(player1.first_name, player1.last_name)
            player2_name = "{} {}".format(player2.first_name, player2.last_name)
            result = input("Quel est le résultat du joueur {}?\n'G' si il a gagné le match\
,'E' si il y a eu égalité ou 'P' si il a perdu le match.\n".format(player1_name))
            while result not in ["G", "E", "P"]:
                print("\nEntrez seulement un résultat au format indiqué svp 'G', 'E' ou 'P'\n")
                result = input("Quel est le résultat du joueur {}?\n'G' si il a gagné le match\
,'E' si il y a eu égalité ou 'P' si il a perdu le match.\n".format(player1_name))
            if result == "G":
                player1_result = 1
                player2_result = 0
            elif result == "E":
                player1_result = 0.5
                player2_result = 0.5
            elif result == "P":
                player1_result = 0
                player2_result = 1

            print("{} gagne {} point.\n".format(player1_name, player1_result))
            print("{} gagne {} point.\n".format(player2_name, player2_result))

            our_tournament.Rounds[our_round_index].set_matches_result(\
player1, player2 , player1_result, player2_result)
        print("\nTous les résultats du Round {} ont bien été enregistrés\n"\
.format(our_round_index + 1))
        our_tournament.Rounds[round_index].end_round()
        return [our_tournament, our_round_index]
        
    @classmethod
    def show_tournament_ending(cls, Tournament_name):
        for tournament in model.Tournament.TOURNAMENTS:
            if tournament.name == Tournament_name:
                our_tournament = tournament
                break
        print("\nLe Tournoi {} est maintenant terminé\n".format(Tournament_name))
        print("\nLes résultats sont :\n")
        players_list = []
        for player in our_tournament.players.values():
            players_list.append(player)
        players_instances = []
        for player_instance in model.Player.PLAYERS:
            for player in players_list:
                if player[0] == player_instance.first_name and \
player[1] == player_instance.last_name:
                    players_instances.append(player_instance)
        for player in players_instances:
            print("{} {} scored {} points".format(player.first_name, player.last_name, \
player.score_in_tournament))
            player.score_in_tournament = 0


class ShowPlayer :
    
    def __init__(self):
        pass
    
    @classmethod
    def show_player(cls):
        print("\n\n ")
        print(r"###############JOUEUR&CLASSEMENT###############")
        print("\nBienvenue sur la page de création de joueur quelle action \
souhaitez-vous effectuer?")
        print("Pour effectuer une action, tapez son numéro dans la console et appuyez \
sur ENTRÉE.\n")
        print("Option '1' = Créer un joueur")
        print("Option '2' = Afficher le classement des joueurs")
        print("Option '3' = Revenir au menu")
        print("Option '4' = Aller à la page de sauvegarde/chargement")
        print("Option '5' = Quitter le programme")
        print("\nEntrez votre commande ci-dessous...")
    
    @classmethod
    def show_create_player(cls):
        print("Entrez les informations de votre nouveau joueur")
        first_name = input("Quel est le prénom de ce nouveau joueur?\n")
        last_name = input("Quel est le nom de famille de ce nouveau joueur?\n")
        birth = input("Quelle est la date de naissance de ce nouveau joueur?\
JJ/MM/AAAA\n")
        foundbirth = re.compile(r"\d\d/\d\d/\d\d\d\d").search(birth)
        while not foundbirth:
            print("Veuillez entrer une date au bon format svp")
            birth = input("Quelle est la date de naissance de ce nouveau joueur?\
JJ/MM/AAAA\n")
            foundbirth = re.compile(r"\d\d/\d\d/\d\d\d\d").search(birth)
        sex = input("Quelle est le sexe de ce nouveau joueur? M/F\n")
        foundsex = re.compile(r"[MF]").search(sex)
        while not foundsex:
            print("Veuillez entrer le bon format svp")
            sex = input("Quelle est le sexe de ce nouveau joueur? M/F\n")
            foundsex = re.compile(r"[MF]").search(sex)
        # Si un tournoi porte déjà la même nom à la même date, message d'erreur
        print("Les informations du nouveau joueur ont été enregistrées, elles \
restent modifiables en choisissant l'option 'Modifier les informations du joueur'")
        return [first_name, last_name, birth, sex]

    @classmethod
    def show_ranks(cls):
        print("\nQue désirez-vous faire ensuite?")
        print("Option '1' : Voir les informations d'un joueur en particulier")
        print("Option '2' : Mettre à jour le classement d'un joueur")
        print("Option '3' : Revenir au menu")



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
        print("Option '2' = Charger une sauvegarde")
        print("Option '3' = Revenir au menu")
        print("Option '4' = Quitter le programme")
        print("\nEntrez votre commande ci-dessous...")


def show_error_msg():
    pass

def show_exit():
    print('Êtes-vous sûr de vouloir quitter le programme?')
    print('Option "1" : Oui')
    print('Option "2" : Non')


#SaveAndLoad.show_save_and_load()