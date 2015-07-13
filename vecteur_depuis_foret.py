## Bibliothèques

import nltk
from fonctions import *

## Fréquence des couples d'arêtes :

# Prend un arbre en argument et renvoie la liste des couples d'arêtes :
def liste_aretes(arbre):
    retour = []
    if type(arbre) == nltk.tree.Tree:
        for fils in arbre:
            if type(fils) == nltk.tree.Tree:
                retour.append((arbre._label,fils._label))
                r2 = liste_aretes(fils)
                retour += r2
    return retour

def vecteur_frequence_couples_aretes(foret):
    liste_ar = [('ROOT', 'S'), ('S', 'NP'), ('NP', 'NNP'), ('S', 'VP'), ('VP', 'VBZ'), ('VP', 'PP'), ('PP', 'IN'), ('PP', 'NP'), ('NP', 'NP'), ('NP', 'DT'), ('NP', 'NN'), ('NP', 'PP'), ('S', '.'), ('S', 'SBAR'), ('SBAR', 'WHADVP'), ('WHADVP', 'WRB'), ('SBAR', 'S'), ('NP', 'NNS'), ('VP', 'VBP'), ('VP', 'PRT'), ('PRT', 'RP'), ('VP', 'NP'), ('NP', 'JJ'), ('NP', 'JJR'), ('VP', 'SBAR'), ('SBAR', 'IN'), ('VP', 'MD'), ('VP', 'VP'), ('VP', 'VB'), ('VP', 'ADJP'), ('ADJP', 'ADJP'), ('ADJP', 'JJR'), ('ADJP', 'SBAR'), ('NP', 'PRP'), ('VP', 'VBD'), ('VP', 'ADVP'), ('ADVP', 'NP'), ('ADVP', 'RBR'), ('NP', ','), ('NP', 'ADVP'), ('ADVP', 'IN'), ('ADVP', 'JJS'), ('S','S'), ('NP', 'EX'), ('VP', 'VBN'), ('NP', 'SBAR'), ('VP', 'S'), ('S', 'ADJP'), ('ADJP', 'JJ'), ('S', 'CC'), ('ADJP', 'CC'), ('ADJP', 'RB'), ('PP', 'PP'), ('S', ','), ('PP', 'TO'), ('VP', ','), ('NP', 'CD'), ('VP', 'VBG'), ('ADVP', 'RB'), ('PP', 'CC'), ('PP', 'RB'), ('NP', 'VBG'), ('VP', 'CC'), ('S', 'ADVP'), ('ADJP', 'S'),('VP', 'TO'), ('NP', 'POS'), ('VP', 'RB'), ('VP', '``'), ('VP', "''"), ('PP', 'SBAR'), ('SBAR', 'WHNP'), ('WHNP', 'WP'), ('NP', 'S'), ('NP', 'VP'), ('WHNP', 'WDT'),('PP', 'S'), ('NP', ':'), ('NP', 'RB'), ('NP', 'ADJP'), ('NP', 'IN'), ('ADJP', 'PP'), ('ADJP', 'RBR'), ('NP', 'CC'), ('NP', 'PRP$'), ('NP', 'JJS'), ('NP', 'QP'), ('QP', 'JJR'), ('QP', 'IN'), ('QP', 'CD'), ('PP', 'VBG'), ('QP', 'RB'), ('VP', ':'), ('ADJP', 'VBN'), ('S', '``'), ('S', 'PP'), ('S', "''"), ('ADVP', 'ADVP'), ('ADVP', 'SBAR'), ('ADVP', 'S'), ('S', ':'), ('S', 'PRN'), ('PRN', 'SINV'), ('SINV', 'VP'), ('SINV', 'NP'), ('SINV', ':'), ('SINV', '``'), ('SINV', 'S'), ('SINV', '.'), ('SINV', "''"), ('NP', "''"), ('PP', 'ADVP'), ('ADVP', 'CC'), ('ADVP', 'PP'), ('NP', 'VBN'), ('QP', 'DT'), ('PRN', ','), ('PRN', 'PP'), ('QP', 'TO'), ('SBAR', 'SINV'), ('SINV', 'VBD'), ('SINV', 'RB'), ('NP', 'PRN'), ('PRN', '-LRB-'), ('PRN', 'NP'), ('PRN', '-RRB-'), ('SBAR', 'FRAG'), ('FRAG', 'NP'), ('FRAG', ':'), ('FRAG', '``'), ('FRAG', 'S'), ('NP', 'NNPS'), ('NP', '``'), ('FRAG', '.'), ('FRAG', "''"), ('ROOT', 'SINV'), ('SINV', ','), ('NP', 'FRAG'), ('FRAG', 'ADJP'), ('ADJP', 'WHADVP'), ('ADJP', 'ADVP'), ('ADVP', 'CD'), ('ADVP', 'TO'), ('ADJP', '``'), ('ADJP', "''"), ('VP', 'PRN'), ('PRN', 'ADVP'), ('S', 'SBARQ'), ('SBARQ', 'WHNP'), ('SBARQ', 'SQ'), ('SQ', 'VBZ'), ('SQ', 'ADJP'), ('SBAR', ','), ('ADVP', 'DT'), ('ADVP', 'RBS'), ('PRN', 'CC'), ('ROOT', 'SBARQ'), ('SBARQ', 'RB'), ('SQ', 'VP'), ('SBARQ', '.'), ('ROOT', 'NP'), ('ADJP', 'NN'), ('NP', '.'), ('SBAR', 'SBAR'), ('SBAR', 'CC'), ('NP', 'CONJP'), ('CONJP', 'RB'), ('CONJP', 'IN'), ('SBAR', 'NP'), ('S', 'RB'), ('QP', 'NP'), ('NP', 'SYM'), ('PRN', 'S'), ('NP', 'PDT'), ('VP', 'NN'), ('VP', '.'), ('SBAR', '``'), ('SBAR', "''"), ('ADJP', ':'), ('VP', 'UCP'), ('UCP', 'PP'), ('UCP', ','), ('UCP', 'CC'), ('UCP', 'ADVP'), ('UCP', 'ADJP'), ('QP', 'CC'), ('ADJP', 'RP'), ('SBAR', '.'), ('ADJP', 'IN'), ('PRN', 'SBAR'), ('UCP', 'SBAR'), ('SBAR', 'RB'), ('PP', 'JJ'), ('ADJP', 'RBS'), ('SBAR', 'WHPP'), ('WHPP', 'IN'), ('WHPP', 'WHNP'), ('ADJP', 'CD'), ('SBARQ', 'WHADVP'), ('SQ', 'NP'), ('SBAR', ':'), ('VP', 'DT'), ('S', 'IN'), ('WHNP', 'NN'), ('PP', 'VBN'), ('NP', 'TO'), ('FRAG', 'ADVP'), ('QP', 'JJ'), ('PP', ','), ('NP', 'UCP'), ('UCP', 'NP'), ('PP', 'VBD'), ('UCP', ':'), ('PRN', ':'), ('SBAR', 'ADVP'), ('SINV', 'CC'), ('SINV', 'VBZ'), ('QP', 'NN'), ('ROOT', 'FRAG'), ('FRAG', 'SBAR'), ('NP', 'WHPP'), ('S', 'INTJ'), ('INTJ', 'UH'), ('NP', 'WDT'), ('SBAR', 'PRN'), ('INTJ', 'RB'), ('SINV', 'ADVP'), ('SINV', 'SINV'), ('NP', 'UH'), ('SBAR', 'MD'), ('ADVP', 'NN'), ('FRAG', 'PP'), ('ADJP', 'PRN'), ('UCP', 'JJ'), ('UCP', 'NN'), ('SBAR', 'WHADJP'), ('WHADJP', 'WRB'), ('WHADJP', 'JJ'), ('ADJP', 'VBG'), ('SBAR', 'NN'), ('QP', 'JJS'), ('WHADVP', 'RB'), ('WHNP', 'DT'), ('WHNP', 'WHPP'), ('PP', 'CONJP'), ('PP', 'DT'), ('NP', 'RBS'), ('QP', 'PDT'), ('ADVP', 'JJR'), ('QP', 'NNS'), ('WHNP', 'NP'), ('VP', 'NNP'), ('PP', '``'), ('PP', 'ADJP'), ('PP', "''"), ('PP', 'FW'), ('ADJP', ','), ('WHPP', 'TO'), ('FRAG', 'CC'), ('FRAG', 'RB'), ('NP', '$'), ('ADJP', '$'), ('QP', '$'), ('ADVP', 'JJ'), ('PP', ':'), ('ADJP', 'DT'), ('NP', 'NAC'), ('NAC', 'NNP'), ('NAC', 'PP'), ('NP', 'RBR'), ('NP', 'FW'), ('PRN', 'UCP'), ('UCP', 'VP'), ('NP', 'WP'), ('ROOT', 'SQ'), ('SQ', 'MD'), ('SQ', 'ADVP'), ('SQ', '.'), ('ROOT', 'INTJ'), ('INTJ', '.'), ('FRAG', ','), ('CONJP', 'CC'), ('PP', 'INTJ'), ('INTJ', 'VB'), ('WHNP', 'NNS'), ('SBAR', 'UCP'), ('ADJP', 'NNP'), ('ADJP', 'JJS'), ('NP', 'RRC'), ('RRC', 'ADVP'), ('RRC', 'NP'), ('PRT', 'CC'), ('WHNP', 'RB'), ('UCP', 'IN'), ('SQ', 'NNP'), ('ADJP', 'NP'), ('VP', 'JJ'), ('S', 'UCP'), ('UCP', 'S'), ('UCP', '.'), ('FRAG', 'WRB'), ('SINV', 'PP'), ('VP', 'WHNP'), ('S', 'FRAG'), ('WHADVP', 'JJ'), ('SBARQ', 'SBAR'), ('VP', 'IN'), ('SINV', 'MD'), ('SQ', 'RB'), ('S', 'SQ'), ('ADJP', 'QP'), ('S', '-LRB-'), ('S', '-RRB-'), ('ADJP', 'TO'), ('SBAR', 'PP'), ('QP', 'RBR'), ('PP', 'RBS'), ('SINV', 'SBAR'), ('SQ', 'VBP'), ('SBAR', 'WDT'), ('VP', 'CONJP'), ('FRAG', 'VP'), ('NP', 'VB'), ('SQ', 'CC'), ('VP', 'FRAG'), ('FRAG', 'IN'), ('NP', 'NX'), ('NX', 'NX'), ('NX', 'NN'), ('NX', 'CC'), ('ADVP', 'PRN'), ('FRAG', 'WHNP'), ('WHNP', 'WRB'), ('NP', 'WRB'), ('FRAG', 'WHADVP'), ('NP', '-LRB-'), ('NP', '-RRB-'), ('SQ', ','), ('NAC', 'NP'), ('ADVP', 'NNS'), ('NX', 'JJ'), ('RRC', 'ADJP'), ('RRC', 'SBAR'), ('VP', 'SBARQ'), ('NX', 'PP'), ('PRN', 'FW'), ('PRN', 'ADJP'), ('ADJP', 'CONJP'), ('VP', 'X'), ('X', 'ADVP'), ('ADVP', '.'), ('ADVP', "''"), ('X', 'NP'), ('ADVP', 'LS'), ('PRN', 'VP'), ('ADVP', 'PDT'), ('PP', 'UCP'), ('QP', 'RBS'), ('WHADVP', 'ADJP'), ('VP', 'RBR'), ('WHNP', 'WHNP'), ('WHNP', 'PP'), ('PP', '.'), ('WHNP', 'WP$'), ('PRN', 'FRAG'), ('PP', 'RBR'), ('SBAR', 'X'), ('X', 'DT'), ('X', 'ADJP'), ('S', 'X'), ('X', 'JJR'), ('ADVP', ','), ('SQ', 'FRAG'), ('SBARQ', 'S'), ('NX', 'NNS'), ('ADVP', 'WRB'), ('NP', 'X'), ('X', 'TO'), ('FRAG', 'CONJP'), ('WHADJP', 'RB'), ('NP', 'RP'), ('ADVP', 'ADJP'), ('ROOT', 'SBAR'), ('WHNP', 'WHADJP'), ('PP', 'NN'), ('SBAR', 'WP$'), ('SBAR', 'VBD'), ('ADJP', 'PRT'), ('PP', 'RP'), ('RRC', 'PP'), ('SBARQ', '``'), ('SBARQ', "''"), ('PP', 'VP'), ('ROOT', 'PP'), ('NX', 'NP'), ('UCP', 'DT'), ('ROOT', 'X'), ('X', 'SBAR'), ('NX', ','), ('NX', 'PRP$'), ('WHNP', 'JJS'), ('SQ', 'VBD'), ('SQ', 'S'), ('ADVP', 'PRP'), ('SINV', 'ADJP'), ('WHNP', 'CD'), ('FRAG', 'JJ'), ('WHNP', 'PRN'), ('PRN', "''"), ('PRN', '``'), ('UCP', 'CONJP'), ('VP', 'LST'), ('LST', 'LS'), ('LST', '-RRB-'), ('NP', 'LST'), ('CONJP', 'JJ'), ('VP', 'RBS'), ('NP', 'PRT'), ('FRAG', 'FRAG'), ('PRN', 'INTJ'), ('SBARQ', ','), ('NP', 'VBD'), ('WHNP', 'JJ'), ('FRAG', 'INTJ'), ('S', 'CONJP'), ('ADVP', 'VB'), ('NP', 'SBARQ'), ('SBARQ', 'SINV'), ('PP', 'PRN'), ('PRN', 'JJ'), ('INTJ', 'DT'), ('INTJ', 'VBZ'), ('PRN', 'CONJP'), ('PRN', 'RB'), ('ADJP', 'VBD'), ('NAC', 'NN'), ('PP', 'FRAG'), ('SQ', 'PP'), ('ROOT', 'UCP'), ('ADVP', 'RP'), ('S', 'DT'), ('PP', 'WHNP'), ('SBARQ', 'CC'), ('ADVP', ':'), ('VP', 'SQ'), ('SBAR', 'CONJP'), ('ADJP', 'VB'), ('PRN', 'NX'), ('WHADVP', 'NP'), ('NX', 'VBG'), ('NX', 'PRN'), ('CONJP', 'NN'), ('CONJP', 'TO'), ('SBARQ', 'WHADJP'), ('WHADJP', 'ADJP'), ('UCP', 'RB'), ('VP', 'INTJ'), ('FRAG', 'DT'), ('PP', 'SBARQ'), ('S', 'MD'), ('S', 'SINV'), ('UCP', 'FRAG'), ('NX', 'S'), ('NX', 'NNP'), ('FRAG', 'X'), ('X', 'SYM'), ('WHADVP', 'CC'), ('UCP', 'WHADVP'), ('NP', 'WP$'), ('CONJP', 'VB'), ('NP', 'INTJ'), ('PRN', 'SQ'), ('ADJP', '.'), ('RRC', 'VP'), ('SBAR', 'QP'), ('FRAG', 'WHADJP'), ('NP', 'SQ'), ('ADVP', 'VBD'), ('X', ':'), ('X', 'PP'), ('SQ', 'SQ'), ('PRN', 'IN'), ('X', ','), ('X', '.'), ('SBARQ', 'NP'), ('S', 'LST'), ('QP', 'VB'), ('SINV', 'VBP'), ('UCP', 'TO'), ('PRN', 'NNP'), ('SBARQ', 'PP'), ('NX', ':'), ('NX', 'SBAR'), ('PP', 'X'), ('INTJ', 'WRB'), ('ADJP', 'VBP'), ('NX', 'CD'), ('NX', 'RB'), ('UCP', 'SINV'), ('PRN', 'DT'), ('FRAG', 'UCP'), ('UCP', 'NNS'), ('ADVP', '``'), ('ROOT', 'ADVP'), ('WHNP', 'ADJP'), ('SBAR', 'SBARQ'), ('X', 'SBARQ'), ('SBARQ', 'ADVP'), ('X', 'RBR'), ('S', 'VBP'), ('X', 'VBD'), ('VP', 'SINV'), ('SBARQ', 'PRN'), ('WHADJP', 'WP'), ('WHNP', 'ADVP'), ('VP', '-LRB-'), ('SINV', 'FRAG'), ('PRN', 'RRC'), ('SBAR', 'WP'), ('PRT', 'RB'), ('ROOT', 'PRN'), ('ADJP', 'FW'), ('SINV', 'CONJP'), ('S', 'TO'), ('ADJP', 'NNS'), ('NAC', 'ADVP'), ('UCP', 'PRN'), ('WHNP', 'WHADVP'), ('ADJP', 'WHPP'), ('X', 'VP'), ('SBAR', 'TO'), ('PRN', 'X'), ('WHNP', ','), ('SQ', ':'), ('PRN', 'NAC'), ('ADVP', 'VBG'), ('SINV', 'VB'), ('X', 'RB'), ('X', 'X'), ('WHADVP', 'ADVP'), ('PP', 'JJR'), ('NP', 'MD'), ('NP', 'VBZ'), ('INTJ', '``'), ('NX', 'ADJP'), ('NX', 'IN'), ('NP', 'VBP'), ('RRC', 'RRC'), ('RRC', 'CC'), ('NX', 'NNPS'), ('NX', '``'), ('NX', "''"), ('WHADVP', 'WDT'), ('WHADVP', 'NN'), ('SINV', 'PRN'), ('PRT', 'RBS'), ('X', 'WP'), ('VP', 'QP'), ('ADJP', 'PRP$'), ('WHNP', 'QP'), ('WHADVP', 'PP'), ('NX', 'FW'), ('VP', '-RRB-'), ('INTJ', 'JJ'), ('INTJ', 'NN'), ('LST', 'JJ'), ('NP', 'WHNP'), ('SQ', 'SBAR'), ('WHADVP', '.'), ('PP', 'NX'), ('UCP', 'X'), ('ADVP', 'FW'), ('INTJ', "''"), ('VP', 'WHPP'), ('WHNP', 'JJR'), ('PRN', 'MD'), ('QP', "''"), ('SBAR', 'VB'), ('PRN', 'WHNP'), ('WHNP', 'RBS'), ('NX', 'POS'), ('SINV', 'SBARQ'), ('INTJ', 'INTJ'), ('INTJ', ','), ('SQ', 'NNS'), ('SBARQ', 'WHPP'), ('QP', 'VBN'), ('FRAG', 'SBARQ'), ('INTJ', 'CC'), ('UCP', '``'), ('UCP', "''"), ('WHNP', 'NX'), ('NAC', 'DT'), ('NAC', 'JJ'), ('QP', '``'), ('X', 'CC'), ('UCP', 'RRC'), ('SBAR', 'ADJP'), ('ADJP', 'FRAG'), ('ADVP', 'VP'), ('SQ', '``'), ('WHNP', 'PRP'), ('ADVP', 'UH'), ('S', 'VBD'), ('SINV', 'SQ'), ('PRT', 'JJ'), ('FRAG', 'WHPP'), ('ROOT', 'VP'), ('QP', 'ADVP'), ('INTJ', 'PP'), ('WHNP', 'NNP'), ('WHNP', 'S'), ('ADVP', 'QP'), ('PP', 'NNP'), ('FRAG', 'SINV'), ('X', 'S'), ('SBARQ', 'FRAG'), ('WHNP', 'CC'), ('WHADJP', 'PP'), ('PRN', 'PRN'), ('SBARQ', 'SBARQ'), ('NAC', ','), ('PRN', 'VB'), ('PRN', '.'), ('X', 'IN'), ('NP', '#'), ('QP', '#'),('ADJP', '#'),('X', 'NNP'),('INTJ', 'PRP$'), ('INTJ', 'NNP'),('PP', 'PRP$'), ('PP', 'NNS'),('ROOT', 'ADJP'), ('ADVP', 'NNP'),('RRC', ',')]
    p = len(liste_ar)
    v = [0]*p
    for arbre in foret:
        l = liste_aretes(arbre)
        for c in l:
            if c in liste_ar:
                v[liste_ar.index(c)] += 1
    s = sum(v)
    v = [nb/s for nb in v]
    return v;

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
        if len(arbre) < len(tableau):
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
                if indice < len(tableau):
                    tableau[indice] += nb_noeuds(fils)/nb_noeuds(arbre)
                    indice += 1
        for fils in arbre:
            tableau = tendance(fils, tableau)
    return tableau; 

