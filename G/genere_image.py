## Import Librairies

import os
import pickle
from pylab import *
import matplotlib.pyplot as plt # Pour le graphique
#from PIL import Image as im

## Code

liste_gram = os.listdir()

for matrice_gram in liste_gram:
    if matrice_gram != 'genere_image.py':
        chemin = './'+matrice_gram
        # Chargement fichier
        fichier = open(chemin, 'rb')
        G = pickle.load(fichier)
        fichier.close()
        
        plt.imsave(matrice_gram+'.png',G,format='png')