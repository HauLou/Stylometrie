## Import Librairies

import os
import pickle
from pylab import *
import matplotlib.pyplot as plt # Pour le graphique
import numpy as np
import copy

## import dégueu

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
    
# Fonction qui normalise une matrice
def reduire(G, normalise = True):
    if normalise:
        D = np.diagonal(G)
        D = [1/(np.sqrt(i)) for i in D]
        D = np.diag(D)
        G = D.dot(G.dot(D))
    return G;

## Code

liste_gram = os.listdir()

for matrice_gram in liste_gram:
    taille = len(matrice_gram)
    if matrice_gram.split('.')[1] == 'txt':
        chemin = './'+matrice_gram
        # Chargement fichier
        fichier = open(chemin, 'rb')
        G = pickle.load(fichier)
        fichier.close()
        
        #G = reduire(G)
        #G = centrer(G)
        #G = reduire(G)
        
        plt.imsave(matrice_gram.split('.')[0]+'.png',G,format='png')