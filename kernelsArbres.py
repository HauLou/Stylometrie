## Librairies

import nltk, re, pprint
import pickle
from fonctions import *

## Fonctions générales

def isFeuille(arbre):
    return (type(arbre)==str)

def isArbre(arbre):
    return (type(arbre)==nltk.tree.Tree)

## Test : import des fichiers

fichier = open('./articlesNature/1/0.txt', 'rb')
N = pickle.load(fichier)
fichier.close()

fichier = open('./articles_arbres/1/0.txt', 'rb')
A = pickle.load(fichier)
fichier.close()

## Test divers

variable = 5

def fonction():
    global variable
    variable += 1
    return;

def fun(entier):
    
    def fun2(ent2):
        global variable
        print(entier)
    def incr():
        global variable
        variable += 1
    
    incr()
    fun2(7);
fun(5)

## Test : Expressions régulières

texte = "DETJJJJJJNN DETJJJJJJNN DET JJ  NN DETJJDETJJNN DETNN"
p = re.compile('DET(JJ)*NN')
a = p.findall(texte)
print(a)
# p = re.compile('\d+')
# a = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')

## Calcule les 'fonctions' trouvées par NLP Stanford Parser [Réponse : Voir ci-dessous. 1) brut 2) où l'on a retiré celles de natureMots]
# 1) ['NN', 'POS', 'RBS', 'WP$', 'NNPS', 'WHADVP', 'PRN', 'VBG', '-LRB-', 'NNP', 'JJR', 'VB', 'EX', 'PP', 'ROOT', ',', "''", 'WHNP', 'FRAG', '-RRB-', 'LS', 'VBP', 'ADJP', 'WHPP', 'MD', 'DT', ':', 'VP', 'PRP$', 'CD', 'SYM', 'VBZ', 'CC', 'NX', 'LST', 'FW', 'ADVP', 'VBD', 'TO', 'SQ', 'IN', 'SBAR', 'WDT', 'RRC', 'WP', 'INTJ', '.', 'JJ', 'S', 'QP', 'JJS', 'SINV', 'NNS', 'PRP', 'RB', 'WHADJP', 'NAC', '$', 'SBARQ', 'RP', 'X', 'CONJP', 'UH', 'VBN', 'NP', 'PRT', 'RBR', '``', 'PDT', 'UCP', 'WRB']

# 2) ['WHADVP','PRN','-LRB-','PP','ROOT','WHNP','FRAG','-RRB-','ADJP','WHPP','NX','VP','SYM','LST','ADVP','SQ','SBAR','RRC','INTJ','QP','S','SINV','WHADJP','NAC','SBARQ','X','CONJP','UH','NP','PRT','UCP']

def foncStand(arbre):
    retour = []
    if isArbre(arbre):
        retour.append(arbre._label)
        for fils in arbre:
            retour = list(set(retour + foncStand(fils) ))
    return retour;

auteurs = ['1','2','3']
nbArt = calcArt(auteurs) # tableau dans lequel est stocké le nombre d'articles par auteur
resultat = []
for auteur in auteurs:
    for article in range(nbArt[int(auteur)-1]):
        # chargement doc
        chemin = './articles_arbres/'+auteur+'/'+str(article)+'.txt'
        fichier = open(chemin, 'rb')
        texte = pickle.load(fichier)
        fichier.close()
        # Traitement
        for phrase in texte:
            resultat = list(set(resultat + foncStand(phrase) ))
print(resultat)

fonctions_Stand = ['NN', 'POS', 'RBS', 'WP$', 'NNPS', 'WHADVP', 'PRN', 'VBG', '-LRB-', 'NNP', 'JJR', 'VB', 'EX', 'PP', 'ROOT', ',', "''", 'WHNP', 'FRAG', '-RRB-', 'LS', 'VBP', 'ADJP', 'WHPP', 'MD', 'DT', ':', 'VP', 'PRP$', 'CD', 'SYM', 'VBZ', 'CC', 'NX', 'LST', 'FW', 'ADVP', 'VBD', 'TO', 'SQ', 'IN', 'SBAR', 'WDT', 'RRC', 'WP', 'INTJ', '.', 'JJ', 'S', 'QP', 'JJS', 'SINV', 'NNS', 'PRP', 'RB', 'WHADJP', 'NAC', '$', 'SBARQ', 'RP', 'X', 'CONJP', 'UH', 'VBN', 'NP', 'PRT', 'RBR', '``', 'PDT', 'UCP', 'WRB']

## Fonctions kernels pour les Arbres

## Kernel 1 : fréquence des groupes nominaux/verbaux fréquents

# Fonction pour les groupes det (jj)* nn
# La fonction prend en argument en arbre, et retourne un tableau (correspond au nb de jj)


# Déjà fait??
    
## Kernel 2 : Répartition des arbres des sous-sentences


def taille(arbre): # Fonction qui calcule le nombre de feuilles d'un arbre
    retour = 0
    if isFeuille(arbre):
        retour = 1
    else:
        for fils in arbre:
            retour += taille(fils)
    return retour;
    
def classe(arbre):
    n = taille(arbre)
    retour = n//3
    if retour > 14:
        retour = 14
    return retour;
    
def repSentences(arbre): # Fonction qui calcule la répartition des sentences d'un arbre
    retour = [0]*15
    auxsent(arbre, retour)
    return retour;
    
def auxsent(arbre, retour):
    if isArbre(arbre):
        if arbre._label=='S':
            retour[classe(arbre)] += 1
        for fils in arbre:
            retour = auxsent(fils, retour)
    return retour;
    
## Kernel 3 : 

p = 5

def nb_fils(arbre, tableau): # fonction qui calcule la fréquence de nombre de fils d'un arbre
    if isArbre(arbre):
        tableau[len(arbre)] += 1
        for fils in arbre:
            tableau = nb_fils(fils, tableau)
    return tableau;

def profondeur(arbre): # fonction qui calcule la profondeur d'un arbre
    retour = 0
    if isArbre(arbre):
        for fils in arbre:
            retour = max([retour, profondeur(fils)])
        retour += 1
    return retour;

def nb_noeuds(arbre): # fonction qui calcule le nombre de noeuds d'un arbre
    retour = 0
    if isArbre(arbre):
        for fils in arbre:
            retour += nb_noeuds(fils)
        retour += 1
    return retour;
    
def tendance(arbre, tableau): # determine la position du sous-arbre de position maximal à chaque fois
    if isArbre(arbre):
        indice = 0
        for fils in arbre:
            tableau[indice] += nb_noeuds(fils)/nb_noeuds(arbre)
            indice += 1
        for fils in arbre:
            tableau = tendance(fils, tableau)
    return tableau;

## Test Kernel 3

def struct_arbre(arbre):
    retour = nb_fils(arbre, [0]*10)
    retour += [profondeur(arbre)]
    retour += [nb_noeuds(arbre)]
    retour += tendance(arbre, [0]*10)
    return retour;

for arbre in A:
    print(struct_arbre(arbre))

## Impression des arbres

from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

for auteur in auteurs:
    for article in range(10):
        # Chargement des fichiers
        chemin = './articles_arbres/'+auteur+'/'+str(article)+'.txt'
        fichier = open(chemin, 'rb')
        A = pickle.load(fichier)
        fichier.close()
        # Impression des arbres
        #A[0].draw()
        cf = CanvasFrame()
        t = A[0]
        tc = TreeWidget(cf.canvas(),t)
        cf.add_widget(tc,10,10) # (10,10) offsets
        cf.print_to_file('./dessins_arbres/'+auteur+'/'+str(article)+'.ps')
        cf.destroy()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    