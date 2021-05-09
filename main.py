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
# OBJECTIF PSEUDO-CODE

# Voir comment créer tout avec le MVC en tête et PEP8 / PEP20


""" importer les fonctions du fichier Vues.py """
""" importer les autres modules nécessaires """

# mettre cette fonction et l'améliorer dans le fichier Vues.py
# def print_menu_options():
#     titre_page = "MENU"
#     print("Bienvenue sur la page de {title}".format(title=titre_page))
#     print("Quelle action souhaitez vous effectuer?")

"""fonction permettant de récupérer les arguments passés dans le programme via l'invite de commande
Si il est passé ce mot-clé, avec possiblement cet argu2ment, alors ...
Sinon renvoyer un message d'erreur et inviter à réessayer
"""
def take_option(option=False):
        if not option:
            sh_me.show_menu()
            new_option = input()
            menu_dict = {1:"Tournament", 2:"Player", 4:"SaveAndLoad", 5:"Quit"}
            if new_option not in ["1","2","3","4","5"]:
                print("Veuillez uniquement entrer une des options proposées")
                take_option()
            else :
                new_option = int(new_option)
                path = menu_dict[new_option]
                return ["Menu", path]
        
        elif option == "Menu":
            sh_me.show_menu()
            new_option = input()
            menu_dict = {1:"Tournament", 2:"Player", 4:"SaveAndLoad", 5:"Quit"}
            if new_option not in ["1","2","3","4","5"]:
                print("Veuillez uniquement entrer une des options proposées")
                take_option()
            else :
                new_option = int(new_option)
                path = menu_dict[new_option]
                return ["Menu", path]

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

        elif option == "Player_menu":
            pass

        elif option == "SaveAndLoad_menu":
            pass

            

            
        else :
            pass
            
                # else:
                #     print("Veuillez uniquement entrer une des options proposées")
                #     path = response[0]
                #     new_option = input()
                #     take_option([path, new_option])
            # else :
            #     raise Exception('!!! No path nor option number provided !!!')
 
def go_to_path(response):
    if response[0] and response[1]:
        if response[1] == "Quit":
            # afficher message, sûr de quitter?
            # Faudrait aussi que vérifie qu'a bien sauvegardé non?
            views.show_exit()
            sure = input()
            if sure not in ["1", "2"]:
                print("Veuillez uniquement entrer une des options proposées")
                got_to_path(response)
            elif sure == "1":
                quit()
            elif sure == "2":
                return response[0]

        if response[0] == "Menu" :
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
                print("Un choix non prévu a été effectué")
                quit()

        if response[0] == "Tournament":
            if response[1] == "Create_tournament":
                Tournament_list_of_values = sh_to.show_create_tournament()
                return "Create_matches"
            else:
                print("Un choix non prévu a été effectué")
                quit()
        if response[0] == "Tournament_creation":
            if response[1] == "":
                Tournament_list_of_values = sh_to.show_create_tournament()
                return ""
            else:
                print("Un choix non prévu a été effectué")
                quit()
    else :
        raise Exception('!!! No path nor option number provided !!!')


def main():
    first_input = take_option()
    new_input = go_to_path(first_input)
    while True: 
        new_option = take_option(new_input)
        new_input = go_to_path(new_option)
        

if __name__ == "__main__":
    main()


"""Ce qui se passe quand on lance l'application
(---La data se charge)?
---La page du menu s'affiche avec des print sur plusieurs lignes
---On a l'option 1 Créer un tournoi / Afficher rapport tournoi
---On a l'option 2 Créer un joueur / Afficher rapport joueur
---On a l'option 3 Mettre à jour le classement
---On a l'option 4 Sauvegarder / Charger les Données
---On a l'option 5 Quitter l'application
"""

"""Ce qui se passe quand on répond créer un tournoi
---la data se charge (cf voir p122 code n°4 pour import json et lire fichier)
---les tournois s'affichent par ordre chronologique, du dernier au 1er entré
---On a l'option 1 Créer un tournoi
------Les nouvelles options s'affichent
------"Entrez les informations de votre nouveau tournoi"
------Nom & Date & Lieu & Nb Tours & Tournée & Joueurs & Temps & Description
------"Ces informations sont-elles incorrectes ou voulez-vous générer les 1eres paires de joueurs?"
------Génération de la 1ère paire de joueur
------"Entrez maintenant le résultat des matchs"
------Option Quitter
------Option Sauvegarder
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
message d'erreur.
---On a l'option 2 Faire défiler la liste des tournois vers le bas ou le haut
---On a l'option 3 Choisir un tournoi particulier par son nom 
------Les nouvelles options s'affichent
------Option 1 Modifier des informations de ce tournoi
---------Option 1 Modifier les informations générales
------------Pour chaque option, est-ce valide ou voulez-vous la modifier?
---------Option 2 Modifier les informations d'un match
------------Voici les différents matches joués et leur résultat, lequel souhaitez-vous modifier ? back pour revenir en arrière
------Option 2 Afficher informations de ce tournoi
---------Option 1 Afficher informations générales
---------Option 2 Afficher les matches
------------Afficher les résultats des tours d'un match particulier ou back
---------Option 3 back
------Option 3 Choisir un autre tournoi qui renvoie vers une autre invite de nom
------Option 4 Revenir à la page de tournoi
---On a l'option 4 Revenir au menu
---On a l'option 5 Sauvegarde rapide ou aller à la page de sauvegarde / Chargement des données
---On a l'option 6 Quitter le programme
"""

"""Ce qui se passe quand on répond créer un joueur
---la data se charge
---les joueurs s'affichent par ordre de classement
---On a l'option 1 Mettre à jour le classement
------"Entrez le nom du joueur dont vous voulez modifier le classement: "
---On a l'option 2 Créer un nouveau joueur
---Si le joueur existe déjà, on a un message d'erreur
------"Entrer les informations du joueur"
---On a l'option 3 Dérouler la liste
------Vers un coté ou vers un autre
---On a l'option 4 Afficher les joueurs par ordre alphabétique
------Qui devra ensuite proposer d'afficher les joueurs par ordre chronologique
---On a l'option 5 Afficher les informations d'un joueur en particulier 
------On a l'option 1 Modifier les informations d'un joueur
---------Pour chaque info, est-ce correct ou voulez-vous la modifier?
------On a l'option 2 back
---On a l'option 6 Revenir au menu
---On a l'option 7 Sauvegarde rapide ou aller à la page de sauvegarde / Chargement des données
---On a l'option 8 Quitter le programme
"""

"""Ce qui se passe quand on répond Sauvegarder / Charger les données
---La data se charge
---Toutes les sauvegardes antérieures sont affichées (ou genre les 5 dernières suivant la mémoire?)
---Option 1 Charger les données
---Option 2 Sauvegarder les données
"""

"""Ce qui se passe quand on répond Quitter l'application
---Entrer la commande quit() et le programme s'arrête
---à part si on a pas sauvegardé les derniers changements, dans ce cas programme en s'arrête pas et message d'erreur
"""


