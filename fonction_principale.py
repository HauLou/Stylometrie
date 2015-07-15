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
import sklearn.cluster
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.cluster import AffinityPropagation
from propre_TSNE import *

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
    return (t >= 1000 and (article.find('video') == -1))

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

def fonction_principale(nb_articles_par_auteur = 50,liste_kernels = [], poids = {'vecteur_frequence_bigrammes_fin': 1,'vecteur_frequence_lettres_majuscule': 1, 'vecteur_frequence_premiere_lettre_majuscule': 1,'vecteur_frequence_bigrammes': 1, 'vecteur_frequence_premiere_lettre_minuscule': 1,'vecteur_frequence_longueur_mots': 1, 'vecteur_frequence_mots': 1, 'vecteur_frequence_lettres_minuscule': 1,'vecteur_frequence_voyelle': 1, 'vecteur_frequence_nature': 1, 'vecteur_frequence_ponctuation': 0,'vecteur_frequence_couples_aretes': 1, 'vecteur_frequence_noeuds':0, 'vecteur_struct_arbre': 0}, tsne = True, acp = True, kmeans = False, critere = plus_1000_char):
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
                            ligne += v
                            ind_fonction += 1
                            

                X.append(ligne)
                nb_articles_pris += 1
                print(auteur,nb_articles_pris,i)
            i += 1
    X = np.array(X)
    
    n = len(X)
    X_p = np.zeros((n,1))
    ind = 0
    i = 0
    Gram = np.zeros((n,n))
    for fonc,t in tailles_vecteurs:
        X_f = X[:,ind:(ind+t)]
        X_p = np.concatenate((X_p,(X_f*poids[fonc])),axis = 1)
        G_f = X_f.dot(X_f.T)
        f = open('./G/'+fonc+'.txt','wb')
        pickle.dump(G_f,f)
        f.close()
        ind += t
        G_f = reduire(G_f)
        G_f = centrer(G_f)
        G_f = reduire(G_f)
        Gram += G_f*poids[fonc]
        i += 1
    
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
    
    return X_p,Gram


X,Gram = fonction_principale()


##

plt.figure()
plt.ion()
plt.jet()


f = open('./G/vecteur_frequence_noeuds.txt','rb')
G_f = pickle.load(f)
f.close()

G2 = reduire(G_f)
G3 = centrer(G2)
G4 = reduire(G3)
G5 = centrer(G_f)
G6 = reduire(G5)

ax = plt.matshow(G4)
##
print('Classificiation')
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import SpectralClustering
from sklearn.cluster.bicluster import SpectralBiclustering
from sklearn.manifold import TSNE
# C1 = sklearn.cluster.AgglomerativeClustering(n_clusters=5, affinity='precomputed')
# 
# R1 = C1.fit_predict(Gram)
# 
n = len(Gram)
Di = np.reshape(np.diag(Gram),(n,1))
M = Di.dot(np.ones((1,n)))

D = M + M.T - 2*Gram

C2 = AffinityPropagation(affinity='precomputed')
C1 = KMeans(n_clusters = 5)
C3 = AgglomerativeClustering(n_clusters=5, affinity='precomputed',linkage='average')
C4 = SpectralClustering(n_clusters=5,affinity='precomputed')
C5 = SpectralBiclustering(n_clusters=(5,5))

R1 = C1.fit_predict(D)
R2 = C2.fit_predict(D)
R3 = C3.fit_predict(D)
R4 = C4.fit_predict(Gram +11)
R5 = C5.fit(D)

print(R4)

modèle = TSNE(n_components=2,metric='precomputed')
Trans = modèle.fit_transform(D)

G_ACP = ACP(Gram,precomputed=True)

trace_ACP(G_ACP,[10]*5)
##

import propre_TSNE as pt

r = pt.reduit_dim(np.array([[0,1],[1,0]]),np.array([[0,2],[2,0]]),1)