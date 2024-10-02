#%%Module
import sqlite3
#%%Création et conncextion à catégories
connection=sqlite3.connect("categorie.db")
cursor = connection.cursor()
try:
    cursor.execute("CREATE TABLE categorie (id INTEGER PRIMARY KEY AUTOINCREMENT,nom_cat TEXT)")
    connection.commit()
except:
    None
#%%Création et conncextion à catégories
connection2=sqlite3.connect("donnees.db")
cursor2= connection.cursor()
try:
    cursor.execute("CREATE TABLE donnees (id INTEGER PRIMARY KEY AUTOINCREMENT,id_cat INT,chiffre INT,annee INT)")
    connection.commit()
except:
    None
#%%Ajout des elt aux tables (E1)
def ajoute_une_categorie(nom):
    a="'"+nom+"'"
    requete="INSERT INTO categorie (nom_cat) VALUES("+a+")"
    cursor.execute(requete)
    connection.commit()
def ajoute_une_donnees(id_cat,chiffre,annee):
    a,b,c=str(id_cat),str(chiffre),str(annee)
    requete="INSERT INTO donnees (id_cat,chiffre,annee) VALUES("+a+","+b+","+c+")"
    cursor2.execute(requete)
    connection2.commit()
#%%Fonction d'affichage (E2)
def affiche_tous(nom_de_la_base):
    cursor2.execute("SELECT * FROM "+ nom_de_la_base)
    rows=cursor2.fetchall()
    for i in range(len(rows)):
        print(rows[i])
def trouve_numéro_une_categorie(nom_categories):
    """Renvoie l'identtifiant associé a la catégorie nom_categories"""
    requete="SELECT id FROM categorie WHERE nom_cat='"+nom_categories+"'"
    cursor.execute(requete)
    rows=cursor.fetchall()
    if rows==[]:#la catégorie n'existe pas
        return -1
    else:
        return int(rows[0][0])

def donnes_associer_a_une_categorie(nom_categories):
    """Affiche tt les donnees de la catégories nom_categories"""
    num=trouve_numéro_une_categorie(nom_categories)
    if num==-1:#la catégorie n'existe pas
        return []
    else:
        requete="SELECT * FROM donnees WHERE id_cat="+str(num)
        cursor.execute(requete)
        rows=cursor.fetchall()
        for i in range(len(rows)):
            print(rows[i])
        return rows
