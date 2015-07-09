## Import des librairies

#from fonctions_auxiliaires import liste_dossiers
from fonctions_ACP import *
from fonctions import *
import os
import pickle
import vecteur_depuis_texte as v_texte
import vecteur_depuis_liste_natures as v_natures

## Variables Globales

# A CORRIGER
#auteurs = liste_dossiers('./auteurs/')
# auteurs = ['dominicfifield','fiona-harvey','julianborger','kim-willsher','larryelliott']
auteurs = ['dominicfifield','kim-willsher']
nb_auteurs = len(auteurs)


## Définition des paramètres par défaut

def accepte(article):
    return True;

## Fonction article to vecteur

poids_par_defaut = None

def vecteur_article(auteur, indice, poids = None, ):
    return;

## Fonction qui charge un fichier

def charge_fichier(chemin, binaire = True):
    fichier = ""
    if binaire:
        fichier = open(chemin, 'rb')
        retour = pickle.load(fichier)
    else:
        fichier = open(chemin, encoding = 'utf-8')
        retour = fichier.read()
    fichier.close()
    return retour;
    
# # Centre de débuggage
# chemin1 = './auteurs/dominicfifield/0.txt'
# fichier1 = charge_fichier(chemin1, binaire = False)
# print(fichier1)
# 
# chemin2 = './forets/dominicfifield/0.txt'
# fichier2 = charge_fichier(chemin2)
# print(fichier2)




## Fonction principale

def fonction_principale(nb_articles_par_auteur = 200, poids = None, tSNE = False, ACP = True, kmeans = False, critere = accepte):
    if type(nb_articles_par_auteur) == int:
        nb_articles_par_auteur = [nb_articles_par_auteur]*nb_auteurs
    
    tailles_vecteurs = {}
    X = []
    
    for auteur in range(len(auteurs)):
        i = 0
        nb_articles_pris = 0
        while nb_articles_pris < nb_articles_par_auteur[auteur]:
            texte = charge_texte(auteurs[auteur],i)
            if critere(texte):
                ligne = []
                for fonction in dir(v_texte):
                    if fonction[:8] == 'vecteur_':
                        # On applique la fonction
                        v = eval('v_texte.'+fonction+'(texte)')
                        tailles_vecteurs[fonction] = len(v)
                        ligne += v
                
                liste_natures = charge_liste_natures(auteurs[auteur],i)
                for fonction in dir(v_natures):
                    if fonction[:8] == 'vecteur_':
                        # On applique la fonction
                        v = eval('v_natures.'+fonction+'(liste_natures)')
                        tailles_vecteurs[fonction] = len(v)
                        ligne += v
                X.append(ligne)
                nb_articles_pris += 1
                print(auteur,nb_articles_pris)
            i += 1
    X = np.array(X)
    
    trace_ACP(X,nb_articles_par_auteur)
    return X,tailles_vecteurs
    # if tSNe:
    #     X_tsne = tSNE(X)
    # if ACP:
    #     X_acp = ACP(X)
    # if kmeans:
    #     X_kmeans = kmeans(X)
    # return;