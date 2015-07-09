## Librairies

# from fonctions_ACP import *
import nltk
# from nltk.probability import FreqDist
# from fonctions import *
import pickle

## Liste des fonctions Bidouilles
# Toutes les fonctions sont construites de la même manière : elle prennnent en argument un auteur [type(auteur) = str] et un indice [type(indice) = int], et renvoie un vecteur de fréquence. Chaque fonction charge elle-même les fichiers dont elle aura besoin.
## Fréquence de la ponctuation

def vecteur_frequence_ponctuation(texte):
    # liste des mots utilisés. [pour l'instant : len(liste_mots) = 53 ]
    liste_signes = [',','?',';','.',':','!','...','(',')','-','—','–']
    taille_vecteur = len(liste_signes) 
    # initialisation du vecteur que l'on renverra
    X = [0]*taille_vecteur
    # Transformation du texte en liste de mots
    mots_texte = nltk.word_tokenize(texte)
    
    for mot in mots_texte:
        if mot in liste_signes:
            X[liste_signes.index(mot)] += 1
    
    nb_signes = sum(X)
    X = [f/nb_signes for f in X]
    return X;
    
    
## Fréquence de mots courants et non contextuels

def vecteur_frequence_mots(texte):
    # liste des mots utilisés. [pour l'instant : len(liste_mots) = 53 ]
    liste_mots=[',','.','the','be','to','of','and','a','in','that','have','I','it','for','not','on','with','he','as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when']
    taille_vecteur = len(liste_mots) 
    # initialisation du vecteur que l'on renverra
    X = [0]*taille_vecteur
    # Transformation du texte en liste de mots
    mots_texte = nltk.word_tokenize(texte)
    nb_mots = len(mots_texte)
    for mot in mots_texte:
        if mot in liste_mots:
            X[liste_mots.index(mot)] += 1
    X = [f/nb_mots for f in X]
    return X;
    

## Fréquence première lettre



# Fonction vecteur_frequence_premiere_lettre

def vecteur_frequence_premiere_lettre_minuscule(texte):

    # liste des lettres utilisées
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    taille_vecteur = len(alphabet) # [ici, taille_alphabet = 26] 
    # initialisation du vecteur que l'on renverra
    X = [0]*taille_vecteur
    # Transformation du texte en liste de mots
    mots_texte = nltk.word_tokenize(texte)
    nb_mots = len(mots_texte)
    for mot in mots_texte:
        if mot[0] in alphabet:
            X[alphabet.index(mot[0])] += 1
    X = [f/nb_mots for f in X]
    return X;

def vecteur_frequence_premiere_lettre_majuscule(texte):

    # liste des lettres utilisées
    alphabet = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
    taille_vecteur = len(alphabet) # [ici, taille_alphabet = 26] 
    # initialisation du vecteur que l'on renverra
    X = [0]*taille_vecteur
    # Transformation du texte en liste de mots
    mots_texte = nltk.word_tokenize(texte)
    nb_mots = len(mots_texte)
    for mot in mots_texte:
        if mot[0] in alphabet:
            X[alphabet.index(mot[0])] += 1
    X = [f/nb_mots for f in X]
    return X;
    
## Fréquence des lettres

def vecteur_frequence_lettres_minuscule(texte):
    # liste des lettres utilisées
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    taille_vecteur = len(alphabet) 
    # initialisation du vecteur que l'on renverra
    X = [0]*taille_vecteur

    
    for l in texte:
        if l in alphabet:
            X[alphabet.index(l)] += 1
    nb_lettres = sum(X)
    X = [f/nb_lettres for f in X]
    return X;

def vecteur_frequence_lettres_majuscule(texte):
    # liste des lettres utilisées
    alphabet = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
    taille_vecteur = len(alphabet) 
    # initialisation du vecteur que l'on renverra
    X = [0]*taille_vecteur

    
    for l in texte:
        if l in alphabet:
            X[alphabet.index(l)] += 1
    nb_lettres = sum(X)
    X = [f/nb_lettres for f in X]
    return X;
    
## Fréquence longueur de mots
    
def vecteur_frequence_longueur_mots(texte):
    # Choix de la taille du vecteur
    longueurs = 30 # [ici, taille_alphabet = 30] 
    # initialisation du vecteur que l'on renverra
    X = [0]*longueurs
    # On travaille sur la liste des mots du texte
    mots_texte = nltk.word_tokenize(texte)
    nb_mots = len(mots_texte)
    # Remplissage
    for mot in mots_texte:
        if len(mot) < longueurs:
            X[len(mot)] += 1
    X = [f/nb_mots for f in X]
    return X;


## Fréquence Bigrams

# Fonction auxiliaire
def estBigramme(indice, texte, bigrammes):
    retour = -1
    for j in range(len(bigrammes)):
        if bigrammes[j] == texte[indice: indice+2]:
            retour = j
    return retour;

