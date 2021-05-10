# OpenCP4

Le fichier Model.py correspond aux classes Player, Tournament, Match, Round

Le fichier Views.py correspond aux vues et différents messages de menus s'affichant dans le programme

Le fichier Controller.py importe les classes de Model.py et Views.py pour ensuite les utiliser avec ses fonctions :

*take_option()* qui prend en paramètre un string contenant le nom de la vue à afficher et qui prends ensuite un input
qui sera retourné dans une liste avec le nom du menu actuel en 1er.

*go_to_path()* qui prend en paramètre deux strings dans une liste qui contiennent de quelle vue on vient et vers
quelle vue l'utilisateur a décidé d'aller. 

Ces deux fonctions sont mises dans une boucle while qui fait en sorte que l'une appelle l'autre à l'infini jusqu'à 
ce que l'utilisateur choisisse une option lui permettant de quitter le programme.
