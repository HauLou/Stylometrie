## Librairies
import nltk
import numpy as np
import pickle #import de données sous forme de tableau
import copy

## Pour les arbres tels qu'ils nous sont donnés :

# Ajoute au bon endroit (pour que la liste soit triée) l'élément :
def ajoute(l_arbres,arbre):
    t = len(l_arbres)
    i = 0
    ajout = False
    while not(ajout) and i < t:
        if l_arbres[i]._label > arbre._label:
            ajout = True
            l_arbres.insert(i,arbre)
        i += 1
    if not ajout: l_arbres.append(arbre);

# On lui envoie un arbre et retourne une liste contenant les sous arbres triés selon leur étiquette:
def liste_sous_arbres2(l,a):
    if type(a) == nltk.tree.Tree:
        ajoute(l,a)
        for fils in a:
            liste_sous_arbres2(l,fils)

def liste_sous_arbres(arbre):
    a = copy.deepcopy(arbre)
    l = []
    liste_sous_arbres2(l,a)
    return l;

# Retourne la liste des paires de noeuds (enfin de sous-arbres) de arbre1*arbre2 ayant la même étiquette
def paires_noeuds(arbre1,arbre2):
    sort = False
    retour = []
    l1 = liste_sous_arbres(arbre1)
    l2 = liste_sous_arbres(arbre2)
    n1 = l1.pop()
    n2 = l2.pop()
    while not sort:
        if n1._label < n2._label: 
            if l2 != []: n2 = l2.pop()
            else: sort = True
        elif n1._label > n2._label: 
            if l1 != []: n1 = l1.pop()
            else: sort = True
        else:
            long = len(l2)
            i = 1
            retour.append((n1,n2))
            while i <= long and n1._label == l2[-i]._label:
                retour.append((n1,l2[-i]))
                i += 1
            if l1 != []: n1 = l1.pop()
            else: sort = True
                    
    return retour;

def delta(arbre1,arbre2):
    if arbre1._label != arbre2._label:
        return 0
    elif len(arbre1) == len(arbre2) == 1:
        return 1
    else:
       r = 1
       l = min([len(arbre1),len(arbre2)])
       for i in range(l):
           if type(arbre1[i]) == type(arbre2[i]) == nltk.tree.Tree:
               r *= (1 + delta(arbre1[i],arbre2[i]))
       return r;
        
# Calcule le nombre de sous-ensemble (?! sous-arbres élagués ou sous-graphes faiblement connexes) d'arbres communs
def noyau_sous_arbres(arbre1,arbre2):
    paires = paires_noeuds(arbre1,arbre2)
    retour = 0
    for paire in paires:
        retour += delta(paire[0],paire[1])
    return retour;

# Prend 2 listes et fait la somme surles couples
def noyau_sous_arbres_forêt(l_arbres1,l_arbres2):
    retour = 0
    for a1 in l_arbres1:
        for a2 in l_arbres2:
            retour += noyau_sous_arbres(a1,a2)
    return retour;

# Renvoie 1 si les 2 arbres sont égaux, 0 sinon :
def sont_égaux(arbre1,arbre2):
    
    if type(arbre1) == type(arbre2) == nltk.tree.Tree:
        t1 = len(arbre1)
        t2 = len(arbre2)
        sort = False
        if t1 != t2:
            retour = 0
        else:
            i = 0
            retour = 1
            while i < t1 and not sort:
                if sont_égaux(arbre1[i],arbre2[i]) == 1:
                    i += 1
                else:
                    retour = 0
                    sort = True
    elif type(arbre1) == nltk.tree.Tree or type(arbre2) == nltk.tree.Tree:
        retour = 0
    else:
        retour = 1
    return retour;

# Renvoie le nb de noeuds :
def nb_noeuds(arbre):
    retour = 0
    if type(arbre) == nltk.tree.Tree:
        retour = 1
        for fils in arbre:
            retour += nb_noeuds(fils)
    return retour;
