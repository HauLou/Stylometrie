def fonction_principale(nb_articles_auteurs, critere, poids):
    X = assemble_matrice(nb_articles_auteurs, critere, poids)
    
    dessine_ACP(X)
    dessine_tSNE(X)
    lance_kmeans(X)
    return;
    
def assemble_matrice(nb_articles_auteurs, critere, poids):
    X = []
    for auteur in range(nb_articles_auteurs):
        taille = nb_articles_auteurs[auteur]
        article = 0
        while (critere(article) and article < taille):
            vecteur = vecteur_genere(auteur, article)
            X.append(vecteur)
            article += 1
    return X;

