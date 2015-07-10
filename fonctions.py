from nltk.corpus import PlaintextCorpusReader # Pour la définition du corpus de textes
import numpy as np
import pickle

## Fonctions annexes

def calcArt(tableau):
    longueurs = []
    for key in tableau:
        corpus_root = "./articles/" + key
        articles = PlaintextCorpusReader(corpus_root, '.*').fileids()
        size = len(articles)
        longueurs.append(size)
    return longueurs;

def sum(table):
    a = 0
    for key in table:
        a += key
    return a;
    
def findCol(clef, tableau, couleurs):
    acc = 0
    indice = 0
    while ((indice < len(tableau))&(clef > acc)):
        acc += tableau[indice]
        indice += 1
    return (couleurs[indice]);
    
def secondParam(tab):
    retour = [t[1] for t in tab]
    return retour;
    
def charge_texte(auteur,i):
    f = open('./auteurs/'+auteur+'/'+str(i)+'.txt','r')
    retour = f.read()
    f.close()
    return retour

def charge_foret(auteur,i):
    f = open('./forets/'+auteur+'/'+str(i)+'.txt','rb')
    retour = pickle.load(f)
    f.close()
    return retour


def charge_liste_natures(auteur,i):
    f = open('./listes_natures/'+auteur+'/'+str(i)+'.txt','rb')
    retour = pickle.load(f)
    f.close()
    return retour
# listeMots = [',', '.', 'the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'I', 'his', 'they', 'be', 'at', 'one', 'have', 'this'] # Liste de mots à changer eventuellement
# auteurs = ['1','2','3']
# nbArt = calcArt(auteurs) # tableau du nombre d'articles par auteur
# p = len(listeMots) # nb de paramètres sur lesquels on lance l'ACP
# n = sum(nbArt) # nb d'articles au total
# X = np.zeros((n,p), dtype = float) # Matrice de données
# couleurs = ['w' ,'b', 'g', 'r', 'c', 'm', 'y', 'k']
#  
# print(findCol(1, nbArt, couleurs))
# print(findCol(900, nbArt, couleurs))
# print(findCol(3025, nbArt, couleurs))