## Test Kernel 3

def vecteur_struct_arbre(foret):
    arbre = nltk.tree.Tree('ROOT', foret)
    taille_foret = len(foret)
    retour = [a/taille_foret for a in nb_fils(arbre, [0]*15)]
    retour += [profondeur(arbre)-1]
    retour += [nb_noeuds(arbre)/taille_foret]
    retour += tendance(arbre, [0]*15)
    return retour; 

## Fréquence des position des fils

# def vecteur_frequence_noeuds(foret, nb_fils_prem_etage = 8):
#     listeNatures = ['ROOT', 'S', 'NP', 'NNP', 'VP', 'VBZ', 'PP', 'IN', 'DT', 'NN', '.', 'SBAR', 'WHADVP', 'WRB','NNS','VBP', 'PRT', 'RP', 'JJ', 'JJR', 'MD', 'VB', 'ADJP', 'PRP' 'VBD','ADVP', 'RBR', ',', 'JJS', 'EX', 'VBN', 'CC', 'RB', 'TO', 'CD', 'VBG', 'POS', '``', "''", 'WHNP', 'WP', 'WDT', ':','PRP$', 'QP', 'PRN', 'SINV', '-LRB-', '-RRB-', 'FRAG', 'NNPS', 'SBARQ', 'SQ', 'RBS', 'CONJP', 'SYM', 'PDT', 'UCP', 'WHPP', 'INTJ', 'UH', 'WHADJP', 'FW', '$', 'NAC', 'RRC', 'NX', 'X', 'LS', 'WP$', 'LST', '#','VBD']
#     nb_natures = len(listeNatures)
#     nb_arbres = len(foret)
#     v = [0]*(nb_fils_prem_etage*nb_natures)
#     for arbre in foret:
#         if not arbre._label == 'ROOT':
#             exit('etiq != Root dans vecteur_frequence_noeuds')
#         else:
#             fils = arbre[:]
#             t = len(fils)
#             # print('1er étage : '+str(t)+' fils')
#             for i in range(len(fils)):
#                 enfants = fils[i][:]
#                 t = len(enfants)
#                 # print('2eme étage, '+str(i)+'eme fils ('+fils[i]._label+') : '+str(t)+' enfants :')
#                 for j in range(len(enfants)):
#                     # print(enfants[j]._label)
#                     if j < nb_fils_prem_etage:
#                         v[j*nb_natures + listeNatures.index(enfants[j]._label)] += 1
#     v = [c/nb_arbres for c in v]
#     return v
listeNatures = ['ROOT', 'S', 'NP', 'NNP', 'VP', 'VBZ', 'PP', 'IN', 'DT', 'NN', '.', 'SBAR', 'WHADVP', 'WRB','NNS','VBP', 'PRT', 'RP', 'JJ', 'JJR', 'MD', 'VB', 'ADJP', 'PRP', 'VBD','ADVP', 'RBR', ',', 'JJS', 'EX', 'VBN', 'CC', 'RB', 'TO', 'CD', 'VBG', 'POS', '``', "''", 'WHNP', 'WP', 'WDT', ':','PRP$', 'QP', 'PRN', 'SINV', '-LRB-', '-RRB-', 'FRAG', 'NNPS', 'SBARQ', 'SQ', 'RBS', 'CONJP', 'SYM', 'PDT', 'UCP', 'WHPP', 'INTJ', 'UH', 'WHADJP', 'FW', '$', 'NAC', 'RRC', 'NX', 'X', 'LS', 'WP$', 'LST', '#','VBD']