# Prend 2 arbres et calcule le nombre de sous-arbres communs :
def nb_sous_arbres(arbre1,arbre2):
    paires = paires_noeuds(arbre1,arbre2)
    retour = 0
    for paire in paires:
        if sont_égaux(paire[0],paire[1]) == 1:
            retour += 1
    return retour


## Pour les arbres pondérés


# Ajoute au bon endroit (pour que la liste soit triée) l'élément :
def ajoute_p(l_arbres,arbre):
    t = len(l_arbres)
    i = 0
    ajout = False
    while not(ajout) and i < t:
        if l_arbres[i]._label[0] > arbre._label[0]:
            ajout = True
            l_arbres.insert(i,arbre)
        i += 1
    if not ajout: l_arbres.append(arbre);

# On lui envoie un arbre et retourne une liste contenant les sous arbres triés selon leur étiquette:
def liste_sous_arbres2_p(l,a):
    if type(a) == nltk.tree.Tree:
        ajoute_p(l,a)
        for fils in a:
            liste_sous_arbres2_p(l,fils)

def liste_sous_arbres_p(arbre):
    a = copy.deepcopy(arbre)
    l = []
    liste_sous_arbres2_p(l,a)
    return l;

# Retourne la liste des paires de noeuds (enfin de sous-arbres) de arbre1*arbre2 ayant la même étiquette
def paires_noeuds_p(arbre1,arbre2):
    sort = False
    retour = []
    l1 = liste_sous_arbres_p(arbre1)
    l2 = liste_sous_arbres_p(arbre2)
    n1 = l1.pop()
    n2 = l2.pop()
    while not sort:
        if n1._label[0] < n2._label[0]: 
            if l2 != []: n2 = l2.pop()
            else: sort = True
        elif n1._label[0] > n2._label[0]: 
            if l1 != []: n1 = l1.pop()
            else: sort = True
        else:
            long = len(l2)
            i = 1
            retour.append((n1,n2))
            while i <= long and n1._label[0] == l2[-i]._label[0]:
                retour.append((n1,l2[-i]))
                i += 1
            if l1 != []: n1 = l1.pop()
            else: sort = True
                    
    return retour;
    
def mini_p(arbre):
    m = [arbre._label[1]]
    for fils in arbre:
        if type(fils) == nltk.tree.Tree:
            m.append(mini_p(fils))
    return min(m)

def delta_p(arbre1,arbre2):
    if arbre1._label[0] != arbre2._label[0]:
        return 0
    elif len(arbre1) == len(arbre2) == 1:
        return arbre1._label[1]*arbre2._label[1]
    else:
       r = arbre1._label[1]*arbre2._label[1]
       l = min([len(arbre1),len(arbre2)])
       for i in range(l):
           if type(arbre1[i]) == type(arbre2[i]) == nltk.tree.Tree:
               r *= (1 + delta_p(arbre1[i],arbre2[i]))
       return r;
        
# Calcule le nombre de sous-ensemble d'arbres communs
def noyau_sous_arbres_p(arbre1,arbre2):
    paires = paires_noeuds_p(arbre1,arbre2)
    retour = 0
    for paire in paires:
        retour += delta_p(paire[0],paire[1])
    return retour;

    

## TESTS :

# f = open('./articles_arbres/1/1.txt','rb')
# arbres = pickle.load(f)
# f.close()
# 
# # print(arbres[0])
# # print(arbres[1])
# # l1 = liste_sous_arbres(arbres[0])
# # l2  = liste_sous_arbres(arbres[1])
# # 
# # l = paires_noeuds(arbres[0],arbres[1])
# # noyau_sous_arbres(arbres[0],arbres[0])
# 
# f = open('./articles_arbres/1/2.txt','rb')
# arbres2 = pickle.load(f)
# f.close()
# 
# for i in range(10):
#     noyau_sous_arbres_forêt(arbres,arbres2)

# f = open('./articles_arbres/A.txt','rb')
# A = pickle.load(f)
# f.close()
# 
# noyau_sous_arbres_p(A[0],A[0])
# paires_noeuds_p(A[0],A[1])
