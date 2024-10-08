from flask import Flask, request, render_template
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Utilisation du backend non interactif
import matplotlib.pyplot as plt
import sqlite3


if True:#Base de donnée
     def get_db_connection(db_name):
          db_path = os.path.join(os.path.dirname(__file__), db_name)  # Chemin absolu
          conn = sqlite3.connect(db_path, check_same_thread=False)
          conn.row_factory = sqlite3.Row
          return conn
  # Connexion aux bases de données avec l'option multithread
     connection = get_db_connection("data/categorie.db")
     connection2 = get_db_connection("data/donnees.db")
     cursor = connection.cursor()
     cursor2 = connection2.cursor()
     # Création des tables si elles n'existent pas
     try:
          cursor.execute("CREATE TABLE IF NOT EXISTS categorie (id INTEGER PRIMARY KEY AUTOINCREMENT, nom_cat TEXT)")
          connection.commit()
     except:
          None
     try:
          cursor2.execute("CREATE TABLE IF NOT EXISTS donnees (id INTEGER PRIMARY KEY AUTOINCREMENT, id_cat INT, chiffre INT, annee INT)")
          connection2.commit()
     except :
          None

     #Ajout des elt aux tables
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
     #Fonction d'affichage
     def affiche_tous(nom_de_la_base):
          cursor2.execute("SELECT * FROM "+ nom_de_la_base)
          rows=cursor2.fetchall()
          for row in rows:
               print(dict(row))
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
          print(f"long: {len(rows)}")
          Chi=[ r[2] for r in rows] #chiffre
          An=[ r[3] for r in rows] #date
          return Chi,An
     def requete_au_bon_format(nom_categories):
          return met_au_format(donnes_associer_a_une_categorie(nom_categories))
