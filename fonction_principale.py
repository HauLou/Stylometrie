## Import des librairies

#from fonctions_auxiliaires import liste_dossiers
import os
import pickle

## Variables Globales

# A CORRIGER
#auteurs = liste_dossiers('./auteurs/')
auteurs = ['dominicfifield','fiona-harvey','julianborger','kim-willsher','larryelliott']
nb_auteurs = len(auteurs)


## Définition des paramètres par défaut

def accepte(article):
    return True;

## Fonction article to vecteur

poids_par_defaut = None

def vecteur_article(auteur, indice, poids = None, ):
    

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
    
# Centre de débuggage
chemin1 = './auteurs/dominicfifield/0.txt'
fichier1 = charge_fichier(chemin1, binaire = False)
print(fichier1)

chemin2 = './forets/dominicfifield/0.txt'
fichier2 = charge_fichier(chemin2)
print(fichier2)


## Fonction assemble_matrice

def assemble_matrice(nb_articles_par_auteur, critere):
    
    for auteur in auteurs:
        indice = auteurs.index
        article = 0
        chemin = './auteurs/'+auteur
        while (article != nb_artcles_par_auteur[indice] and article < len(os.path.listdir(chemin) )):
            if critere(article)

## Fonction principale

def fonction_principale(nb_articles_par_auteur = [100]*nb_auteurs, poids = None, tSNE = False, ACP = True, kmeans = False, critere = None):
    
    X = assemble_matrice(nb_a
    
    if tSNe:
        X_tsne = tSNE(X)
    if ACP:
        X_acp = ACP(X)
    if kmeans:
        X_kmeans = kmeans(X)
    return;