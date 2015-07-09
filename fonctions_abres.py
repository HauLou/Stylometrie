## Les librairies dont on aura besoin :
import nltk
import pickle
import copy

## charge_foret : reçoit un auteur et un article et retourne la forêt d'arbres correspondant

def charge_foret(auteur,article):
    f = open('./forets/'+auteur+'/'+str(article)+'.txt','rb')
    retour = pickle.load(f)
    f.close()
    return retour

## transforme : fonction qui reçoit un arbre et le modifie en un arbre où les noeuds sont des couples étiquette/poids=1

def transforme(arbre):
    if type(arbre) == nltk.tree.Tree:
        arbre._label = [arbre._label, 1]
        for fiston in arbre:
            transforme(fiston)

## long : retourne le nombre d'enfants d'un arbre

def long(arbre):
    retour = 0
    if type(arbre) == nltk.tree.Tree:
        for enfant in arbre:
            retour += 1
    return retour;

## prod_scal : le produit scalaire sur des arbres pondérés

def prod_scal(arbre1,arbre2):
    retour = 0
    if type(arbre1) == nltk.tree.Tree and type(arbre2) == nltk.tree.Tree and arbre1._label[0] == arbre2._label[0]:
        retour = arbre1._label[1]*arbre2._label[1]
        étiquettes = {}
        for arbre in arbre1:
            if type(arbre) == nltk.tree.Tree:
                if not arbre._label[0] in étiquettes:
                    étiquettes[arbre._label[0]] = 0
                étiquettes[arbre._label[0]] += 1
                ind = 0
                i = 0
                l = long(arbre2)
                while i < l and ind < étiquettes[arbre._label[0]]:
                    if type(arbre2[i]) == nltk.tree.Tree and arbre2[i]._label[0] == arbre._label[0]:
                        ind += 1
                        if ind == étiquettes[arbre._label[0]]:
                            retour += prod_scal(arbre,arbre2[i])
                    i += 1
    return retour;

## prod_scal2 : idem que prod_scal avec rajout d'un facteur 2^h quand on est à profondeur h

def prod_scal2(arbre1,arbre2):
    retour = 0
    if type(arbre1) == nltk.tree.Tree and type(arbre2) == nltk.tree.Tree and arbre1._label[0] == arbre2._label[0]:
        retour = arbre1._label[1]*arbre2._label[1]
        étiquettes = {}
        for arbre in arbre1:
            if type(arbre) == nltk.tree.Tree:
                if not arbre._label[0] in étiquettes:
                    étiquettes[arbre._label[0]] = 0
                étiquettes[arbre._label[0]] += 1
                ind = 0
                i = 0
                l = long(arbre2)
                while i < l and ind < étiquettes[arbre._label[0]]:
                    if type(arbre2[i]) == nltk.tree.Tree and arbre2[i]._label[0] == arbre._label[0]:
                        ind += 1
                        if ind == étiquettes[arbre._label[0]]:
                            retour += 2*prod_scal2(arbre,arbre2[i])
                    i += 1
    return retour;
    
## mult : prend un arbre pondéré et un scalaire et renvoie l.arbre

def mult(l, arbre):
    retour = copy.deepcopy(arbre)
    mult2(l,retour)
    return retour;

def mult2(l, retour):
    if type(retour) == nltk.tree.Tree:
        #print(type(l), type(retour._label))
        retour._label[1] *= l
        for fiston in retour:
            mult2(l,fiston)

## add : prend deux arbres pondérés et renvoie leur somme

def add(arbre1,arbre2):
    retour = copy.deepcopy(arbre1)
    copie2 = copy.deepcopy(arbre2)
    add2(retour,copie2)
    return retour;



def add2(arbre1,arbre2):
    if type(arbre1) == nltk.tree.Tree and type(arbre2) == nltk.tree.Tree and arbre1._label[0] == arbre2._label[0]:
        arbre1._label[1] += arbre2._label[1]
        étiquettes = {}
        déjà_pris = []
        l = long(arbre2)
        for arbre in arbre1:
            if type(arbre) == nltk.tree.Tree:
                if not arbre._label[0] in étiquettes:
                    étiquettes[arbre._label[0]] = 0
                étiquettes[arbre._label[0]] += 1
                ind = 0
                i = 0
                while i < l and ind < étiquettes[arbre._label[0]]:
                    if type(arbre2[i]) == nltk.tree.Tree and arbre2[i]._label[0] == arbre._label[0]:
                        ind += 1
                        if ind == étiquettes[arbre._label[0]]:
                            add2(arbre,arbre2[i])
                            #del(arbre2[i])
                            déjà_pris.append(i)
                    i += 1
        for i in range(l):
            if not i in déjà_pris and type(arbre2[i]) == nltk.tree.Tree:
                arbre1.append(arbre2[i])

## moyenne : prend une liste d'arbres et renvoie leur moyenne arithmétique

def moyenne(l_arbre):
    t = len(l_arbre)
    l = 1/t
    retour = l_arbre[0]
    for i in range(1,t):
        retour = add(retour,l_arbre[i])
    return mult(l,retour)

## Toutes les fonctions relatives aux noyaux d'arbres :

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
            retour += nb_noeuds(paire[0])
    return retour

# Prend 2 forêts et renvoie Somme sur les couples nb_sous_abres(a1,a2) :
def nb_sous_arbres_forêt(l_arbres1,l_arbres2):
    retour = 0
    for a1 in l_arbres1:
        for a2 in l_arbres2:
            retour += nb_sous_arbres(a1,a2)
    return retour;
    

