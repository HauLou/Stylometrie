## Les librairies dont on aura besoin :

import nltk.data
import os
from nltk.parse import stanford
import pickle

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


## Utilisation :

# liste_auteurs = ['larryelliott','kim-willsher','dominicfifield','fiona-harvey','julianborger']
# 
# genere_forets(liste_auteurs)