def est_arbre(arbre):
    return type(arbre) == nltk.tree.Tree

def traite_freq(arbre, tableau): # Fonction qui calcule la fréquence d'apparition d'une nature de mot dans un arbre
    if est_arbre(arbre):
        indice = listeNatures.index(arbre._label)
        tableau[indice] +=1
        for fils in arbre:
            tableau = traite_freq(fils, tableau)
    return tableau;

def vecteur_frequence_noeuds(foret, retour = []):

    nb_natures = len(listeNatures)
    retour = [0]*nb_natures
    for arbre in foret:
        retour = traite_freq(arbre,retour)
    s = sum(retour)
    retour = [e/s for e in retour]
    return retour

def liste_etiq():
    liste_ar = [('ROOT', 'S'), ('S', 'NP'), ('NP', 'NNP'), ('S', 'VP'), ('VP', 'VBZ'), ('VP', 'PP'), ('PP', 'IN'), ('PP', 'NP'), ('NP', 'NP'), ('NP', 'DT'), ('NP', 'NN'), ('NP', 'PP'), ('S', '.'), ('S', 'SBAR'), ('SBAR', 'WHADVP'), ('WHADVP', 'WRB'), ('SBAR', 'S'), ('NP', 'NNS'), ('VP', 'VBP'), ('VP', 'PRT'), ('PRT', 'RP'), ('VP', 'NP'), ('NP', 'JJ'), ('NP', 'JJR'), ('VP', 'SBAR'), ('SBAR', 'IN'), ('VP', 'MD'), ('VP', 'VP'), ('VP', 'VB'), ('VP', 'ADJP'), ('ADJP', 'ADJP'), ('ADJP', 'JJR'), ('ADJP', 'SBAR'), ('NP', 'PRP'), ('VP', 'VBD'), ('VP', 'ADVP'), ('ADVP', 'NP'), ('ADVP', 'RBR'), ('NP', ','), ('NP', 'ADVP'), ('ADVP', 'IN'), ('ADVP', 'JJS'), ('S','S'), ('NP', 'EX'), ('VP', 'VBN'), ('NP', 'SBAR'), ('VP', 'S'), ('S', 'ADJP'), ('ADJP', 'JJ'), ('S', 'CC'), ('ADJP', 'CC'), ('ADJP', 'RB'), ('PP', 'PP'), ('S', ','), ('PP', 'TO'), ('VP', ','), ('NP', 'CD'), ('VP', 'VBG'), ('ADVP', 'RB'), ('PP', 'CC'), ('PP', 'RB'), ('NP', 'VBG'), ('VP', 'CC'), ('S', 'ADVP'), ('ADJP', 'S'),('VP', 'TO'), ('NP', 'POS'), ('VP', 'RB'), ('VP', '``'), ('VP', "''"), ('PP', 'SBAR'), ('SBAR', 'WHNP'), ('WHNP', 'WP'), ('NP', 'S'), ('NP', 'VP'), ('WHNP', 'WDT'),('PP', 'S'), ('NP', ':'), ('NP', 'RB'), ('NP', 'ADJP'), ('NP', 'IN'), ('ADJP', 'PP'), ('ADJP', 'RBR'), ('NP', 'CC'), ('NP', 'PRP$'), ('NP', 'JJS'), ('NP', 'QP'), ('QP', 'JJR'), ('QP', 'IN'), ('QP', 'CD'), ('PP', 'VBG'), ('QP', 'RB'), ('VP', ':'), ('ADJP', 'VBN'), ('S', '``'), ('S', 'PP'), ('S', "''"), ('ADVP', 'ADVP'), ('ADVP', 'SBAR'), ('ADVP', 'S'), ('S', ':'), ('S', 'PRN'), ('PRN', 'SINV'), ('SINV', 'VP'), ('SINV', 'NP'), ('SINV', ':'), ('SINV', '``'), ('SINV', 'S'), ('SINV', '.'), ('SINV', "''"), ('NP', "''"), ('PP', 'ADVP'), ('ADVP', 'CC'), ('ADVP', 'PP'), ('NP', 'VBN'), ('QP', 'DT'), ('PRN', ','), ('PRN', 'PP'), ('QP', 'TO'), ('SBAR', 'SINV'), ('SINV', 'VBD'), ('SINV', 'RB'), ('NP', 'PRN'), ('PRN', '-LRB-'), ('PRN', 'NP'), ('PRN', '-RRB-'), ('SBAR', 'FRAG'), ('FRAG', 'NP'), ('FRAG', ':'), ('FRAG', '``'), ('FRAG', 'S'), ('NP', 'NNPS'), ('NP', '``'), ('FRAG', '.'), ('FRAG', "''"), ('ROOT', 'SINV'), ('SINV', ','), ('NP', 'FRAG'), ('FRAG', 'ADJP'), ('ADJP', 'WHADVP'), ('ADJP', 'ADVP'), ('ADVP', 'CD'), ('ADVP', 'TO'), ('ADJP', '``'), ('ADJP', "''"), ('VP', 'PRN'), ('PRN', 'ADVP'), ('S', 'SBARQ'), ('SBARQ', 'WHNP'), ('SBARQ', 'SQ'), ('SQ', 'VBZ'), ('SQ', 'ADJP'), ('SBAR', ','), ('ADVP', 'DT'), ('ADVP', 'RBS'), ('PRN', 'CC'), ('ROOT', 'SBARQ'), ('SBARQ', 'RB'), ('SQ', 'VP'), ('SBARQ', '.'), ('ROOT', 'NP'), ('ADJP', 'NN'), ('NP', '.'), ('SBAR', 'SBAR'), ('SBAR', 'CC'), ('NP', 'CONJP'), ('CONJP', 'RB'), ('CONJP', 'IN'), ('SBAR', 'NP'), ('S', 'RB'), ('QP', 'NP'), ('NP', 'SYM'), ('PRN', 'S'), ('NP', 'PDT'), ('VP', 'NN'), ('VP', '.'), ('SBAR', '``'), ('SBAR', "''"), ('ADJP', ':'), ('VP', 'UCP'), ('UCP', 'PP'), ('UCP', ','), ('UCP', 'CC'), ('UCP', 'ADVP'), ('UCP', 'ADJP'), ('QP', 'CC'), ('ADJP', 'RP'), ('SBAR', '.'), ('ADJP', 'IN'), ('PRN', 'SBAR'), ('UCP', 'SBAR'), ('SBAR', 'RB'), ('PP', 'JJ'), ('ADJP', 'RBS'), ('SBAR', 'WHPP'), ('WHPP', 'IN'), ('WHPP', 'WHNP'), ('ADJP', 'CD'), ('SBARQ', 'WHADVP'), ('SQ', 'NP'), ('SBAR', ':'), ('VP', 'DT'), ('S', 'IN'), ('WHNP', 'NN'), ('PP', 'VBN'), ('NP', 'TO'), ('FRAG', 'ADVP'), ('QP', 'JJ'), ('PP', ','), ('NP', 'UCP'), ('UCP', 'NP'), ('PP', 'VBD'), ('UCP', ':'), ('PRN', ':'), ('SBAR', 'ADVP'), ('SINV', 'CC'), ('SINV', 'VBZ'), ('QP', 'NN'), ('ROOT', 'FRAG'), ('FRAG', 'SBAR'), ('NP', 'WHPP'), ('S', 'INTJ'), ('INTJ', 'UH'), ('NP', 'WDT'), ('SBAR', 'PRN'), ('INTJ', 'RB'), ('SINV', 'ADVP'), ('SINV', 'SINV'), ('NP', 'UH'), ('SBAR', 'MD'), ('ADVP', 'NN'), ('FRAG', 'PP'), ('ADJP', 'PRN'), ('UCP', 'JJ'), ('UCP', 'NN'), ('SBAR', 'WHADJP'), ('WHADJP', 'WRB'), ('WHADJP', 'JJ'), ('ADJP', 'VBG'), ('SBAR', 'NN'), ('QP', 'JJS'), ('WHADVP', 'RB'), ('WHNP', 'DT'), ('WHNP', 'WHPP'), ('PP', 'CONJP'), ('PP', 'DT'), ('NP', 'RBS'), ('QP', 'PDT'), ('ADVP', 'JJR'), ('QP', 'NNS'), ('WHNP', 'NP'), ('VP', 'NNP'), ('PP', '``'), ('PP', 'ADJP'), ('PP', "''"), ('PP', 'FW'), ('ADJP', ','), ('WHPP', 'TO'), ('FRAG', 'CC'), ('FRAG', 'RB'), ('NP', '$'), ('ADJP', '$'), ('QP', '$'), ('ADVP', 'JJ'), ('PP', ':'), ('ADJP', 'DT'), ('NP', 'NAC'), ('NAC', 'NNP'), ('NAC', 'PP'), ('NP', 'RBR'), ('NP', 'FW'), ('PRN', 'UCP'), ('UCP', 'VP'), ('NP', 'WP'), ('ROOT', 'SQ'), ('SQ', 'MD'), ('SQ', 'ADVP'), ('SQ', '.'), ('ROOT', 'INTJ'), ('INTJ', '.'), ('FRAG', ','), ('CONJP', 'CC'), ('PP', 'INTJ'), ('INTJ', 'VB'), ('WHNP', 'NNS'), ('SBAR', 'UCP'), ('ADJP', 'NNP'), ('ADJP', 'JJS'), ('NP', 'RRC'), ('RRC', 'ADVP'), ('RRC', 'NP'), ('PRT', 'CC'), ('WHNP', 'RB'), ('UCP', 'IN'), ('SQ', 'NNP'), ('ADJP', 'NP'), ('VP', 'JJ'), ('S', 'UCP'), ('UCP', 'S'), ('UCP', '.'), ('FRAG', 'WRB'), ('SINV', 'PP'), ('VP', 'WHNP'), ('S', 'FRAG'), ('WHADVP', 'JJ'), ('SBARQ', 'SBAR'), ('VP', 'IN'), ('SINV', 'MD'), ('SQ', 'RB'), ('S', 'SQ'), ('ADJP', 'QP'), ('S', '-LRB-'), ('S', '-RRB-'), ('ADJP', 'TO'), ('SBAR', 'PP'), ('QP', 'RBR'), ('PP', 'RBS'), ('SINV', 'SBAR'), ('SQ', 'VBP'), ('SBAR', 'WDT'), ('VP', 'CONJP'), ('FRAG', 'VP'), ('NP', 'VB'), ('SQ', 'CC'), ('VP', 'FRAG'), ('FRAG', 'IN'), ('NP', 'NX'), ('NX', 'NX'), ('NX', 'NN'), ('NX', 'CC'), ('ADVP', 'PRN'), ('FRAG', 'WHNP'), ('WHNP', 'WRB'), ('NP', 'WRB'), ('FRAG', 'WHADVP'), ('NP', '-LRB-'), ('NP', '-RRB-'), ('SQ', ','), ('NAC', 'NP'), ('ADVP', 'NNS'), ('NX', 'JJ'), ('RRC', 'ADJP'), ('RRC', 'SBAR'), ('VP', 'SBARQ'), ('NX', 'PP'), ('PRN', 'FW'), ('PRN', 'ADJP'), ('ADJP', 'CONJP'), ('VP', 'X'), ('X', 'ADVP'), ('ADVP', '.'), ('ADVP', "''"), ('X', 'NP'), ('ADVP', 'LS'), ('PRN', 'VP'), ('ADVP', 'PDT'), ('PP', 'UCP'), ('QP', 'RBS'), ('WHADVP', 'ADJP'), ('VP', 'RBR'), ('WHNP', 'WHNP'), ('WHNP', 'PP'), ('PP', '.'), ('WHNP', 'WP$'), ('PRN', 'FRAG'), ('PP', 'RBR'), ('SBAR', 'X'), ('X', 'DT'), ('X', 'ADJP'), ('S', 'X'), ('X', 'JJR'), ('ADVP', ','), ('SQ', 'FRAG'), ('SBARQ', 'S'), ('NX', 'NNS'), ('ADVP', 'WRB'), ('NP', 'X'), ('X', 'TO'), ('FRAG', 'CONJP'), ('WHADJP', 'RB'), ('NP', 'RP'), ('ADVP', 'ADJP'), ('ROOT', 'SBAR'), ('WHNP', 'WHADJP'), ('PP', 'NN'), ('SBAR', 'WP$'), ('SBAR', 'VBD'), ('ADJP', 'PRT'), ('PP', 'RP'), ('RRC', 'PP'), ('SBARQ', '``'), ('SBARQ', "''"), ('PP', 'VP'), ('ROOT', 'PP'), ('NX', 'NP'), ('UCP', 'DT'), ('ROOT', 'X'), ('X', 'SBAR'), ('NX', ','), ('NX', 'PRP$'), ('WHNP', 'JJS'), ('SQ', 'VBD'), ('SQ', 'S'), ('ADVP', 'PRP'), ('SINV', 'ADJP'), ('WHNP', 'CD'), ('FRAG', 'JJ'), ('WHNP', 'PRN'), ('PRN', "''"), ('PRN', '``'), ('UCP', 'CONJP'), ('VP', 'LST'), ('LST', 'LS'), ('LST', '-RRB-'), ('NP', 'LST'), ('CONJP', 'JJ'), ('VP', 'RBS'), ('NP', 'PRT'), ('FRAG', 'FRAG'), ('PRN', 'INTJ'), ('SBARQ', ','), ('NP', 'VBD'), ('WHNP', 'JJ'), ('FRAG', 'INTJ'), ('S', 'CONJP'), ('ADVP', 'VB'), ('NP', 'SBARQ'), ('SBARQ', 'SINV'), ('PP', 'PRN'), ('PRN', 'JJ'), ('INTJ', 'DT'), ('INTJ', 'VBZ'), ('PRN', 'CONJP'), ('PRN', 'RB'), ('ADJP', 'VBD'), ('NAC', 'NN'), ('PP', 'FRAG'), ('SQ', 'PP'), ('ROOT', 'UCP'), ('ADVP', 'RP'), ('S', 'DT'), ('PP', 'WHNP'), ('SBARQ', 'CC'), ('ADVP', ':'), ('VP', 'SQ'), ('SBAR', 'CONJP'), ('ADJP', 'VB'), ('PRN', 'NX'), ('WHADVP', 'NP'), ('NX', 'VBG'), ('NX', 'PRN'), ('CONJP', 'NN'), ('CONJP', 'TO'), ('SBARQ', 'WHADJP'), ('WHADJP', 'ADJP'), ('UCP', 'RB'), ('VP', 'INTJ'), ('FRAG', 'DT'), ('PP', 'SBARQ'), ('S', 'MD'), ('S', 'SINV'), ('UCP', 'FRAG'), ('NX', 'S'), ('NX', 'NNP'), ('FRAG', 'X'), ('X', 'SYM'), ('WHADVP', 'CC'), ('UCP', 'WHADVP'), ('NP', 'WP$'), ('CONJP', 'VB'), ('NP', 'INTJ'), ('PRN', 'SQ'), ('ADJP', '.'), ('RRC', 'VP'), ('SBAR', 'QP'), ('FRAG', 'WHADJP'), ('NP', 'SQ'), ('ADVP', 'VBD'), ('X', ':'), ('X', 'PP'), ('SQ', 'SQ'), ('PRN', 'IN'), ('X', ','), ('X', '.'), ('SBARQ', 'NP'), ('S', 'LST'), ('QP', 'VB'), ('SINV', 'VBP'), ('UCP', 'TO'), ('PRN', 'NNP'), ('SBARQ', 'PP'), ('NX', ':'), ('NX', 'SBAR'), ('PP', 'X'), ('INTJ', 'WRB'), ('ADJP', 'VBP'), ('NX', 'CD'), ('NX', 'RB'), ('UCP', 'SINV'), ('PRN', 'DT'), ('FRAG', 'UCP'), ('UCP', 'NNS'), ('ADVP', '``'), ('ROOT', 'ADVP'), ('WHNP', 'ADJP'), ('SBAR', 'SBARQ'), ('X', 'SBARQ'), ('SBARQ', 'ADVP'), ('X', 'RBR'), ('S', 'VBP'), ('X', 'VBD'), ('VP', 'SINV'), ('SBARQ', 'PRN'), ('WHADJP', 'WP'), ('WHNP', 'ADVP'), ('VP', '-LRB-'), ('SINV', 'FRAG'), ('PRN', 'RRC'), ('SBAR', 'WP'), ('PRT', 'RB'), ('ROOT', 'PRN'), ('ADJP', 'FW'), ('SINV', 'CONJP'), ('S', 'TO'), ('ADJP', 'NNS'), ('NAC', 'ADVP'), ('UCP', 'PRN'), ('WHNP', 'WHADVP'), ('ADJP', 'WHPP'), ('X', 'VP'), ('SBAR', 'TO'), ('PRN', 'X'), ('WHNP', ','), ('SQ', ':'), ('PRN', 'NAC'), ('ADVP', 'VBG'), ('SINV', 'VB'), ('X', 'RB'), ('X', 'X'), ('WHADVP', 'ADVP'), ('PP', 'JJR'), ('NP', 'MD'), ('NP', 'VBZ'), ('INTJ', '``'), ('NX', 'ADJP'), ('NX', 'IN'), ('NP', 'VBP'), ('RRC', 'RRC'), ('RRC', 'CC'), ('NX', 'NNPS'), ('NX', '``'), ('NX', "''"), ('WHADVP', 'WDT'), ('WHADVP', 'NN'), ('SINV', 'PRN'), ('PRT', 'RBS'), ('X', 'WP'), ('VP', 'QP'), ('ADJP', 'PRP$'), ('WHNP', 'QP'), ('WHADVP', 'PP'), ('NX', 'FW'), ('VP', '-RRB-'), ('INTJ', 'JJ'), ('INTJ', 'NN'), ('LST', 'JJ'), ('NP', 'WHNP'), ('SQ', 'SBAR'), ('WHADVP', '.'), ('PP', 'NX'), ('UCP', 'X'), ('ADVP', 'FW'), ('INTJ', "''"), ('VP', 'WHPP'), ('WHNP', 'JJR'), ('PRN', 'MD'), ('QP', "''"), ('SBAR', 'VB'), ('PRN', 'WHNP'), ('WHNP', 'RBS'), ('NX', 'POS'), ('SINV', 'SBARQ'), ('INTJ', 'INTJ'), ('INTJ', ','), ('SQ', 'NNS'), ('SBARQ', 'WHPP'), ('QP', 'VBN'), ('FRAG', 'SBARQ'), ('INTJ', 'CC'), ('UCP', '``'), ('UCP', "''"), ('WHNP', 'NX'), ('NAC', 'DT'), ('NAC', 'JJ'), ('QP', '``'), ('X', 'CC'), ('UCP', 'RRC'), ('SBAR', 'ADJP'), ('ADJP', 'FRAG'), ('ADVP', 'VP'), ('SQ', '``'), ('WHNP', 'PRP'), ('ADVP', 'UH'), ('S', 'VBD'), ('SINV', 'SQ'), ('PRT', 'JJ'), ('FRAG', 'WHPP'), ('ROOT', 'VP'), ('QP', 'ADVP'), ('INTJ', 'PP'), ('WHNP', 'NNP'), ('WHNP', 'S'), ('ADVP', 'QP'), ('PP', 'NNP'), ('FRAG', 'SINV'), ('X', 'S'), ('SBARQ', 'FRAG'), ('WHNP', 'CC'), ('WHADJP', 'PP'), ('PRN', 'PRN'), ('SBARQ', 'SBARQ'), ('NAC', ','), ('PRN', 'VB'), ('PRN', '.'), ('X', 'IN'), ('NP', '#'), ('QP', '#'),('ADJP', '#'),('X', 'NNP'),('INTJ', 'PRP$'), ('INTJ', 'NNP'),('PP', 'PRP$'), ('PP', 'NNS'),('ROOT', 'ADJP'), ('ADVP', 'NNP'),('RRC', ',')]
    ret = []
    for e1,e2 in liste_ar:
        if not e1 in ret:
            ret.append(e1)
        if not e2 in ret:
            ret.append(e2)
    return ret
