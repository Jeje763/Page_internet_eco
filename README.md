# Page_internet_eco
-L'image indique la décomposition du projet de page en sous projet plus simple. 

-La base de données SQL a été créer a la 'main' (grâce aux fonctions d'ajout fait dans le fichier python associées). 

-Le fichier "Affichage_graphe(E3).py" n'est pas un vrai fichier du projet. Il est juste un 'grand' extrait du fichier python principal et permet de mieux comprendre le traitement des données afin de tracer le graphique.
En effet, le code python a été recopier dans le fichier recup_donnee.py avec quelque ajustement afin de pouvoir utiliser le module Flask.

-Je n'arrive pas a mettre des dossiers dans git (et les construires donc voici un schéma des dossier pour que cela fonction:

-Projet
    -templates
        -page_acceuil.html
        -page_affichage_graphique.html
    -static
        -style_visuel_page.css
        -images (UN DOSSIER QUI CONTIENDRA TEMPORAIREMENT LE GRAPHIQUE)
    -recup_donnee.py (1) 
    -gestion_base_donnes(E1_et_E2).py
    -categorie.db
    -donnees.db

-Pour lancer l'application, j'execute la commande suivante: python Projet/recup_donnee.py (1)
Module nécessaire:  flask , os, numpy , matplotlib , sqlite3

(1): la dernière ligne de code  du fichier recup_donnee.py peut être modifier afin de changer le port en cas de problème.
