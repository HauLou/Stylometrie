## Import Librairies

from fonctions_ACP import *
import nltk
from nltk.probability import FreqDist
from fonctions import *
import pickle

## Fonction qui effectue le parcours des fichiers, et qui, à l'aide d'une fonction vecteur_*** passée en argument genere une matrice de données

def genere_matrice_donnees(auteurs, vecteur_frequence):
    # Initialisation de la matrice que l'on remplit
    X = []
    # A MODIFIER !!
    # A MODIFIER !!
    # A MODIFIER !!
    # A MODIFIER !!
    auteurs = ['1','2','3']
    for auteur in auteurs:
        for indice in range(nbArt(auteur)):
            vecteur = vecteur_frequence(auteur, indice)
            X.append(vecteur)
    return X;

## Liste des fonctions Bidouilles
# Toutes les fonctions sont construites de la même manière : elle prennnent en argument un auteur [type(auteur) = str] et un indice [type(indice) = int], et renvoie un vecteur de fréquence. Chaque fonction charge elle-même les fichiers dont elle aura besoin.

## Fréquence de mots

def vecteur_frequence_mots(auteur, indice):
    # Chargement du texte
    chemin  = './articles/'+auteur+'/'+str(indice)+'.txt'
    fichier = open(chemin, encoding = 'utf-8')
    text = pickle.load(fichier)
    # liste des mots utilisés. [pour l'instant : len(liste_mots) = 53 ]
    liste_mots=[',','.','the','be','to','of','and','a','in','that','have','I','it','for','not','on','with','he','as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when']
    # initialisation du vecteur que l'on va remplir et que l'on renverra
    X = []
    # Ici, on considère que l'entrée est un texte brut
    mots_texte = nltk.word_tokenize(texte)
    nb_mots = len(mots_texte)
    # Fonction à proprement parler
    frequences = FreqDist(mots_texte) # frequences = dictionnaires du nombre d'occurrence des mots
    for mot in liste_mots:
        freq = frequence(mot)/nb_mots
        X.append(freq)
    return X;
    
## Fréquence de natures de mots

def vecteur_frequence_nature(auteur, indice):
    # Chargement du fichier
    chemin = './articles_natures/'+auteur+'/'+str(indice)+'.txt'
    fichier = open(chemin, 'rb')
    texte = pickle.load(fichier)
    # liste des natures utilisées. [pour l'instant : len(liste_natures) = 53 ]
    liste_natures = ['LS', 'NN', 'VBZ', 'IN', 'DT', '.', 'WRB', 'NNS', 'NNP', 'JJ', 'JJR', 'VBP', 'MD', 'VB', 'PRP', 'VBD', 'VBN', ',', 'JJS', 'EX', 'CC', 'RB', 'TO', 'CD', 'VBG', ':', 'RP', 'WP', 'PRP$', '-NONE-', 'WDT', 'RBR', 'RBS', 'PDT', 'NNPS', '$', 'WP$', "''", 'POS', '``', '#', 'FW']
    # initialisation du vecteur que l'on va remplir et que l'on renverra
    X = []
    # Ici, l'entrée correspond déjà à ce que l'on veut: un tableau de natures.
    natures_texte = texte
    nb_mots = len(mots_texte)
    # Fonction à proprement parler
    frequences = FreqDist(mots_texte) # frequences = dictionnaires du nombre d'occurrence des mots
    for mot in liste_mots:
        freq = frequence(mot)/nb_mots
        X.append(freq)
    return X;

## Fréquence première lettre

# Définition de quelques fonctions auxiliares

def indice_lettre(lettre, alphabet):
    retour = -1
    for i in range(len(alphabet)):
        if lettre==alphabet[i]:
            retour = i
    return retour;

# Fonction vecteur_frequence_premiere_lettre

def vecteur_frequence_premiere_lettre(auteur, indice):
    # Chargement du fichier
    chemin = './articles/'+auteur+'/'+str(indice)+'.txt'
    fichier = open(chemin, encoding = 'utf-8')
    texte = pickle.load(fichier)
    # liste des lettres utilisées
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    taille_alphabet = len(alphabet) # [ici, taille_alphabet = 26] 
    # initialisation du vecteur que l'on renverra
    X = [0]*taille_alphabet
    # Transformation du texte en liste de mots
    mots_texte = nltk.word_tokenize(texte)
    nb_mots = len(mots_texte)
    for mot in mots_texte:
        X[indice_lettre(mot[0])] += 1
    for i in range(taille_alphabet):
        X[i] /= nb_mots
    return X;
    
## Fréquence des lettres

def vecteur_frequence_lettres(auteur, indice):
    # Chargement du fichier
    chemin = './articles/'+auteur+'/'+str(indice)+'.txt'
    fichier = open(chemin, encoding = 'utf-8')
    texte = pickle.load(fichier)
    # liste des lettres utilisées
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    taille_alphabet = len(alphabet) # [ici, taille_alphabet = 26] 
    # initialisation du vecteur que l'on renverra
    X = [0]*taille_alphabet
    # Ici, on travaille directement sur les lettres du texte
    nb_lettres = len(texte)
    # Remplissage
    for lettre in texte:
        X[indice_lettre(lettre)] += 1
    for i in range(taille_alphabet):
        X[i] /= nb_lettres
    return X;
    
