## Librairies

# from fonctions_ACP import *
# import nltk
# from nltk.probability import FreqDist
# from fonctions import *
# import pickle

## Fréquence de natures de mots

def vecteur_frequence_nature(liste_natures):
    # liste des natures utilisées. [pour l'instant : len(liste_natures) = 53 ]
    listeNatures = ['LS', 'NN', 'VBZ', 'IN', 'DT', '.', 'WRB', 'NNS', 'NNP', 'JJ', 'JJR', 'VBP', 'MD', 'VB', 'PRP', 'VBD', 'VBN', ',', 'JJS', 'EX', 'CC', 'RB', 'TO', 'CD', 'VBG', ':', 'RP', 'WP', 'PRP$', '-NONE-', 'WDT', 'RBR', 'RBS', 'PDT', 'NNPS', '$', 'WP$', "''", 'POS', '``', '#', 'FW','UH','SYM']
    # initialisation du vecteur que l'on va remplir et que l'on renverra
    taille_vecteur = len(listeNatures) 
    # initialisation du vecteur que l'on renverra
    X = [0]*taille_vecteur

    nb_mots = len(liste_natures)
    for nat in liste_natures:
        X[listeNatures.index(nat)] += 1
    X = [f/nb_mots for f in X]
    return X;