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


def take_option(option=False):
    """take_option permet de récupérer l'input de l'utilisateur après lui avoir 
    montré ses choix. Si le programme se lance pour la première fois, take_option
    est invoquée sans paramètre, ce qui montre le menu.
    Si le programme est déjà lancé et qu'on réinvoque take_option, le paramètre 
    option sera un string ou une liste de strings fourni(s) par la fonction go_to_path 
    à la fin du programme, qui permet de naviguer entre les différents menus.
    """
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
        sh_to.show_tournament()
        tournament_menu_dict = {1:"Create_tournament", 2:"Show_tournament_list", \
3:"Choose_tournament", 4:"Menu", 5:"SaveAndLoad", 6:"Quit"}
        new_option = input()
        if new_option not in ["1","2","3","4","5","6"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option()
        else:
            new_option = int(new_option)
            path = tournament_menu_dict[new_option]
            return ["Tournament", path]

    elif option[0] == "Create_matches":
        sh_to.show_create_matches(option[1])
        create_tournament_dict = {1:"Matches_result", 2:"Modify_tournament_info", \
3:"Back_to_tournament_menu"}
        new_option = input()
        if new_option not in ["1","2","3"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option()
        else:
            new_option = int(new_option)
            path = create_tournament_dict[new_option]
            print("le path avant de renvoyer à go_to_path est {}".format(path))
            return ["Tournament", path, option[1]]

    # Si on veut aller dans la CREATION DE JOUEUR
    elif option == "Player_menu":
        sh_pl.show_player()
        player_menu_dict = {1:"Create_player", 2:"Show_ranks", \
3:"Menu", 4:"SaveAndLoad", 5:"Quit"}
        new_option = input()
        if new_option not in ["1","2","3","4","5","6"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option()
        else:
            new_option = int(new_option)
            path = player_menu_dict[new_option]
            return ["Player", path]
    elif option == "Show_ranks_choices":
        sh_pl.show_ranks()
        # possibilité de rajouter un défilement des joueurs
        ranks_menu_dict = {1:"See_player_info", 2:"Actualize_rank", 3:"Player_Menu"}
        new_option = input()
        if new_option not in ["1","2","3"]:
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
        print("Navigation not found")
        pass
        

#########################################
#########################################
    
class FromMenu:
    """Une fois que le programme a été lancé une 1ère fois et 
    que l'utilisateur a navigué vers une 1ère page, ce menu FromMenu
    permet de lui montrer à nouveau les options du Menu.
    """
    def __init__(self):
        pass

    @classmethod
    def take_response(self, response):
        self.response = response
        if response[1] == "Tournament":
            return "Tournament_menu"
        if response[1] == None:
            pass
        if response[1] == "Player":
            return "Player_menu"
        if response[1] == "SaveAndLoad":
            return "SaveAndLoad_menu"  
        else:
            print("Un choix non prévu a été effectué en venant de {}"\
.format(response[0], response[1]))
            quit()


class FromPlayer:
    """Le menu FromPlayer permet à l'utilisateur d'accéder aux vues
    du menu de création et d'affichage de Joueur présentes dans le module
    views, de la manière : sh_pl.exemple_de_vue. 
    """
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
                print("\n{} {} | né(e) le {} | Sexe: {} | Classement: {}".format\
(player.first_name,player.last_name, player.birthdate, player.sex, player.ranking))
            return "Show_ranks_choices"

        if response[1] == "See_player_info":
            player_first_name = input('Entrez le prénom joueur\n')
            player_last_name = input('Entrez le nom de famille du joueur\n')
            for player in md.Player.PLAYERS:
                if player_first_name == player.first_name and \
                player_last_name == player.last_name:
                    print("{}--{}--{}--{}--{}\n\n".format(player.first_name, \
player.last_name, player.birthdate, player.sex, player.ranking))
                    return "Show_ranks_choices"
                print("\nCe joueur n'est pas enregistré \n")
                return "Show_ranks_choices"
            
        if response[1] == "Actualize_rank":
            player_first_name = input('Entrez le prénom joueur\n')
            player_last_name = input('Entrez le nom de famille du joueur\n')
            for player in md.Player.PLAYERS:
                if player_first_name == player.first_name and \
                player_last_name == player.last_name:
                    nb_players = len(md.Player.PLAYERS)
                    new_rank = int(input('Quel serait son nouveau classement sur \
{} joueurs ?\n'.format(nb_players)))
                    while new_rank > len(range(1, nb_players + 1)) or new_rank < 1:
                        print('Veuillez entrer un nouveau classement valide svp')
                        new_rank = input('Quel serait son nouveau classement sur \
{} joueurs ?\n'.format(nb_players))
                    if new_rank == player.ranking :
                        print("Erreur : le nouveau classement du joueur \
est le même que l'ancien")
                        return "Show_ranks_choices"
                    player.change_rank(new_rank)
                    print("\n le changement a bien été enregistré\n")
                    for player in md.Player.PLAYERS:
                        print("\n{} {} | né(e) le {} | Sexe: {} | Classement: {}".format\
(player.first_name,player.last_name, player.birthdate, player.sex, player.ranking))
                    return "Show_ranks_choices"

            print("\nCe joueur n'est pas enregistré \n")
            return "Show_ranks_choices"

        if response[1] == "Player_Menu":
            return "Player_menu"
        if response[1] == "SaveAndLoad":
            return "SaveAndLoad_menu"
        if response[1] == "Menu":
            return "Menu"
        else:
            print("Un choix non prévu a été effectué en venant de {}, {}".\
format(response[0], response[1]))
            quit()


class FromTournament:
    """Le menu FromTournament permet à l'utilisateur d'accéder aux vues
    du menu de création et d'affichage de tournoi présentes dans le module
    views, de la manière : sh_to.exemple_de_vue. 
    """
    def __init__(self):
        pass
        

    @classmethod
    def take_response(self, response):
        self.response = response
        if response[1] == "Create_tournament":
            if len(md.Player.PLAYERS) < 8:
                print("ERREUR : Il n'existe pas assez de joueurs \
enregistrés pour créer un tournoi")
                return "Tournament_menu"
            Tournament_list = sh_to.show_create_tournament()
            md.Tournament(Tournament_list[0], Tournament_list[1], \
Tournament_list[2], Tournament_list[3], Tournament_list[4], Tournament_list[5])
            return ["Create_matches", Tournament_list[0]]

        if response[1] == "Matches_result":
            tournament_name = response[2]
            tournament_and_round_index = sh_to.show_enter_matches(tournament_name)
            tournament = tournament_and_round_index[0]
            round_index = tournament_and_round_index[1]
            if round_index < (tournament.number_of_rounds - 1):
                return ["Create_matches", tournament_name]
            sh_to.show_tournament_ending(tournament_name)
            return "Tournament_menu"

        if response[1] == "Modify_tournament_info":
            print("Cette fonctionnalité n'a pas encore été implémentée")
            return "Tournament_menu"

        if response[1] == "Show_tournament_list":
            print("Cette fonctionnalité n'a pas encore été implantée")
            return "Tournament_menu"

        if response[1] == "Back_to_tournament_menu":
            return "Tournament_menu"

        if response[1] == "SaveAndLoad":
            return "SaveAndLoad_menu"
        if response[1] == "Menu":
            return "Menu"

        else:
            print("Un choix non prévu a été effectué en venant de {}".\
format(response[0], response[1]))
            quit()


class FromSaveAndLoad:
    """Le menu FromSaveAndLoad n'est pour l'instant pas implémenté, il permettra
     de sauvegarder toutes les instances de Joueurs et de Tournois enregistrés 
     dans la session où de charger des instances à partir d'un fichier .json.
    """

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
    """go_to_path permet de naviguer entre les menus à partir du résultat de take_option.
    Response est une liste constituée de deux à trois strings, le 1er string indique
    d'où l'on vient, le 2e string indique vers quel menu on veut aller, le 3e string
    peut indiquer le nom d'un tournoi. Chaque Menu comporte une Classe, possédant une
    méthode, take_response, qui permet de réduire la longueur totale de go_to_path en en
    séparant la logique.
    """
    if response[0] and response[1]:
            if response[1] == "Quit":
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
            if response[0] == "Tournament":
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

# LA BOUCLE NORMALE SANS AIDE AU DEBUGGAGE
def main():
    """La fonction main consiste essentiellement à afficher des choix à
    l'utilisateur, pour ensuite récupérer son input avec take_option(). 
    On utilisera ensuite son input pour naviguer dans les menus du
    programme avec go_to_path pour ensuite lui proposer à nouveau d'autres
    choix. 
    Cette boucle s'arrêtera avec l'arrêt du programme si l'utilisateur
    l'indique dans ses choix où si le programme reçoit une commande inconnue.
    """
    first_input = take_option()
    new_input = go_to_path(first_input)
    while True: 
        new_option = take_option(new_input)
        new_input = go_to_path(new_option)
        


# LA BOUCLE NORMALE AVEC AIDE AU DEBUGGAGE
# def main():
    # first_input = take_option()
    # new_input = go_to_path(first_input)
    # while True: 
    #     print("######################DEBUT DE LA BOUCLE#########################")
    #     new_option = take_option(new_input)
    #     print("NEW_OPTION : {}".format(new_option))
    #     if new_option[1] == "admin":
    #         break
    #     new_input = go_to_path(new_option)
    #     print("NEW_INPUT : {}".format(new_input))

# UNE BOUCLE ALTERNATIVE CHARGEANT 8 JOUEURS ET AMENANT DIRECTEMENT 
# À LA CRÉA DES MATCHES D'UN TOURNOI
# def main():
    
#     player1 = md.Player("John", "Doe", "12/01/1930", "M")
#     player2 = md.Player("Jane", "Doe", "17/04/1926", "F")
#     player3 = md.Player("Jojo", "Rabbit", "19/04/1928", "M")
#     player4 = md.Player("Joselaine", "Dabit", "20/04/1922", "F")
#     player5 = md.Player("Polo", "LePolo", "11/06/1815", "M")
#     player6 = md.Player("Carabine", "LeCarabin", "16/05/1982", "M")
#     player7 = md.Player("Canelle", "Doublekick", "12/11/1956", "F")
#     player8 = md.Player("Gaelle", "Belle", "12/11/1965", "M")

#     ex_tournament = md.Tournament("Exemple_tournament", "12/11/1999", "Las Vegas", \
# {1:["John", "Doe"], 2:["Jane", "Doe"], 3:["Jojo", "Rabbit"], 4:["Joselaine", "Dabit"], 5:["Polo", "LePolo"], \
# 6:["Carabine", "LeCarabin"], 7:["Canelle", "Doublekick"], 8:["Gaelle", "Belle"]}, "Bullet", "no_description")

#     new_option = take_option(["Create_matches", ex_tournament.name])
#     new_input = go_to_path(new_option)
#     while True: 
#         new_option = take_option(new_input)
#         if new_option[1] == "admin":
#             break
#         new_input = go_to_path(new_option)
        
        
    
if __name__ == "__main__":
    main()
