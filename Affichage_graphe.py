#%%
import matplotlib.pyplot as plt
import numpy as np
#%%
if True:
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

def affichage(X,Y,format,L):
     """L est la liste des options/paramètre"""
     ordre,couleur=L[0],L[1]
     titre,nom_grandX,nom_grandY=L[2],L[3],L[4]
     affich_titre,affich_grandX,affich_grandY=L[5],L[6],L[7]
     nom_legend,legend,reg_lin,coul_reg_lin=L[8],L[9],L[10],L[11] #légende pour une courbe
     ordonne(X,Y,ordre)
     if True: #titre,nom grandeur X,nom grandeur Y
          if affich_titre:
               plt.title(titre)
          if affich_grandX:
               plt.xlabel(nom_grandX)
          if affich_grandY:
               plt.ylabel(nom_grandY)
     if format=="histogramme":
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
          #A Completer
Opt=["","black","Titre_graphe","GX","GY",True,True,True,"Leg",True,True,"blue"]
affichage([1,2,3,4,5],[2,4,7,7,10],"courbe",Opt)
# %%
