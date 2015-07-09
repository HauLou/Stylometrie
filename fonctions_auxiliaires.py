## Import Librairies

import os

## Fonction qui renvoie la liste des 'directories'

def liste_dossiers(chemin):
    retour = []
    liste = os.listdir(chemin)
    for element in liste:
        if os.path.isdir(element) and element[0]!= '.':
            retour.append(element)
    return retour;

