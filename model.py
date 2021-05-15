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

    def __init__(self):
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.turn = turn
        self.players = players
        self.time_mode = time_mode
        self.description = description

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

