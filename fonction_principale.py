## Import des librairies

#from fonctions_auxiliaires import liste_dossiers
from fonctions_ACP import *
from fonctions import *
import os
import pickle
import vecteur_depuis_texte as v_texte
import vecteur_depuis_liste_natures as v_natures
import vecteur_depuis_foret as v_foret
import kernels
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


## Variables Globales

# A CORRIGER
#auteurs = liste_dossiers('./auteurs/')
auteurs = ['dominicfifield','fiona-harvey','julianborger','kim-willsher','larryelliott']
# auteurs = ['larryelliott','dominicfifield']
nb_auteurs = len(auteurs)


## Définition des paramètres par défaut

def accepte(article):
    return True;

def plus_1000_char(article):
    t = len(article)
    return t >= 1000

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

def fonction_principale(nb_articles_par_auteur = 100,liste_kernels = [], poids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], tsne = True, acp = True, kmeans = False, critere = plus_1000_char):
    if type(nb_articles_par_auteur) == int:
        nb_articles_par_auteur = [nb_articles_par_auteur]*nb_auteurs
    
    tailles_vecteurs = []
    X = []
    nb_fonctions = 0
    
    textes_pris = []
    for auteur in range(len(auteurs)):
        i = 0
        nb_articles_pris = 0
        while nb_articles_pris < nb_articles_par_auteur[auteur]:
            texte = charge_texte(auteurs[auteur],i)
            if critere(texte):
                textes_pris.append((auteurs[auteur],i))
                ind_fonction = 0
                natures = charge_liste_natures(auteurs[auteur],i)
                foret = charge_foret(auteurs[auteur],i)
                ligne = []
                
                type_fonctions = ['texte','natures','foret']
                
                for t in type_fonctions:
                    fonctions = eval('dir(v_'+t+')')
                    for fonction in fonctions:
                        if fonction[:8] == 'vecteur_':
                            v = eval('v_'+t+'.'+fonction+'('+t+')')
                            if auteur == 0 and nb_articles_pris == 0:
                                tailles_vecteurs.append((fonction,len(v)))
                                nb_fonctions += 1
                            if type(poids) == int:
                                ligne += [a*poids for a in v]
                            else:
                                ligne += [a*poids[ind_fonction] for a in v]
                            ind_fonction += 1
                            

                X.append(ligne)
                nb_articles_pris += 1
                print(auteur,nb_articles_pris,i)
            i += 1
    X = np.array(X)
    
    ind = 0
    for fonc,t in tailles_vecteurs:
        X_f = X[:,ind:(ind+t)]
        G_f = X_f.dot(X_f.T)
        f = open('./G/'+fonc+'.txt','wb')
        pickle.dump(G_f,f)
        f.close()
        ind += t
    
    G = {}
    n = len(textes_pris)
    ind_ker = 0
    for ker in liste_kernels:
        G[ker] = np.zeros((n,n))
        for i in range(n):
            print(ker,i)
            foret1 = charge_foret(textes_pris[i][0],textes_pris[i][1])
            for j in range(i+1):
                foret2 = charge_foret(textes_pris[j][0],textes_pris[j][1])
                G[ker][i,j] = G[ker][j,i] = eval('kernels.kernel_'+ker+'(foret1,foret2)')
        ind_ker += 1
    

    if acp:
        X_acp = ACP(X)
    if tsne:
        modele = TSNE(n_components=2)
        print(np.shape(X))
        Y = modele.fit_transform(X_acp) 
        
        couleurs = ['b','r','g','y','k','m']
        n = len(X)
        plt.figure(figsize=(8,8))
        for i in range(n):
            plt.plot(Y[i,0], Y[i,1], '+', c = couleur(i, nb_articles_par_auteur, couleurs)) 
    if kmeans:
        X_kmeans = kmeans(X)
    
    trace_ACP(X_acp,nb_articles_par_auteur)
    return X,G,tailles_vecteurs,nb_fonctions


X,G,t,nb_fonctions = fonction_principale()