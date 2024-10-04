#%%
import matplotlib.pyplot as plt
import numpy as np

#IL PEUT ETRE INTERESSANT DE RAJOUTER UNE OPTION COMME LE POURCENTAGE MINIMUM MAIS POUR LE HISTOGRAMMES
#%%
if True:  #fonction d'ajustement des données
     def mirroir(L):
          n=len(L)
          for k in range(n//2):
               L[k],L[n-1-k]=L[n-1-k],L[k]
     def tri_croissant(X,Y):
          """ Tri selon la composante de Y (la vrai donnée)"""
          n=len(Y) #=len(X)
          for j in range(1,n):
               for i in range(1,n):
                    if Y[i] < Y[i-1]:
                         Y[i-1],Y[i] =Y[i],Y[i-1]
                         X[i-1],X[i] =X[i],X[i-1]
     def tri_decroissant(X,Y):
          """ Tri selon la composante de Y (la vrai donnée)"""
          tri_croissant(X,Y)
          mirroir(X)
          mirroir(Y)     
     def ordonne(X,Y,ordre):
          if ordre=="croissant":
               tri_croissant(X,Y)
          elif ordre=="décroissant":
               tri_decroissant(X,Y)
          else:
               None
     def ajuste(X,pourc,minimum_pourcent_pie):
          ordonne(X,pourc,"croissant")
          while pourc[0]<minimum_pourcent_pie:
               del X[0]
               del pourc[0]
          s=sum(pourc)
          if s!=100:
               X.append("autre")
               a=100-s
               pourc.append(int(10*a)/10)
def affichage(X,Y,format,L):
     """L est la liste des options/paramètre"""
     if True:#récupère toute les options
          #générique 
          ordre,couleur=L[0],L[1]
          titre,nom_grandX,nom_grandY=L[2],L[3],L[4]
          #histogramme
          horizontalite=L[5]
          #courbe
          nom_legend,legend,reg_lin,coul_reg_lin=L[6],L[7],L[8],L[9] #légende pour une courbe
          #camembert
          label_pie,affiche_pour,affichage_total=L[10],L[11],L[12]
          minimum_pourcent_pie=L[13]
     if True: #ordre,titre,nom grandeur X,nom grandeur Y
          ordonne(X,Y,ordre)
          plt.title(titre)
          plt.xlabel(nom_grandX)
          plt.ylabel(nom_grandY)
     if format=="histogramme":
          if horizontalite:
               plt.barh(X,Y,edgecolor='black',color=couleur)
          else:
               plt.bar(X,Y,edgecolor='black',color=couleur)
     if format=="courbe":
          if legend:
               plt.plot(X,Y,color=couleur,label=nom_legend)
          else:
               plt.plot(X,Y,color=couleur)
          if reg_lin:
               a,b=np.polyfit(X,Y,1)
               Y_reg=[a*x+b for x in X]
               if legend:
                    plt.plot(X,Y_reg,color=coul_reg_lin,label="Régression linéaire")
               else:
                    plt.plot(X,Y_reg,color=coul_reg_lin)
          if legend:
               plt.legend()
     if format=="camembert":
          s=sum(Y)
          pourc=[int(1000*y/s)/10 for y in Y]
          ajuste(X,pourc,minimum_pourcent_pie)
          print(X)
          print(pourc)
          print(minimum_pourcent_pie)
          if affiche_pour:
               label_pie=True
               X=[X[k]+"\n"+str(pourc[k])+"%" for k in range(len(X))]
          if affichage_total:
               plt.figtext(0.1, 0.1,"Total= "+str(int(1000*s)/1000))
          if label_pie:
               plt.pie(pourc,labels=X)
          else:
               plt.pie(pourc)

Opt=["croissant","blue","Titre_graphe","GX","GY",True,"Leg",True,True,"blue",True,True,True,25]
affichage(["AAA","B","C","D"],[1.5,3.7,2.65,6.294],"histogramme",Opt)
# %%
