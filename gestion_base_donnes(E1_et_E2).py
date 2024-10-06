#%%Module
import sqlite3
#%%Création et conncextion à catégories
connection=sqlite3.connect("data/categorie.db")
cursor = connection.cursor()
try:
    cursor.execute("CREATE TABLE categorie (id INTEGER PRIMARY KEY AUTOINCREMENT,nom_cat TEXT)")
    connection.commit()
except:
    None
#%%Création et conncextion à donnees
connection2=sqlite3.connect("data/donnees.db")
cursor2= connection.cursor()
try:
    cursor2.execute("CREATE TABLE donnees (id INTEGER PRIMARY KEY AUTOINCREMENT,id_cat INT,chiffre INT,annee INT)")
    connection2.commit()
except:
    None
#%%Ajout des elt aux tables
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
#%%Fonction d'affichage
def affiche_tous(nom_de_la_base):
    cursor2.execute("SELECT * FROM "+ nom_de_la_base)
    rows=cursor2.fetchall()
    print(len(rows))
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
def met_au_format(rows):   
    Chi=[ r[2] for r in rows] #chiffre
    An=[ r[3] for r in rows] #date
    return Chi,An
def requete_au_bon_format(nom_categories):
    return met_au_format(donnes_associer_a_une_categorie(nom_categories))
# %%
affiche_tous("categorie")
#%%
affiche_tous("donnees")
# %%Création de la base catégorie dans un cas concret
if True:
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (-50h, 0-99 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (51-65h, 0-99 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (+65h, 0-99 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (-50h, 100-199 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (51-65h, 100-199 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (+65h, 100-199 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (-50h, 200-399 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (51-65h, 200-399 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (+65h, 200-399 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (-50h, +400 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (51-65h, +400 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (+65h, +400 places)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (-50h)")
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (51-65h)")             
    ajoute_une_categorie("Amplitude d’ouverture des bibliothèques universitaires (+65h)")
# %%Création de la base donnees dans un cas concret
def ajoute_liste(L,annee):
    for i in range(1,16):
        ajoute_une_donnees(i,L[i-1],annee)
if True:
    L_2022=[173,41,7,41,47,8,9,56,25,13,66,69,236,210,109]
    L_2021=[187,44,7,37,48,9,9,54,22,3,67,63,236,213,101]
    L_2020=[185,47,5,37,45,8,7,60,18,4,69,65,233,221,96]
    L_2019=[193,42,6,41,43,8,7,57,19,4,72,62,245,214,95]
    L_2018=[183,44,6,36,46,7,10,52,20,4,72,55,233,214,88]
    L_2017=[182,49,6,40,43,10,10,54,17,4,69,55,236,215,88]
    L_2016=[162,36,6,27,31,8,11,51,10,0,50,38,200,168,62]
    ajoute_liste(L_2022,2022)
    ajoute_liste(L_2021,2021)
    ajoute_liste(L_2020,2020)
    ajoute_liste(L_2019,2019)
    ajoute_liste(L_2018,2018)
    ajoute_liste(L_2017,2017)
    ajoute_liste(L_2016,2016)
# %%
