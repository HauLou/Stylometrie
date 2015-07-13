## Les librairies dont on aura besoin :

import nltk.data
import os
from nltk.parse import stanford
import pickle
from nltk.tag import StanfordPOSTagger

## La fonction genere_forets qui prend une liste de noms d'auteurs en paramètre et génère dans le dossier ./forets

def genere_forets(l_auteurs, STANFORD_PARSER='../stanford', STANFORD_MODELS='../stanford', JAVAHOME='/import/lhauseux/jre1.8.0_45/bin', model_path="../stanford/englishPCFG.ser.gz",english_pickle='/import/lhauseux/nltk_data/tokenizers/punkt/english.pickle'):
    # On règle les paramètres du prog' de Stangord et de java :
    os.environ['STANFORD_PARSER'] = STANFORD_PARSER
    os.environ['STANFORD_MODELS'] = STANFORD_MODELS
    os.environ['JAVAHOME'] = JAVAHOME
    parser = stanford.StanfordParser(model_path=model_path,java_options='-mx15000m')
    
    nltk.internals.config_java(options='-xmx2G')
    detecteur = nltk.data.load(english_pickle)
    
    # On crée le dossier forets si nécessaire
    if not os.path.isdir('./forets'):
        os.mkdir('./forets')
    for auteur in l_auteurs:
        # On crée le dossier propre à l'auteur si nécessaire
        if not os.path.isdir('./forets/'+auteur):
            os.mkdir('./forets/'+auteur)
        articles = os.listdir('./auteurs/'+auteur)
        for article in articles:
            if article != 'liens.txt':
                # On récupère l'article au format texte
                f = open('./auteurs/'+auteur+'/'+article,'r')
                contenu = f.read()
                f.close()
                # On le transforme en forêts d'arbres
                contenu = detecteur.tokenize(contenu.strip())
                contenu = parser.raw_parse_sents(contenu)
                arbres = []
                for i in contenu:
                    for j in i:
                        arbres.append(j)
                # On enregistre
                f = open('./forets/'+auteur+'/'+article,'wb')
                pickle.dump(arbres,f)
                f.close()
                print(auteur,article)



## Regénère les forêts où les étiquettes ne contiennent plus les mots de la phrase mais des chaînes vides :

def enleve_etiquettes(arbre):
    if type(arbre) != nltk.tree.Tree:
        print(arbre)
        print(type(arbre))
        exit()
    fils = arbre[:]
    if type(fils[0]) == str:
        arbre[:] = ['']*len(fils)
    else:
        for fiston in fils:
            enleve_etiquettes(fiston)


def charge_foret_sans_etiquettes(auteur, i):
    f = open('./forets_sans_etiquettes/'+auteur+'/'+str(i)+'.txt','rb')
    ret = pickle.load(f)
    f.close()
    return ret

def charge_foret(auteur, i):
    f = open('./forets/'+auteur+'/'+str(i)+'.txt','rb')
    ret = pickle.load(f)
    f.close()
    return ret


def genere_forets_sans_etiquettes(l_auteurs):
    # On crée le dossier forets si nécessaire
    if not os.path.isdir('./forets_sans_etiquettes'):
        os.mkdir('./forets_sans_etiquettes')
    for auteur in l_auteurs:
        # On crée le dossier propre à l'auteur si nécessaire
        if not os.path.isdir('./forets_sans_etiquettes/'+auteur):
            os.mkdir('./forets_sans_etiquettes/'+auteur)
        articles = os.listdir('./forets/'+auteur)
        for article in articles:
            if article != 'liens.txt':
                # On récupère la forêt
                f = open('./forets/'+auteur+'/'+article,'rb')
                foret = pickle.load(f)
                f.close()
                # On le transforme en forêts d'arbres sans étiquettes
                for arbre in foret:
                    enleve_etiquettes(arbre)
                # On enregistre
                f = open('./forets_sans_etiquettes/'+auteur+'/'+article,'wb')
                pickle.dump(foret,f)
                f.close()
                print(auteur,article)

## La fonction genere_listes_natures qui prend une liste de noms d'auteurs en parmaètre et génère dans le dossier ./listes_natures


def genere_liste_natures(l_auteurs, STANFORD_PARSER='../stanford', STANFORD_MODELS='../stanford', JAVAHOME='/import/lhauseux/jre1.8.0_45/bin', bid = '/import/lhauseux/Pyzo/pyzo2015a/stanford-postagger-2015-04-20/models/english-bidirectional-distsim.tagger', pt = '/import/lhauseux/Pyzo/pyzo2015a/stanford-postagger-2015-04-20/stanford-postagger.jar'):
    # On règle les paramètres du prog' de Stangord et de java :
    os.environ['STANFORD_PARSER'] = STANFORD_PARSER
    os.environ['STANFORD_MODELS'] = STANFORD_MODELS
    os.environ['JAVAHOME'] = JAVAHOME
    
    st = StanfordPOSTagger(bid,path_to_jar=pt,java_options='-mx15000m') 
    nltk.internals.config_java(options='-xmx2G')

    
    # On crée le dossier forets si nécessaire
    if not os.path.isdir('./listes_natures'):
        os.mkdir('./listes_natures')
    for auteur in l_auteurs:
        # On crée le dossier propre à l'auteur si nécessaire
        if not os.path.isdir('./listes_natures/'+auteur):
            os.mkdir('./listes_natures/'+auteur)
        articles = os.listdir('./auteurs/'+auteur)
        for article in articles:
            if article != 'liens.txt':
                # On récupère l'article au format texte
                f = open('./auteurs/'+auteur+'/'+article,'r')
                contenu = f.read()
                f.close()
                # On le transforme en forêts d'arbres
                contenu = nltk.word_tokenize(contenu)
                contenu = st.tag(contenu)
                contenu = [c[1] for c in contenu]
                # On enregistre
                f = open('./listes_natures/'+auteur+'/'+article,'wb')
                pickle.dump(contenu,f)
                f.close()
                print(auteur,article)


## Utilisation :


liste_auteurs = ['larryelliott','kim-willsher','dominicfifield','fiona-harvey','julianborger']

genere_forets_sans_etiquettes(liste_auteurs)