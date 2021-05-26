# OpenCP4
---
Présentation
---
Cette application permet d'entrer les résultats de tournois d'échecs, et d'ajouter des joueurs dans une base de données réutilisable par la suite afin
de garder une trace de ceux-ci.

---
Fonctionnement
---
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

.flake8 sert indiquer à flake8 d'ignorer l'environnement virtuel

Data.json permet de sauvegarder et de charger des données à partir ou vers ce fichier

requirements.txt contient les librairies à installer avec pip pour faire fonctionner le programme

---
Instructions pour faire fonctionner le programme
---

 • Tout d'abord, téléchargez ces différents fichiers dans un dossier que vous choisirez. Créez ensuite dans ce dossier un environnement virtuel nommé : env
 
Par ex avec la commande : python -m venv env

Afin que flake8 puisse correctement ignorer ces fichiers lors de son initialisation.

 • La version de python utilisée pour faire fonctionner ce programme est la 3.8.0.
 
 • Utilisez la commande dans un éditeur de commande :
pip install -r /path/to/requirements.txt
où /path/to/requirements.txt est le chemin d'accès vers le fichier requirements.txt fourni dans ce repository

 • Exécutez ensuite le programme en tapant :
python3 main_controller.py

 • Pour générer un rapport flake8 (la librairies flake8 est inclus dans requirements.txt) avec le nombre de lignes fixé à 119, faites ensuite:
 
flake8 --max-line-length 119
