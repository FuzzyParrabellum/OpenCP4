#! /usr/bin/env python3
# coding: utf-8

import model as md

from views import ShowMenu as sh_me
from views import ShowPlayer as sh_pl
from views import ShowTournament as sh_to
from views import ShowSaveAndLoad as sh_sa
from views import show_exit

from controllers_supp.take_response_classes import FromMenu, FromTournament, FromPlayer, FromSaveAndLoad, SaveAndLoad


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
            take_option(option)
        else :
            new_option = int(new_option)
            path = menu_dict[new_option]
            return ["Menu", path]

    #Si l'on veut aller dans la CREATION DE TOURNOI
    elif option == "Tournament_menu":
        sh_to.show_tournament()
        tournament_menu_dict = {1:"Create_tournament", 2:"Show_tournament_list", \
3:"Menu", 4:"SaveAndLoad", 5:"Quit"}
        new_option = input()
        if new_option not in ["1","2","3","4","5","6"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option(option)
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
            take_option(option)
        else:
            new_option = int(new_option)
            path = create_tournament_dict[new_option]
            return ["Tournament", path, option[1]]

    elif option == "Tournament_list_choices":
        sh_to.show_tournaments_status_options()
        tournaments_status_dict = {1:"Select_tournament", 2:"Back_to_tournament_menu", \
3:"SaveAndLoad", 4:"Quit"}
        new_option = input()
        if new_option not in ["1","2","3","4"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option(option)
        else:
            new_option = int(new_option)
            path = tournaments_status_dict[new_option]
            return ["Tournament", path]

    elif option[0] == "Tournament_status_choices":
        chosen_tournament = option[1]
        sh_to.show_tournament_status()
        chosen_tournament_status_dict = {1:"Show_rounds", 2:"Show_tournament_matches", \
3:"Modify_tournament_info", 4:"Tournament_players_alphab", 5:"Tournament_players_ranked", 6:"Show_tournament_list"}
        new_option = input()
        if new_option not in ["1","2","3","4", "5","6"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option(option)
        else:
            new_option = int(new_option)
            path = chosen_tournament_status_dict[new_option]
            return ["Tournament", path, chosen_tournament]

    # Si on veut aller dans la CREATION DE JOUEUR
    elif option == "Player_menu":
        sh_pl.show_player()
        player_menu_dict = {1:"Create_player", 2:"Show_ranks", \
3:"Menu", 4:"SaveAndLoad", 5:"Quit"}
        new_option = input()
        if new_option not in ["1","2","3","4","5","6"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option(option)
        else:
            new_option = int(new_option)
            path = player_menu_dict[new_option]
            return ["Player", path]
    elif option == "Show_ranks_choices":
        sh_pl.show_ranks()
        # possibilité de rajouter un défilement des joueurs
        ranks_menu_dict = {1:"See_player_info", 2:"Actualize_rank", 3: "Alphabetical_order", \
4:"Ranking_order", 5:"Player_Menu"}
        new_option = input()
        if new_option not in ["1","2","3","4","5"]:
            print("Veuillez uniquement entrer une des options proposées")
            take_option(option)
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
            take_option(option)
        else:
            new_option = int(new_option)
            path = SaveAndLoad_menu_dict[new_option]
            return ["SaveAndLoad", path]
        
    else :
        print("Navigation not found")
        pass

#########################################
#########################################

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
# def main():
#     """La fonction main consiste essentiellement à afficher des choix à
#     l'utilisateur, pour ensuite récupérer son input avec take_option(). 
#     On utilisera ensuite son input pour naviguer dans les menus du
#     programme avec go_to_path pour ensuite lui proposer à nouveau d'autres
#     choix. 
#     Cette boucle s'arrêtera avec l'arrêt du programme si l'utilisateur
#     l'indique dans ses choix où si le programme reçoit une commande inconnue.
#     """
#     first_input = take_option()
#     new_input = go_to_path(first_input)
#     while True: 
#         new_option = take_option(new_input)
#         new_input = go_to_path(new_option)
        


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
def main():
    
    player1 = md.Player("John", "Doe", "12/01/1930", "M")
    player2 = md.Player("Jane", "Doe", "17/04/1926", "F")
    player3 = md.Player("Jojo", "Rabbit", "19/04/1928", "M")
    player4 = md.Player("Joselaine", "Dabit", "20/04/1922", "F")
    player5 = md.Player("Polo", "LePolo", "11/06/1815", "M")
    player6 = md.Player("Carabine", "LeCarabin", "16/05/1982", "M")
    player7 = md.Player("Canelle", "Doublekick", "12/11/1956", "F")
    player8 = md.Player("Gaelle", "Belle", "12/11/1965", "M")

    ex_tournament = md.Tournament("Other_exemple", "10/11/1990", "Las Parano", \
{1:["John", "Doe"], 2:["Jane", "Doe"], 3:["Jojo", "Rabbit"], 4:["Joselaine", "Dabit"], 5:["Polo", "LePolo"], \
6:["Carabine", "LeCarabin"], 7:["Canelle", "Doublekick"], 8:["Gaelle", "Belle"]}, "Bullet", "no_description")

    new_option = take_option(["Create_matches", ex_tournament.name])
    new_input = go_to_path(new_option)
    while True: 
        new_option = take_option(new_input)
        if new_option[1] == "admin":
            break
        new_input = go_to_path(new_option)
        
        
    
if __name__ == "__main__":
    main()
