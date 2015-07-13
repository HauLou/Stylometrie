## Bibliothèques

import nltk

## elagage : fonction qui reçoit un arbre pondéré et un poids minimum et élague toutes les branches où le poids est y est inférieur 


def est_arbre(arbre): return type(arbre) == nltk.tree.Tree


def elagage(arbre,p_min):
	if est_arbre(arbre):
		if arbre._label[] >= p_min:
			for fiston in arbre:
				elagage(fiston,p_min)
		else:
			del(arbre)


