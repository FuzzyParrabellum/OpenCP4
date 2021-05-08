#! /usr/bin/env python3
# coding: utf-8
import os
import json

import model
from views import Navigation as nav
from views import ShowPlayer as sh_pl
from views import ShowTournament as sh_to
from views import ShowSaveAndLoad as sh_sa

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

def main():
    response = nav.navigate()
    new_response = nav.navigate(response)
    while True: 
        if new_response[0] == "Menu" :
            if new_response[1] == "Tournament":
                
        # penser à mettre le choix d'affichage du classement
            if new_response[1] == None:
                pass
            if new_response[1] == "Player":
                pass
            if new_response[1] == "SaveAndLoad":
                pass
            else:
                print("Un choix non prévu a été effectué")
                break
        

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


