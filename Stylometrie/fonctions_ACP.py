## Fichier de recodage de l'ACP

## Import des librairies

import numpy as np
import copy
import matplotlib.pyplot as plt
import pickle

## Code des fonctions utiles

# Kernel Euclidien
def kernel_eucl(X, Y):
    # Remarque: Le passage par les np.array accelère incroyablement les calculs
    X = np.array(X)
    Y = np.array(Y)
    return X.dot(Y.T);

# Fonction qui calcule la matrice de Gram associée à X, à condition que l'on fournisse le kernel
def gram(X, kernel=kernel_eucl):
    n = len(X)
    G = np.zeros((n, n), dtype = float)
    for i in range(n):
        for j in range(n):
            G[i, j] = G[j, i] = kernel(X[i], X[j])
        G[i, i] = kernel(X[i], X[i])
    return G;

# Centre la matrice de Gram selon un certain vecteur centre [selon la moyenne si on ne spécifie pas le vecteur]:
# Intérêt:  Centrer par rapport à d'autres choses que la moyenne, qui n'est pas toujours représentative des points que l'on considère.
def centrer(Gini, centre = None):
    G = copy.deepcopy(Gini)
    n = len(G)
    ones = np.ones((1,n), dtype =float)
    # Si le centre n'est pas spécifié, on choisit le barycentre de tous les points
    if centre==None:
        centre = ones
    # Codage du 'recentrage' à proprement parler
    poids = sum(centre[0]) # poids total pour le barycentre
    bar = (1/poids)*ones.T.dot(centre)
    G = G - bar.dot(G) - G.dot(bar) + bar.dot(G.dot(bar))
    return G;

# Fonction qui diagonalise une matrice symmétrique réelle
def composantes(G, n_components=2, divise_lambda = False):
    (l,v) = np.linalg.eigh(G)
    v = v[:, ::-1]
    l = l[::-1]
    print(l)
    retour = G.dot(v[:, 0:n_components])
    if divise_lambda:
        inv_rac = [(1/np.sqrt(i)) for i in l[0:n_components]]
        divise = np.diag(inv_rac)
        retour = retour.dot(divise)
    return retour;

# Fonction qui normalise une matrice
def reduire(G, normalise = True):
    if normalise:
        D = np.diagonal(G)
        D = [1/(np.sqrt(i)) for i in D]
        D = np.diag(D)
        G = D.dot(G.dot(D))
    return G;

## Fonction d'enregistrement et de chargement matrices de Gram

# A CORRIGER ***********************
def enregistre_gram(nom, G):
    chemin = './matrices_Gram/'+nom
    fichier = open(chemin, 'wb')
    pickle.dump(fichier, G)
    return;

def charge_gram(nom):
    chemin = './matrices_Gram/'+nom
    fichier = open(chemin, 'rb')
    G = fichier.load()
    return G;

## Fonction ACP à proprement parler

def ACP(X, n_components=None, kernel=kernel_eucl, centre = None, normalisee = True, divise_lambda = False, precomputed = False):
    # Réglages initiaux
    if n_components==None:
        n_components = 2
    # Fonction ACP à proprement parler
    G = gram(X, kernel)
    if precomputed:
        G = X
    G = centrer(G, centre)
    G = reduire(G, normalisee)
    V = composantes(G, n_components, divise_lambda = divise_lambda)
    return V;

## Fonction de dessin en 2D

def trace_ACP(X, titre = "", axes = None, numero = None):
    n = len(X)
    plt.figure(figsize=(8,8))
    for i in range(n):
        #if (findCol(i, nbArt, couleurs)!='g'):
        plt.plot(X[i,0], X[i,1], '+', c='k')#findCol(i, nbArt, couleurs)) 
    plt.title(titre)
    if axes != None:
        plt.axis(axes)
    plt.show()
    return;

## Centre de débuggage

def kernel(X, Y):
    retour = 0
    for i in range(len(X)):
        retour += X[i]*X[i]*Y[i]*Y[i]
    return retour;

X = [[2,4,5],[7,3,2],[1,3,2],[7,6,3],[0,4,2]]
V = ACP(X, n_components=3, normalisee = False, divise_lambda = True, kernel = kernel)
print("ACP", "\n", V)
trace_ACP(V)

from sklearn.decomposition import PCA
n_components = 3 # Pour projeter en 2D
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
print("X_pca", "\n", X_pca)
trace_ACP(X_pca)

from sklearn.decomposition import KernelPCA
G = gram(X)
kACP = KernelPCA(n_components = 3, kernel = kernel)
X_kpca = kACP.fit_transform(X)
print("X_kpca", "\n", X_kpca)
trace_ACP(X_kpca)

X_2 = ACP(G, n_components=3, normalisee = False, divise_lambda = True, precomputed = True)
print("X_2", "\n", X_2)
trace_ACP(X_2)