# Fonction vecteur_frequence_bigrammes à proprement parler

def vecteur_frequence_bigrammes(texte):
    # Liste des bigrammes utilisés
    bigrammes = ['th', 'he', 'in', 'en', 'nt', 're', 'er', 'an', 'ti', 'es', 'on', 'at', 'se', 'nd', 'or', 'ar', 'al', 'te', 'co', 'de', 'to', 'ra', 'et', 'ed', 'it', 'sa', 'em', 'ro']
    nb_bigrammes = len(bigrammes)
    # Initialisation de la matrice
    X = [0]* nb_bigrammes
    nb_lettres = len(texte)
    # Parcours du texte à la recherche de bigrams
    for indice_lettre in range(nb_lettres -1):
        estbig = estBigramme(indice_lettre, texte, bigrammes)
        if (estbig != -1):
            X[estbig] += 1
    X = [f/nb_lettres for f in X]
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
def vecteur_frequence_longueur_mots(texte):
    # Définition du vecteur que l'on renverra
    nb_tailles = 25
    X = [0] * nb_tailles
    # Transformation du texte en liste de phrases
    phrases = nltk.sent_tokenize(texte)
    nb_phrases = len(phrases)
    # Parcours des phrases
    for phrase in phrases:
<<<<<<< HEAD
        mots_phrase = nltk.word_tokenize(phrase)
        taille = classification(mots_phrase)

        phrases = nltk.sent_tokenize(texte)
        for phrase in phrases:
            listeMots = nltk.word_tokenize(phrase)
            taille = classification(listeMots)
            X[taille] += 1
        nb_phrases= len(phrases)
        X = [t/nb_phrases for t in X]

## Fonction fréquence de trigrams

def esttrigram(indice, texte, trigrams):
    retour = -1
    for j in range(len(trigrams)):
        if (trigrams[j]==texte[indice: indice+3]):
            retour = j
    return retour;

def frequence_trigrams(texte):
    # Données sur le texte
    longueur_texte = len(texte)
    # Définition des trigrams les plus fréquents
    trigrams = ['the', 'ing', 'and', 'her', 'ere', 'ent', 'tha', 'nth', 'was', 'eth', 'for', 'dth']
    nb_trigrams = len(trigrams)
    # Définition de la matrice que l'on renverra
    X = [0]*nb_trigrams
    # A la recherche des trigrammes -- Boucle sur les lettres
    for indice_lettre in range(len(texte)-2):
        est_trigram = esttrigram(indice_lettre, texte, trigrams)
        if (est_trigram!= -1):
            X[est_trigram] += 1
    X = [i/longueur_texte for i in X]
    return X;
    
## Fonction nombre de voyelles

## Fonction auxiliaire

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def isVoyelle(lettre):
    voyelles = ['a','e','u', 'i', 'o', 'y']
    retour = lettre in voyelles
    return retour;

## Génération de la Matrice

def vecteur_frequence_voyelle(texte):
    # Informations relatives au texte
    len_texte = len(texte)
    # Définition des voyelles
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    nb_voyelles = len(voyelles)
    # Définition du vecteur que l'on rend
    X = [0]* nb_voyelles
    # A la recherche des voyelles -- boucle sur le texte
    for lettre in texte:
        if lettre in voyelles:
            X[voyelles.index(lettre)] += 1
    X = [i/len_texte for i in X]
    return X;

## Vecteur de fréquence des bigrammes de fin

def estBigram(texte, bigrams):
    retour = -1
    for j in range(len(bigrams)):
        if (bigrams[j]==texte[-2]+texte[-1]):
            retour = j
    return retour;

# Fonction sur les bigrammes à la fin d'un mot à proprement parler
def vecteur_frequence_bigrammes_fin(texte):
    # Définition des données relatives au texte
    len_texte = len(texte)
    texte = nltk.word.tokenize(texte)
    # Définition des bigrammes
    bigrams = ['th', 'he', 'in', 'en', 'nt', 're', 'er', 'an', 'ti', 'es', 'on', 'at', 'se', 'nd', 'or', 'ar', 'al', 'te', 'co', 'de', 'to', 'ra', 'et', 'ed', 'it', 'sa', 'em', 'ro']
    nb_bigrams = len(bigrams)
    # Définition vecteur X de retour
    X = [0]*nb_bigrams
    # A la recherche de bigrammes à la fin des mots
    for mot in texte:
        if 2 < len(mot):
            estbig = estBigram(mot, bigrams)
                if (estbig!=-1):
                    X[numArt, estbig] += 1
    X = [i/len_texte for i in X]
=======
        listeMots = nltk.word_tokenize(phrase)
        taille = classification(listeMots)
        X[taille] += 1
    nb_phrases= len(phrases)
    X = [t/nb_phrases for t in X]
>>>>>>> 2c27ca7a1a24d02af724814478eb9fa26d878c85
    return X;