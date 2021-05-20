#! /usr/bin/env python3
# coding: utf-8

import datetime 

class Player:

    NUMBER_OF_PLAYERS = 0
    PLAYERS = []

    def __init__(self,first_name, last_name, birthdate, sex):
        """On initialise un joueur, puis on indique dans une constante
        NUMBER_OF_PLAYERS le nombre de joueurs existants. On ajoute également
        l'instance de ce joueur dans une constante PLAYERS afin de pouvoir plus tard
        facilement identifier un joueur en le comparant avec les instances de cette 
        liste. score_in_tournament ne sert que quand le joueur est actuellement dans
        un tournoi et indique son score dans le tournoi, il est remis à 0 quand le
        tournoi se termine.
        """
        self.first_name = first_name
        self.last_name = last_name
        full_name = first_name + " " + last_name
        self.full_name = full_name
        self.birthdate = birthdate
        self.sex = sex
        Player.NUMBER_OF_PLAYERS += 1
        self.ranking = self.NUMBER_OF_PLAYERS
        self.PLAYERS.append(self)

        score_in_tournament = 0
        self.score_in_tournament = score_in_tournament

    def change_rank(self, new_rank):
        """La méthode change_ranks permet de changer le classement d'un joueur
        en prenant en paramètre le nouveau classement que l'on aimerait donner
        au joueur.
        """
        old_rank = self.ranking
        self.new_rank = new_rank
        for player in self.PLAYERS:
            if player != self and new_rank > old_rank:
                if player.ranking <= new_rank and player.ranking > old_rank:
                    player.ranking -= 1
            elif player != self and new_rank < old_rank:
                if player.ranking >= new_rank and player.ranking < old_rank:
                    player.ranking += 1
        self.ranking = new_rank

class Tournament:

    TOURNAMENTS = []

    def __init__(self, name, date, location, players, time_mode, description):
        """On initialise une instance de tournoi, puis on ajoute cette instance
        dans la constante de classe TOURNAMENTS afin plus tard de facilement 
        trouver un tournoi en le comparant avec chacune de ces instances. On
        initialise ensuite plusieurs instances de Round selon la variable 
        number_of_rounds fixée par défaut à 4. On range ces Rounds dans une liste
        On crée une liste Pairs qui contiendra ensuite toutes les différentes paires
        de chaque Round.
        """
        self.name = name
        self.location = location
        self.date = date
        self.players = players
        self.time_mode = time_mode
        self.description = description
        number_of_rounds = 4
        self.number_of_rounds = number_of_rounds
        self.TOURNAMENTS.append(self)
        Rounds = []
        self.Rounds = Rounds
        for round_int in range(number_of_rounds):
            Rounds.append(Round("Round {}".format(round_int + 1)))
        Pairs = []
        self.Pairs = Pairs


    def classify_by_rank(self, dictionnary_of_players):
        """classify_by_rank permet de prendre un dictionnaire de joueurs
        et de retourner une liste classée selon le classement de ces joueurs.
        avec le joueur ayant le plus haut classement en 1er.
        """
        players_list = []
        for player in dictionnary_of_players.values():
            players_list.append(player)
        players_instances = []
        for player_instance in Player.PLAYERS:
            for player in players_list:
                if player[0] == player_instance.first_name and \
player[1] == player_instance.last_name:
                    players_instances.append(player_instance)
        classified_players = []
        for tournament_player in players_instances:
            if classified_players == []:
                classified_players.append(tournament_player)
            else:
                if tournament_player.ranking > classified_players[-1].ranking:
                    classified_players.append(tournament_player)
                elif tournament_player.ranking < classified_players[0].ranking:
                    classified_players = [tournament_player] + classified_players
                else:
                    for player in classified_players:
                        if tournament_player.ranking > player.ranking:
                            new_index = classified_players.index(player)  
                    classified_players = classified_players[0:new_index] + \