if True:# Fonctions de traitement des données et d'affichage
     def mirroir(L):
          n = len(L)
          for k in range(n // 2):
               L[k], L[n - 1 - k] = L[n - 1 - k], L[k]
     def tri_croissant(X, Y):
          n = len(Y) # =len(X)
          for j in range(1, n):
               for i in range(1, n):
                    if Y[i] < Y[i - 1]:
                         Y[i - 1], Y[i] = Y[i], Y[i - 1]
                         X[i - 1], X[i] = X[i], X[i - 1]
     def tri_decroissant(X, Y):
          tri_croissant(X, Y)
          mirroir(X)
          mirroir(Y)
     def ordonne(X, Y, ordre):
          if ordre == "croissant" or ordre=="croissant":
               tri_croissant(X, Y)
          elif ordre == "décroissant" or ordre == "decroissant":
               tri_decroissant(X, Y)
     def ajuste(X, pourc, minimum_pourcent_pie):
          ordonne(X, pourc, "croissant")
          while pourc!=[] and pourc[0] < minimum_pourcent_pie:
               del X[0]
               del pourc[0]
          s = sum(pourc)
          if s != 100:
               X.append("autre")
               a = 100 - s
               pourc.append(int(10 * a) / 10)
     def affichage(X, Y, format, L, adresse):
          ordre, couleur = L[0], L[1]
          titre, nom_grandX, nom_grandY = L[2], L[3], L[4]
          horizontalite = L[5]
          nom_legend, legend, reg_lin, coul_reg_lin = L[6], L[7], L[8], L[9]
          label_pie, affiche_pour, affichage_total = L[10], L[11], L[12]
          minimum_pourcent_pie = L[13]

          ordonne(X, Y, ordre)
          plt.title(titre)
          plt.xlabel(nom_grandX)
          plt.ylabel(nom_grandY)
          plt.xticks(X,label=[str(x) for x in X])
          if format == "Histogramme":
               if horizontalite:
                    plt.barh(X, Y, edgecolor='black', color=couleur)
               else:
                    plt.bar(X, Y, edgecolor='black', color=couleur)

          if format == "Courbe":
               plt.plot(X, Y, color=couleur, label=nom_legend if legend else "")
               if reg_lin:
                    a, b = np.polyfit(X, Y, 1)
                    Y_reg = [a * x + b for x in X]
                    plt.plot(X, Y_reg, color=coul_reg_lin, label="Régression linéaire" if legend else "")
               if legend:
                    plt.legend()

          if format == "Camembert":
               s = sum(Y)
               pourc = [int(1000 * y / s) / 10 for y in Y]
               ajuste(X, pourc, minimum_pourcent_pie)
               if affiche_pour:
                    X = [f"{X[k]}\n{pourc[k]}%" for k in range(len(X))]
               if affichage_total:
                    plt.figtext(0.1, 0.1, f"Total= {int(1000 * s) / 1000}")
               plt.pie(pourc, labels=X if label_pie else None)
          try: #enleve l'ancien graphique
               os.remove(adresse)
          except:
               None
          plt.savefig(adresse)
          plt.close()
          print(f"Image saved at: {adresse}")
# Configuration de l'application Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page_affichage_graphique.html')

@app.route('/page_acceuil')
def index2():
    return render_template('page_acceuil.html')
@app.route('/', methods=['GET', 'POST'])
def submit():
    image_path = None
    if request.method == 'POST' or request.method=='GET':
        if True:
            if True: #option générique
               categorie = request.form.get('Categorie_donnee')
               graph_type = request.form.get('format_graph')
               titre_graph = request.form.get('Titre_graph')
               nom_axe_x = request.form.get('Nom_axe_x')
               nom_axe_y = request.form.get('Nom_axe_y')
               couleur = request.form.get('Couleur')
            if True:# Options spécifiques à chaque type de graphe
               # Options spécifiques à chaque type de graphe
               ordre = request.form.get('ordre')
               horizontalite = request.form.get('horizont') == 'True'  # Conversion en booléen
               # Options pour les courbes
               reg_lin = request.form.get('reg') == 'True'  # Conversion en booléen
               couleur_reg = request.form.get('Couleur_reg')
               legend = request.form.get('legend') == 'True'  # Conversion en booléen
               nom_legend = request.form.get('nom_legend')
               # Options pour les camemberts
               label_pie = request.form.get('label_pie') == 'True'  # Conversion en booléen
               affiche_pour = request.form.get('affiche_pource') == 'True'  # Conversion en booléen
               affichage_total = request.form.get('affichage_total') == 'True'  # Conversion en booléen
               minimum_pourcent_pie_str = request.form.get('minimum_pourcent_pie', default=0)
               try:
                   minimum_pourcent_pie = float(minimum_pourcent_pie_str)
               except ValueError:
                   minimum_pourcent_pie = 0.0  # Valeur par défaut en cas d'erreur
          # Traiter les données pour générer un graphique
        Y,X=requete_au_bon_format(categorie)
        Y, X = requete_au_bon_format(categorie)
        print(f"Valeurs X : {X}, Valeurs Y : {Y}")
        print(f"{categorie}+ {type(categorie)}")

        options = [ordre, couleur, titre_graph, nom_axe_x, nom_axe_y, horizontalite, 
                   nom_legend, legend, reg_lin, couleur_reg, label_pie, affiche_pour, 
                   affichage_total, minimum_pourcent_pie]
        for i in [graph_type]:
            print(f""+str(i)+str(type(i)))
            print(f""+str(i)+str(type(i)))
            print(f""+str(i)+str(type(i)))
        
        # Chemin pour enregistrer l'image dans le dossier 'static/images'
        image_name = "Image_plt.png"
        image_folder = os.path.join('Page_internet_eco','static', 'images')
        image_path = os.path.join(image_folder, image_name)
        # Crée le dossier 'static/images' s'il n'existe pas
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        # Génération du graphique avec affichage
        affichage(X,Y, graph_type, options, image_path)
        image_name = "Image_plt.png"
        image_folder = os.path.join('static', 'images')
        image_path = os.path.join(image_folder, image_name)

        # Envoyer l'image au template HTML
        return render_template('page_affichage_graphique.html', image=image_path)

if __name__ == '__main__':
    app.run(debug=True)

#%%
affiche_tous('categorie')
# %%
