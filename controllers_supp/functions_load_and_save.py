#! /usr/bin/env python3
# coding: utf-8

class SaveAndLoad:

    def __init__(self):
        pass

    @classmethod
    def save_instances(data_file):
        """La fonction save_instances() prend en paramètre le nom d'un fichier .json présent 
        dans le dossier de l'application. Elle sauvegarde sur ce fichier toutes les instances
        de joueurs et de tournois présentes dans la session, en les sérialisant. Quand une 
        instance comporte d'autres instances à d'une autre classe à l'intérieur d'elle-même,
        la fonction va formatter cet instances d'une manière lisible et enregistrable pour 
        tinyDB. La fonction load_instances permettra ensuite de ré-instantier les instances enregistréees.
        """
        db = TinyDB(data_file)

        serialized_players = []
        if len(md.Player.PLAYERS) < 1:
            pass
        else:
            for player in md.Player.PLAYERS:
                serialized_player = {
                'first_name': player.first_name, 
                'last_name': player.last_name,
                'birthdate': player.birthdate, 
                'sex': player.sex,
                'ranking': player.ranking, 
                'score_in_tournament': player.score_in_tournament
                }
                serialized_players.append(serialized_player)

        serialized_tournaments = []
        serialized_tournament_rounds = []
        if len(md.Tournament.TOURNAMENTS) < 1:
            pass
        else:
            for tournament in md.Tournament.TOURNAMENTS:

                simplified_pairs_for_tinydb = tournament.transform_pairs_instances_in_pairs_names()
                
                serialized_tournament = {
                    'name': tournament.name, 
                    'location': tournament.location,
                    'date': tournament.date, 
                    'players': tournament.players,
                    'time_mode': tournament.time_mode, 
                    'description': tournament.description, 
                    'number_of_rounds': tournament.number_of_rounds,
                    'Pairs': simplified_pairs_for_tinydb
                }
                serialized_tournaments.append(serialized_tournament)
                for round in tournament.Rounds:
                    simplified_matches_results = round.transform_instances_in_matches()
                    serialized_round = {
                        'name' : round.name,
                        'matches_results' : simplified_matches_results,
                        'first_timestamp' : round.first_timestamp,
                        'last_timestamp' : round.last_timestamp,
                        'tournament_name' : tournament.name,
                        'round_index' : (int((round.name[-1])) - 1)
                    }
                    
                    serialized_tournament_rounds.append(serialized_round)
        players_table = db.table('players')
        players_table.truncate()
        players_table.insert_multiple(serialized_players)
        tournaments_table = db.table('tournaments')
        tournaments_table.truncate()
        tournaments_table.insert_multiple(serialized_tournaments)
        rounds_table = db.table('rounds')
        rounds_table.truncate()
        rounds_table.insert_multiple(serialized_tournament_rounds)

    @classmethod
    def load_instances(data_file):
        """La fonction load-instances() prend en paramètre le nom d'un fichier .json présent 
        dans le dossier de l'application. Elle charge toutes les instances sérialisées de Player et 
        Tournament présentes sur ce fichier et les instancie notre programme. Certaines valeurs des
        instances de Player et Tournament sont ensuite réactualisées, pour éviter que la logique interne
        de leurs classes à leur initialisation remette à leur état initial ces valeurs, ou pour 
        ré-instancier des instances de Round et de Joueur à l'intérieur des instances de Tournament, 
        tinyDB ne pouvant les enregistrer telles quelles. 
        """
        db = TinyDB(data_file)

        already_instanced_players = []
        already_instanced_tournaments = []
        for player in md.Player.PLAYERS:
            already_instanced_players.append(player.full_name)
        for tournament in md.Tournament.TOURNAMENTS:
            already_instanced_tournaments.append(tournament.name)

        players_table = db.table('players')
        serialized_players = players_table.all()
        for player in serialized_players:
            list_of_player_values = []
            for value in player.values():
                list_of_player_values.append(value)
            first_name = list_of_player_values[0]
            last_name = list_of_player_values[1]
            birthdate = list_of_player_values[2]
            sex = list_of_player_values[3]
            ranking = list_of_player_values[4]
            score_in_tournament = list_of_player_values[5]
            player_full_name = first_name + " " + last_name

            if player_full_name in already_instanced_players:
                pass
            else:
                player_instance = md.Player(first_name, last_name, birthdate, sex)
                player_instance.ranking = ranking
                player_instance.score_in_tournament = score_in_tournament

        tournaments_table = db.table('tournaments')
        serialized_tournaments = tournaments_table.all()
        for tournament in serialized_tournaments:
            list_of_tournament_values = []
            for value in tournament.values():
                list_of_tournament_values.append(value)
            name = list_of_tournament_values[0]
            location = list_of_tournament_values[1]
            date = list_of_tournament_values[2]
            players = list_of_tournament_values[3]
            time_mode = list_of_tournament_values[4]
            description = list_of_tournament_values[5]
            number_of_rounds = list_of_tournament_values[6]
            simplified_pairs = list_of_tournament_values[7]

            if name in already_instanced_tournaments:
                pass
            else:
                Pairs_of_instanced_players = []
                for pairs_of_a_round in simplified_pairs:
                    real_pair_of_a_round = []
                    for pair in pairs_of_a_round:
                        real_pair = []
                        for player_of_pair in pair:
                            for player in md.Player.PLAYERS:
                                if player_of_pair[0] == player.first_name and \
        player_of_pair[1] == player.last_name:
                                    real_pair.append(player)
                        real_pair_of_a_round.append(real_pair)
                    Pairs_of_instanced_players.append(real_pair_of_a_round)

                tournament_instance = md.Tournament(name, date, location, players, time_mode, description)
                tournament_instance.number_of_rounds = number_of_rounds
                tournament_instance.Pairs = Pairs_of_instanced_players

                rounds_table = db.table('rounds')
                serialized_rounds = rounds_table.all()
                for round in serialized_rounds:
                    list_of_round_values = []
                    for value in round.values():
                        list_of_round_values.append(value)
                    name_of_round = list_of_tournament_values[0]
                    simplified_matches_results = list_of_round_values[1]
                    first_timestamp = list_of_round_values[2]
                    last_timestamp = list_of_round_values[3]
                    tournament_name_of_round = list_of_round_values[4]
                    round_index = list_of_round_values[5]

                    
                    real_matches_results = []
                    for match_result in simplified_matches_results:
                        real_match_result = []
                        for list_of_player_and_score in match_result:
                            player_name = [list_of_player_and_score[0][0],\
        list_of_player_and_score[0][1]]
                            player_score = list_of_player_and_score[1]
                            for player in md.Player.PLAYERS:
                                if player_name[0] == player.first_name and \
        player_name[1] == player.last_name:
                                    new_list = [player, player_score]
                                    real_match_result.append(new_list)
                    real_matches_results.append(real_match_result)
                        

                    for tournament in md.Tournament.TOURNAMENTS:
                        if tournament.name == tournament_name_of_round:
                            our_round = tournament.Rounds[round_index]
                            our_round.matches_results = real_matches_results
                            our_round.first_timestamp = first_timestamp
                            our_round.last_timestamp = last_timestamp
                            break
