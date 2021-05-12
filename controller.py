#! /usr/bin/env python3
# coding: utf-8

import os
import json

import model as md
from views import ShowMenu as sh_me
from views import ShowPlayer as sh_pl
from views import ShowTournament as sh_to
from views import ShowSaveAndLoad as sh_sa
from views import show_exit 
from views import show_error_msg


"""fonction permettant de récupérer les arguments passés dans le programme via l'invite de commande
Si il est passé ce mot-clé, avec possiblement cet argument, alors ...
Sinon renvoyer un message d'erreur et inviter à réessayer
"""
    
def take_option(option=False):
    if not option:
        sh_me.show_menu()
        new_option = input()
        menu_dict = {1:"Tournament", 2:"Player", 3:"Actualize_rank", 4:"SaveAndLoad",\
5:"Quit"}
        if new_option not in ["1","2","3","4","5"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option()
        else :
            new_option = int(new_option)
            path = menu_dict[new_option]
            return ["Menu", path]
    
    # Si l'on veut aller dans le MENU
    elif option == "Menu":
        sh_me.show_menu()
        new_option = input()
        menu_dict = {1:"Tournament", 2:"Player", 3:"Actualize_rank", 4:"SaveAndLoad", \
5:"Quit", 42:"admin"}
        if new_option not in ["1","2","3","4","5", "42"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option()
        else :
            new_option = int(new_option)
            path = menu_dict[new_option]
            return ["Menu", path]

    #Si l'on veut aller dans la CREATION DE TOURNOI
    elif option == "Tournament_menu":
        tournament_menu_dict = {1:"Create_tournament", 2:"Show_tournament_list", \
3:"Choose_tournament", 4:"Menu", 5:"SaveAndLoad", 6:"Quit"}
        new_option = input()
        if new_option not in ["1","2","3","4","5","6"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option()
        else:
            new_option = int(new_option)
            path = tournament_menu_dict[new_option]
            return ["Tournament_menu", path]
    elif option == "Create_matches":
        create_tournament_dict = {1:"Matches_result", 2:"Modify_tournament_info", \
3:"Back_to_tournament_menu"}
        if new_option not in ["1","2","3"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option()
        else:
            new_option = int(new_option)
            path = create_tournament_dict[new_option]
            return ["Tournament_creation1", path]

    # Si on veut aller dans la CREATION DE JOUEUR
    elif option == "Player_menu":
        sh_pl.show_player()
        player_menu_dict = {1:"Create_player", 2:"Show_ranks", \
3:"Actualize_rank", 4:"Menu", 5:"SaveAndLoad", 6:"Quit"}
        new_option = input()
        if new_option not in ["1","2","3","4","5","6"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option()
        else:
            new_option = int(new_option)
            path = player_menu_dict[new_option]
            return ["Player", path]
    elif option == "Show_ranks_choices":
        # possibilité de rajouter un défilement des joueurs
        ranks_menu_dict = {1:"See_player_info", 2:"Player"}
        new_option = input()
        if new_option not in ["1","2"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option()
        else:
            new_option = int(new_option)
            path = ranks_menu_dict[new_option]
            return ["Player", path]

    # Si l'on veut SAUVEGARDER ou CHARGER UNE SAUVEGARDE
    elif option == "SaveAndLoad_menu":
        sh_sa.show_save_and_load()
        SaveAndLoad_menu_dict = {1:"New_save", 2:"Load_save", 3:"Menu", 4:"Quit"}
        new_option = input()
        if new_option not in ["1","2","3","4"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option()
        else:
            new_option = int(new_option)
            path = SaveAndLoad_menu_dict[new_option]
            return ["SaveAndLoad", path]


        

        
    else :
        pass
        
            # else:
            #     print("Veuillez uniquement entrer une des options proposées")
            #     path = response[0]
            #     new_option = input()
            #     take_option([path, new_option])
        # else :
        #     raise Exception('!!! No path nor option number provided !!!')
 
#########################################
#########################################

def generate_pair_of_players(list_of_players):
    players = [player1, player2, player3, player4, player5, player6, player7, \
player8]
    for i in len(list_of_players):
        players[i] = list_of_players[i-1]

#########################################
#########################################
    
class FromMenu():

    def __init__(self):
        pass

    @classmethod
    def take_response(self, response):
        self.response = response
        if response[1] == "Tournament":
            sh_to.show_tournament()
            return "Tournament_menu"
        if response[1] == None:
            pass
        if response[1] == "Player":
            sh_pl.show_player()
            return "Player_menu"
        if response[1] == "SaveAndLoad":
            sh_sa.show_save_and_load()
            return "SaveAndLoad_menu"  
        else:
            print("Un choix non prévu a été effectué en venant de {}"\
.format(response[0], response[1]))
            quit()


class FromPlayer():

    def __init__(self):
        pass

    @classmethod
    def take_response(self, response):
        self.response = response
        if response[1] == "Create_player":
            player_list = sh_pl.show_create_player()
            new_player = md.Player(player_list[0], player_list[1], player_list[2], \
player_list[3])
            return "Player_menu"

        if response[1] == "Show_ranks":
            for player in md.Player.PLAYERS:
                print("{}--{}--{}--{}--{}".format(player.first_name, player.last_name, \
player.birthdate, player.sex, player.rank))
            sh_pl.show_ranks()
            return "Show_ranks_choices"

        if response[1] == "See_player_info":
            player_first_name = input('Entrez le nom de famille du joueur\n')
            player_last_name = input('Entrez le prénom du joueur\n')
            for player in md.Player.PLAYERS:
                if player_first_name == player.first_name and \
                player_last_name == player.last_name:
                    print("{}--{}--{}--{}--{}\n\n".format(player.first_name, \
player.last_name, player.birthdate, player.sex, player.rank))
                    return "Show_ranks_choices"
                else:
                    print("\nCe joueur n'est pas enregistré \n")
                    return "Show_ranks_choices"
            
        if response[1] == "Actualize_rank":
            pass
        if response[1] == "SaveAndLoad":
            pass
        if response[1] == "Menu":
            return "Menu"
        else:
            print("Un choix non prévu a été effectué en venant de {}, {}".\
format(response[0], response[1]))
            quit()


class FromTournament():

    def __init__(self):
        pass

    @classmethod
    def take_response(self, response):
        self.response = response
        if response[1] == "Create_tournament":
            Tournament_list_of_values = sh_to.show_create_tournament()
            return "Create_matches"
        else:
            print("Un choix non prévu a été effectué en venant de {}".\
format(response[0], response[1]))
            quit()

        if response[0] == "Tournament_creation1":
            if response[1] == "Matches_result":
                Matches_list_of_values = sh_to.show_enter_matches()
                return ""
            else:
                print("Un choix non prévu a été effectué en venant de {}".\
    format(response[0], response[1]))
                quit()


class FromSaveAndLoad():

    def __init__(self):
        pass

    @classmethod
    def take_response(self, response):
        self.response = response
        if response[1] == "New_save":
            return ""

        if response[1] == "Load_save":
            return ""

        if response[1] == "Menu":
            return "Menu"

        else:
            print("Un choix non prévu a été effectué en venant de {}, {}".\
format(response[0], response[1]))
            quit()

def go_to_path(response):
    if response[0] and response[1]:
            if response[1] == "Quit":
                # afficher message, sûr de quitter?
                # Faudrait aussi que vérifie qu'a bien sauvegardé non?
                show_exit()
                sure = input()
                if sure not in ["1", "2"]:
                    print("Veuillez uniquement entrer une des options proposées")
                    go_to_path(response)
                elif sure == "1":
                    quit()
                elif sure == "2":
                    return response[0]
            if response[0] == "Menu" :
                return FromMenu.take_response(response)
            if response[0] == "Tournament_menu":
                return FromTournament.take_response(response)
            if response[0] == "Player":
                return FromPlayer.take_response(response)
            if response[0] == "SaveAndLoad":
                return FromSaveAndLoad.take_response(response)
            
    else:
        print('!!! No path nor option number provided !!!')
        quit()
    

#########################################
#########################################

def main():
    first_input = take_option()
    new_input = go_to_path(first_input)
    while True: 
        print("######################DEBUT DE LA BOUCLE#########################")
        new_option = take_option(new_input)
        print("NEW_OPTION : {}".format(new_option))
        if new_option[1] == "admin":
            break
        new_input = go_to_path(new_option)
        print("NEW_INPUT : {}".format(new_input))
        
    
if __name__ == "__main__":
    main()


# def go_to_path(response):
    # if response[0] and response[1]:
        # if response[1] == "Quit":
        #     # afficher message, sûr de quitter?
        #     # Faudrait aussi que vérifie qu'a bien sauvegardé non?
        #     show_exit()
        #     sure = input()
        #     if sure not in ["1", "2"]:
        #         print("Veuillez uniquement entrer une des options proposées")
        #         go_to_path(response)
        #     elif sure == "1":
        #         quit()
        #     elif sure == "2":
        #         return response[0]

        # QUAND ON VIENT DU MENU
        # if response[0] == "Menu" :
        #     if response[1] == "Tournament":
        #         sh_to.show_tournament()
        #         return "Tournament_menu"

        #     if response[1] == None:
        #         pass

        #     if response[1] == "Player":
        #         sh_pl.show_player()
        #         return "Player_menu"

        #     if response[1] == "SaveAndLoad":
        #         sh_sa.show_save_and_load()
        #         return "SaveAndLoad_menu"
                
        #     else:
        #         print("Un choix non prévu a été effectué en venant de {}".format(response[0], response[1]))
        #         quit()

        #QUAND ON VIENT DE LA CREATION DE TOURNOI
        # if response[0] == "Tournament_menu":
        #     if response[1] == "Create_tournament":
        #         Tournament_list_of_values = sh_to.show_create_tournament()
        #         return "Create_matches"
        #     else:
        #         print("Un choix non prévu a été effectué en venant de {}".format(response[0], response[1]))
        #         quit()

        # if response[0] == "Tournament_creation1":
        #     if response[1] == "Matches_result":
        #         Matches_list_of_values = sh_to.show_enter_matches()
        #         return ""
        #     else:
        #         print("Un choix non prévu a été effectué en venant de {}".format(response[0], response[1]))
        #         quit()

        #QUAND ON VIENT DE LA CREATION DE JOUEUR
#         if response[0] == "Player":
#             if response[1] == "Create_player":
#                 player_list = sh_pl.show_create_player()
#                 new_player = md.Player(player_list[0], player_list[1], player_list[2], \
# player_list[3])
#                 return "Player_menu"

#             if response[1] == "Show_ranks":
#                 for player in md.Player.PLAYERS:
#                     print("{}--{}--{}--{}--{}".format(player.first_name, player.last_name, \
# player.birthdate, player.sex, player.rank))
#                 sh_pl.show_ranks()
#                 return "Show_ranks_choices"

#             if response[1] == "See_player_info":
#                 player_first_name = input('Entrez le nom de famille du joueur\n')
#                 player_last_name = input('Entrez le prénom du joueur\n')
#                 for player in md.Player.PLAYERS:
#                     if player_first_name == player.first_name and \
#                     player_last_name == player.last_name:
#                         print("{}--{}--{}--{}--{}\n\n".format(player.first_name, \
# player.last_name, player.birthdate, player.sex, player.rank))
#                         return "Show_ranks_choices"
#                     else:
#                         print("\nCe joueur n'est pas enregistré \n")
#                         return "Show_ranks_choices"
                
#             if response[1] == "Actualize_rank":
#                 pass
#             if response[1] == "SaveAndLoad":
#                 pass
#             if response[1] == "Menu":
#                 return "Menu"
#             else:
#                 print("Un choix non prévu a été effectué en venant de {}, {}".format(response[0], response[1]))
#                 quit()
                        

        # if response[0] == "SaveAndLoad":
        #     if response[1] == "New_save":
        #         return ""

        #     if response[1] == "Load_save":
        #         return ""

        #     if response[1] == "Menu":
        #         return "Menu"

        #     else:
        #         print("Un choix non prévu a été effectué en venant de {}, {}".format(response[0], response[1]))
        #         quit()
    # else :
    #     raise Exception('!!! No path nor option number provided !!!')
