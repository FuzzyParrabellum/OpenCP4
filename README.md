# OpenCP4

Le fichier Model.py correspond aux classes Player, Tournament, Round

Le fichier Views.py correspond aux vues et différents messages de menus s'affichant dans le programme

Le fichier Controller.py importe les classes de Model.py et Views.py pour ensuite les utiliser avec ses fonctions :

*take_option()* qui prend en paramètre un string contenant le nom de la vue à afficher et qui prends ensuite un input
qui sera retourné dans une liste avec le nom du menu actuel en 1er.

*go_to_path()* qui prend en paramètre deux strings dans une liste qui contiennent de quelle vue on vient et vers
quelle vue l'utilisateur a décidé d'aller. 

Ces deux fonctions sont mises dans une boucle while qui fait en sorte que l'une appelle l'autre à l'infini jusqu'à 
ce que l'utilisateur choisisse une option lui permettant de quitter le programme.

Il existe également un dossier annexe appelé controller_supp qui permet de continuer l'action du fichier Controller.py
sans le surcharger en lignes de code. C'est dans ce dossier qu'est utilisé TinyDB pour sauvegarder et charger 
les données rentrées dans le programme.
-------------------
.flake8 sert indiquer à flake8 d'ignorer l'environnement virtuel
Data.json permet de sauvegarder et de charger des données à partir ou vers ce fichier
requirements.txt contient les librairies à installer avec pip pour faire fonctionner le programme

Pour utiliser flake8 afin d'afficher un rapport des anomalies présentes dans le programme, faire
python3 flake8 une fois dans le dossier contenant le programme.

IMPORTANT : Le rapport flake8 fourni par flake8 comporte actuellement des erreurs générées par flake8,
il ne reconnait pas certains modules importés dans le programme.

