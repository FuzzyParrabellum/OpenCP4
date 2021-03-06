#! /usr/bin/env python3
# coding: utf-8
import re
import model


class ShowMenu:

    def __init__(self):
        pass

    @classmethod
    def show_menu(cls):
        print("\n\n ")
        print(r"###############MENU###############")
        print("\nBienvenue sur la page de menu de ce programme de gestion de tournois d'échecs. ")
        print("En tapant une commande avec votre clavier et en tapant Enter ensuite, vous pourrez")
        print("naviguer entre les différents menus du programme. Vous pourrez ajouter des joueurs, des tournois,")
        print("et le résultat de ces joueurs pendant ces tournois à une base de donnée en allant dans le menu")
        print("Sauvegarder / Charger les Données et charger ces données dans le même menu pour votre prochaine")
        print("utilisation.")
        print("ATTENTION : Si vous quittez sans sauvegarder, les données entrées ne seront pas enregistrées")
        print("\nPour effectuer une action, tapez son numéro dans la console et appuyez \
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
        print("Option '3' = Revenir au menu")
        print("Option '4' = Aller à la page de sauvegarde/chargement")
        print("Option '5' = Quitter le programme")
        print("\nEntrez votre commande ci-dessous...")

    @classmethod
    def show_create_tournament(cls):
        print("Entrez les informations de votre nouveau tournoi")
        Tournament_Name = input("Quel est le nom de ce nouveau tournoi?\n")
        for tournament in model.Tournament.TOURNAMENTS:
            if tournament.name == Tournament_Name:
                print("\nUn tournoi portant ce nom existe déjà, veuillez \
réessayer de créer un tournoi avec un autre nom svp \n")
                return "Tournament_menu"
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
        for player_index in range(1, 9):
            player_first_name = input("Quel est le prénom du joueur n°{} à \
ajouter?\n".format(player_index))
            player_last_name = input("Quel est le nom du joueur n°{} à \
ajouter?\n".format(player_index))
            player_found = False
            while player_found is False:
                for player in model.Player.PLAYERS:
                    if player_first_name == player.first_name and \
                            player_last_name == player.last_name:
                        if [player_first_name, player_last_name] in player_dictionnary.values():
                            print("\nCe joueur a déjà été ajouté au tournoi\n")
                        else:
                            print("\nCe joueur a bien été rajouté à la liste\n")
                            player_dictionnary[player_index] = [player_first_name, player_last_name]
                            player_found = True
                if player_found is True:
                    pass
                else:
                    print("Ajouter ce joueur n'est pas possible.\n")
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
restent modifiables en choisissant l'option ")
        print("'Modifier les informations de ce tournoi'après l'avoir sélectionné \
dans la liste des tournois.\n")
        return [Tournament_Name, Tournament_Date, Tournament_Location,
                player_dictionnary, Time_Preference, Description]

    @classmethod
    def show_REcreate_tournament(cls):
        tournament_date = input("Quelle est la date de ce nouveau tournoi? \
JJ/MM/AAAA\n")
        found_date = re.compile(r"\d\d/\d\d/\d\d\d\d").search(tournament_date)
        while not found_date:
            print("Veuillez entrer une date au bon format svp")
            tournament_date = input("Quelle est la date de ce nouveau tournoi? \
JJ/MM/AAAA\n")
            found_date = re.compile(r"\d\d/\d\d/\d\d\d\d").search(tournament_date)
        # Si un tournoi porte déjà la même nom à la même date, message d'erreur
        tournament_location = input("Où se déroule ce nouveau tournoi?\n")
        time_preference = input("'Bullet', 'Blitz' ou 'Coup rapide'?\n")
        while time_preference not in ['Bullet', 'Blitz', 'Coup rapide']:
            print("Veuillez entrer un mode de temps au bon format svp")
            time_preference = input("'Bullet', 'Blitz' ou 'Coup rapide'?\n")
        description = input("Comment décrire ce tournoi de manière brève?\n")
        print("Les informations de votre nouveau tournoi ont été enregistrées, elles \
restent modifiables en choisissant l'option ")
        print("'Modifier les informations de ce tournoi'après l'avoir sélectionné \
dans la liste des tournois.\n")
        return [tournament_date, tournament_location, time_preference, description]

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
                new_pair = "{} {} contre {} {}".format(pair[0].first_name, pair[0].last_name,
                                                       pair[1].first_name, pair[1].last_name)
                pairs_names.append(new_pair)
        else:
            pairs = our_tournament.generate_new_pairs()
            pairs_names = []
            for pair in pairs:
                new_pair = "{} {} contre {} {}".format(pair[0].first_name, pair[0].last_name,
                                                       pair[1].first_name, pair[1].last_name)
                pairs_names.append(new_pair)

        print("Les paires de joueurs crées pour ce round sont: \n")
        print("{0}\n{1}\n{2}\n{3}".format(pairs_names[0], pairs_names[1], pairs_names[2],
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

            our_tournament.Rounds[our_round_index].set_matches_result(
                player1, player2, player1_result, player2_result)
        print("\nTous les résultats du Round {} ont bien été enregistrés\n"
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
            print("Le score final de {} {} est de {} points".format(player.first_name, player.last_name,
                                                                    player.score_in_tournament))
            player.score_in_tournament = 0

    @classmethod
    def show_modify_round(cls, tournament_name):
        for tournament in model.Tournament.TOURNAMENTS:
            if tournament.name == tournament_name:
                our_tournament = tournament
                break
        answer1 = input("Souhaitez-vous modifier les informations générales de ce tournoi? O/N\n")
        if answer1 not in ["O", "N"]:
            while answer1 not in ["O", "N"]:
                print("Veuillez entrer une réponse au bon format svp\n")
                answer1 = input("Souhaitez-vous modifier les informations générales de ce tournoi? O/N\n")
        else:
            if answer1 == "O":
                tournament_values_to_change = cls.show_REcreate_tournament()
                our_tournament.date = tournament_values_to_change[0]
                our_tournament.location = tournament_values_to_change[1]
                our_tournament.time_mode = tournament_values_to_change[2]
                our_tournament.description = tournament_values_to_change[3]
                print("\nLes informations ont bien été changées.\n")
                return ["Tournament_status_choices", our_tournament]
            else:
                pass
        print("Souhaitez-vous compléter le résultat des matches de ce tournoi ? O/N")
        answer2 = input()
        if answer2 not in ["O", "N"]:
            while answer2 not in ["O", "N"]:
                print("Veuillez entrer une réponse au bon format svp\n")
                answer2 = input("Souhaitez-vous compléter le résultat des matches de ce tournoi ? O/N\n")
        else:
            if answer2 == "O":
                for round in our_tournament.Rounds:
                    if round.matches_results == []:
                        first_empty_round = [True]
                        break
                    if round == our_tournament.Rounds[-1]:
                        print("Les résultats de tous les matches ont déjà été rentrés !\n")
                        return ["Tournament_status_choices", our_tournament]
                return first_empty_round
            elif answer2 == "N":
                return ["Tournament_status_choices", our_tournament]

    @classmethod
    def show_tournaments_status_options(cls):
        print("\nQuelle action souhaitez-vous effectuer ensuite?")
        print("Option '1' = Sélectionner un tournoi en particulier")
        print("Option '2' = Revenir au menu de création de tournoi")
        print("Option '3' = Aller à la page de sauvegarde/chargement")
        print("Option '4' = Quitter le programme")
        print("\nEntrez votre commande ci-dessous...")

    @classmethod
    def show_tournament_status(cls):
        print("\nOption '1' = Liste de tous les tours du tournoi")
        print("Option '2' = Liste de tous les matches du tournoi")
        print("Option '3' = Modifier des informations de ce tournoi et/ou")
        print("terminer des remplir ces informations")
        print("Option '4' = Montrer les joueurs composant le tournoi triés par ordre alphabétique")
        print("Option '5' = Montrer les joueurs composant le tournoi triés par leur classement")
        print("Option '6' = Retourner à l'affichage des tournois")
        print("\nEntrez votre commande ci-dessous...")


class ShowPlayer:

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
        print("Option '3' : Afficher les joueurs selon leur nom de famille")
        print("Option '4' : Afficher les joueurs selon leur classement")
        print("Option '5' : Revenir au menu")


class ShowSaveAndLoad:

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
