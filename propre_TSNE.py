##

import numpy as np
from fonctions_ACP import *
from sklearn.decomposition import PCA
##

def identité(x):
    return x

# rapport doit être une fonction impaire croissante
def reduit_dim(X, Distances = None,nouv_dim = 2, rapport = identité, frottements = 0.999, nb_iter = 20):
    n,p = np.shape(X)
    
    if Distances == None:
        Distances = X.dot(X.T)
        Di = np.reshape(np.diag(Distances),(n,1))
        Ai = Di.dot(np.ones((1,n)))
        Distances = Ai + Ai.T - 2*Distances
        Distances = np.sqrt(Distances)
    X_ACP = X
    
    while p > nouv_dim:
        p -= 1
        print(p)
        X_ACP = PCA(n_components=p).fit_transform(X_ACP)
        # acp = PCA(n_components=p).fit(X_ACP).components_
        # print(X_ACP)
        # Le vecteur des vitesses :
        V = np.zeros((n,p))
        for k in range(nb_iter):
            nouv_Distances = X_ACP.dot(X_ACP.T)
            Di = np.reshape(np.diag(nouv_Distances),(n,1))
            Ai = Di.dot(np.ones((1,n)))
            nouv_Distances = Ai + Ai.T - 2*nouv_Distances
            nouv_Distances = np.sqrt(nouv_Distances)
            Diff = nouv_Distances - Distances
            # print(X_ACP)
            print(k, Diff)
            # if k == 0:
            #     print('k = 0')
            #     print(Diff)
            # if k == (nb_iter-1):
            #     print('k = nb_iter-1')
            #     print(Diff)
            for i in range(n):
                for j in range(n):
                    d = X_ACP[j] - X_ACP[i]
                    # La vitesse change de l'accélération (somme des forces)
                    c = d * rapport(Diff[i,j])
                    V[i] += c
            
            for i in range(n):
                V[i] *= (1 - frottements)
                X_ACP[i] += V[i]
    return X_ACP

A = np.array([
[1,1,1],
[1,0,1],
[0,1,1],
[-1,-2,0]
])

# Dist = np.sqrt(D)
# r = reduit_dim(Gram/11,nouv_dim=2)