## Fréquence longueur de mots
    
def vecteur_frequence_longueur_mots(auteur, indice):
    # Chargement du fichier
    chemin = './articles/'+auteur+'/'+str(indice)+'.txt'
    fichier = open(chemin, encoding = 'utf-8')
    texte = pickle.load(fichier)
    # Choix de la taille du vecteur
    longueurs = 30 # [ici, taille_alphabet = 30] 
    # initialisation du vecteur que l'on renverra
    X = [0]*longueurs
    # On travaille sur la liste des mots du texte
    mots_texte = nltk.word_tokenize(texte)
    nb_mots = len(mots_texte)
    # Remplissage
    for mot in mots_texte:
        if len(mot) < longueurs
            X[len(mot)] += 1
    for i in range(longueurs):
        X[i] /= nb_mots
    return X;

## Fréquence première lettre

# Définition de quelques fonctions auxiliares

def indice_lettre(lettre, alphabet):
    retour = -1
    for i in range(len(alphabet)):
        if lettre==alphabet[i]:
            retour = i
    return retour;

# Fonction vecteur_frequence_premiere_lettre

def vecteur_frequence_derniere_lettre(auteur, indice):
    # Chargement du fichier
    chemin = './articles/'+auteur+'/'+str(indice)+'.txt'
    fichier = open(chemin, encoding = 'utf-8')
    texte = pickle.load(fichier)
    # liste des lettres utilisées
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    taille_alphabet = len(alphabet) # [ici, taille_alphabet = 26] 
    # initialisation du vecteur que l'on renverra
    X = [0]*taille_alphabet
    # Transformation du texte en liste de mots
    mots_texte = nltk.word_tokenize(texte)
    nb_mots = len(mots_texte)
    for mot in mots_texte:
        X[indice_lettre(mot[-1])] += 1
    for i in range(taille_alphabet):
        X[i] /= nb_mots
    return X;

## Fréquence Bigrams

# Fonction auxiliaire
def estBigram(indice, texte, bigrams):
    retour = -1
    for j in range(len(bigrams)):
        if (bigrams[j]==texte[indice: indice+2]):
            retour = j
    return retour;

# Fonction vecteur_frequence_bigram à proprement parler
def vecteur_frequence_bigram(auteur, indice):
    # Chargement du fichier
    chemin = './articles/'+auteur+'/'+str(indice)+'.txt'
    fichier = open(chemin, encoding = 'utf-8')
    texte = pickle.load(fichier)
    # Liste des bigrams utilisés
    bigrams = ['th', 'he', 'in', 'en', 'nt', 're', 'er', 'an', 'ti', 'es', 'on', 'at', 'se', 'nd', 'or', 'ar', 'al', 'te', 'co', 'de', 'to', 'ra', 'et', 'ed', 'it', 'sa', 'em', 'ro']
    nb_bigrams = len(bigrams)
    # Initialisation de la matrice
    X = [0]* nb_bigrams
    nb_lettres = len(texte)
    # Parcours du texte à la recherche de bigrams
    for indice_lettre in range(nb_lettres -1):
        estbig = estBigram(indice, texte, bigrams)
        if (estbig != -1):
            X[estbig] += 1
    for i in range(nb_bigrams):
        X[i] /= nb_lettres
    return X;
    
## Vecteurs fréquence longueur de phrases

# Fonction de classification des phrases en fonction de leur longueur [Classification de 5 en 5, puis tous les > 120 ensembles]

# Fonction de classification 
def classification(phrase):
    retour = 0
    longueur = len(phrase)
    if (longueur > 120):
        retour = 24
    else:
        retour = longueur//5
    return retour;

# Fonction de vecteur phrases à proprement parler
def vecteur_frequence_longueur_mots(auteur, indice):
    # Chargement fichier
    chemin = './articles/'+str(auteur)+'/'+str(article)+'.txt'
    fichier = open(chemin, encoding = 'utf-8')
    texte = fichier.read()
    # Définition du vecteur que l'on renverra
    nb_tailles = 25
    X = [0] * nb_tailles
    # Transformation du texte en liste de phrases
    phrases = nltk.sent_tokenize(texte)
    nb_phrases = len(phrases)
    # Parcours des phrases
    for phrase in phrases:
        mots_phrase = nltk.word_tokenize(phrase)
        taille = classification(mots_phrase)
    



        phrases = nltk.sent_tokenize(texte)
        for phrase in phrases:
            listeMots = nltk.word_tokenize(phrase)
            taille = classification(listeMots)
            X[numArt, taille] += 1
            #print(X[numArt, taille])
        for i in range(p):
            X[numArt, i] /= len(phrases)
        numArt += 1