[tournament_player] + classified_players[new_index+1:-1]    
        return classified_players

    def generate_pairs_of_players(self, dictionnary_of_players):
        """generate_pairs_of_players prend en paramètre un dictionnaire de
        joueurs et va, à l'aide de la méthode classify_by_rank, retourner des
        paires selon le système de tournoi Suisse.
        Cette méthode ne s'utilise que pour la 1ère génération de paires, quand
        les joueurs n'ont pas encore de score.
        """
        classified_players = self.classify_by_rank(dictionnary_of_players)
        first_group = classified_players[0:4]
        second_group = classified_players[4:]
        pairs = []
        for player_index in range(len(first_group)):
            pairs.append([first_group[player_index], second_group[player_index]])
        self.Pairs.append(pairs)
        return pairs

    def reclassify_if_equal(self, list_of_players):
        """reclassify_if_equal prend en paramètre une liste de joueurs 
        renvoyée par la méthode generate_new_pairs, qui est déjà classée
        selon le score des joueurs pendant le tournoi.
        Si plusieurs de ces joueurs ont des scores égaux, la méthode va
        renvoyer une nouvelle liste en reclassant ces joueurs selon leur
        classement.
        """
        new_list = []
        for player in list_of_players:
            current_index = list_of_players.index(player)
            if player == list_of_players[-1]:
                if player in new_list:
                    pass
                else:
                    new_list.append(player)
            else:
                next_player = list_of_players[current_index+1]
                if player.score_in_tournament != next_player.score_in_tournament:
                    if player in new_list:
                        pass
                    else:
                        new_list.append(player)
                elif player.score_in_tournament == next_player.score_in_tournament:
                    number_of_successive_equalities = 1
                    if player in new_list:
                        pass
                    elif len(list_of_players[current_index+1:]) > 1:
                        for play_index in range(len(list_of_players[current_index+1:])):
                            next_play = list_of_players[play_index+1]
                            if list_of_players[play_index].score_in_tournament == next_play.score_in_tournament:
                                number_of_successive_equalities += 1
                        equality_list = list_of_players[current_index : (current_index + 1)\
+ number_of_successive_equalities]
                        dictionnary_of_equal_players = {}
                        for player_index in range(len(equality_list)):
                            dictionnary_of_equal_players[player_index] = [equality_list[player_index].first_name, \
equality_list[player_index].last_name]
                        classified_equality_list = self.classify_by_rank(dictionnary_of_equal_players)
                        new_list = new_list + classified_equality_list
                    else:
                        dictionnary_of_equal_players = {}
                        for player_index in range(0,2):
                            dictionnary_of_equal_players[player_index] = [equality_list[player_index].first_name, \
equality_list[player_index].last_name]   
                        classified_equality_list = self.classify_by_rank(dictionnary_of_equal_players)
                        new_list = new_list + classified_equality_list
        return new_list

    def generate_new_pairs(self):
        """generate_new_pairs va générer de nouvelles paires d'instance de joueurs selon
        le round pendant lequel on se trouve et le score des joueurs.
        """
        our_players = []
        for pair in self.Pairs[0]:
            for player_instance in pair:
                our_players.append(player_instance)
        classified_players = []
        for player in our_players:
            if classified_players == []:
                classified_players.append(player)
            elif player.score_in_tournament >= classified_players[-1].score_in_tournament:
                classified_players.append(player)
            elif player.score_in_tournament <= classified_players[0].score_in_tournament:
                classified_players = [player] + classified_players
            else:
                for play in classified_players:
                    if player.score_in_tournament > play.score_in_tournament:
                        new_index = classified_players.index(play)
                classified_players = classified_players[0:new_index+1] + \
[player] + classified_players[new_index+1:]
        right_order_classified_players = list(reversed(classified_players))
        classified_players = self.reclassify_if_equal(right_order_classified_players)
        # doit maintenant écrire du code pour faire en sorte que si un joueur a déjà joué contre un autre
        # il doive maintenant jouer avec encore un autre joueur
        first_group = classified_players[0:4]
        second_group = classified_players[4:]
        pairs = []
        for player_index in range(len(first_group)):
            pairs.append([first_group[player_index], second_group[player_index]])
        self.Pairs.append(pairs)
        return pairs

    def transform_pairs_instances_in_pairs_names(self):
        """Pairs in a tournament are instances of players, this function allows
        us to replace these instances by the players' first and last name.
        """
        transformed_pairs = []
        for pairs_of_a_round in self.Pairs:
            simplified_pair_of_a_round = []
            for pair in pairs_of_a_round:
                simplified_pair = []
                for player in pair:
                    player = [player.first_name, player.last_name]
                    simplified_pair.append(player)
                simplified_pair_of_a_round.append(simplified_pair)
            transformed_pairs.append(simplified_pair_of_a_round)
        return transformed_pairs


class Round:

    def __init__(self, name):
        self.name = name
        matches_results = []
        self.matches_results = matches_results
        self.first_timestamp = "Cette tournée n°{} n'a pas encore commencée".format(self.name[-1])
        self.last_timestamp = "Cette tournée n°{} n'est pas encore terminée".format(self.name[-1])

    def begin_round(self):
        """fonctionnalité à développer - indique l'heure de début d'un round
        """
        timestamp_to_format = datetime.datetime.now()
        self.first_timestamp = timestamp_to_format.strftime("%m-%d-%Y, %H:%M:%S")
        
    
    def set_matches_result(self, player1, player2, player1_result, player2_result):
        """set_matches_result permet de créer un tuple contenant le score correspondant
        à chaque joueur à la fin d'un match. Chaque tuple sera ajouté dans la liste 
        matches_results crée pendant l'initialisation du Round.
        """
        match_tuple = ([player1, player1_result], [player2, player2_result])
        self.matches_results.append(match_tuple)
        player1.score_in_tournament += player1_result
        player2.score_in_tournament += player2_result

    def end_round(self):
        """fonctionnalité à développer - indique l'heure de fin d'un round
        """
        timestamp_to_format = datetime.datetime.now()
        self.last_timestamp = timestamp_to_format.strftime("%m-%d-%Y, %H:%M:%S")

    def transform_instances_in_matches(self):
        simplified_matches_results = []
        for match_result in self.matches_results:
            simplified_match_result = []
            for list_of_player_and_score in match_result:
                player_instance_to_format = [list_of_player_and_score[0].first_name,\
list_of_player_and_score[0].last_name]
                player_score = list_of_player_and_score[1]
                new_list = [player_instance_to_format, player_score]
                simplified_match_result.append(new_list)
            simplified_matches_results.append(simplified_match_result)
        return simplified_matches_results

