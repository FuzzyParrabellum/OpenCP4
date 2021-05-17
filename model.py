#! /usr/bin/env python3
# coding: utf-8

class Player:

    NUMBER_OF_PLAYERS = 0
    PLAYERS = []

    def __init__(self,first_name, last_name, birthdate, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.sex = sex
        Player.NUMBER_OF_PLAYERS += 1
        self.ranking = self.NUMBER_OF_PLAYERS
        self.PLAYERS.append(self)

    def change_rank(self, new_rank):
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
        self.name = name
        self.location = location
        self.date = date
        self.players = players
        self.time_mode = time_mode
        self.description = description
        number_of_rounds = 4
        self.TOURNAMENTS.append(self)

    def classify_by_rank(self, dictionnary_of_players):
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
        classified_players = self.classify_by_rank(dictionnary_of_players)
        first_group = classified_players[0:4]
        second_group = classified_players[4:]
        pairs = []
        for player_index in range(len(first_group)):
            pairs.append([first_group[player_index], second_group[player_index]])
        return pairs

class Match:

    def __init__(self):
        self.player1 = player1
        self.player2 = player2

class Round:

    def __init__(self):
        self.match = match
        self.name = name
        self.first_timestamp = first_timestamp
        self.last_timestamp = last_timestamp

