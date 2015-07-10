## Bibliothèques
import nltk
from fonctions_kernels import *

## kernel_sa : prend 2 forêts et renvoie Somme sur les couples nb_sous_abres(a1,a2) :
def kernel_sa(l_arbres1,l_arbres2):
    retour = 0
    for a1 in l_arbres1:
        for a2 in l_arbres2:
            retour += nb_sous_arbres(a1,a2)
    return retour;