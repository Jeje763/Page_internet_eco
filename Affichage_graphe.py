import matplotlib.pyplot as plt
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

def affichage(X,Y,format,ordre="",couleur="black"):
     ordonne(X,Y,ordre) #notamment valable pour des histos
     if format=="histogramme":
          plt.bar(X,Y,edgecolor='black',color=couleur)
          plt.show()

