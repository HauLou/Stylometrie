##

import numpy as np
from fonctions_ACP import *
from sklearn.decomposition import PCA
##

def identité(x):
    return x

def carré(M):
    return M ** 2

def cube(M):
    return M ** 3

def exp_moins1(M):
    return np.expm1(M)

def racine(M):
    return np.sqrt(M)

def xxp1(M):
    M2 = M ** 2
    return (M + M2)

def saut_a_4(M):
    n = len(M)
    ret = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if M[i,j] <= 3.2:
                # ret[i,j] = M[i,j]/3
                ret[i,j] = 0
            else:
                # ret[i,j] = 4*M[i,j]
                # ret[i,j] = 3.5+M[i,j]
                ret[i,j] = 3*M[i,j]
    return ret


# rapport doit être une fonction impaire croissante
def reduit_dim(X, Distances = None,nouv_dim = 2, rapport = identité, frottements = 0.95, nb_iter = 50, seuil_var = 0.05, distance_souhaitée=saut_a_4):
    n,p = np.shape(X)
    
    restant = 1 - frottements
    restant /= n
    
    
    if Distances == None:
        Distances = X.dot(X.T)
        Di = np.reshape(np.diag(Distances),(n,1))
        Ai = Di.dot(np.ones((1,n)))
        Distances = Ai + Ai.T - 2*Distances
        Distances = np.sqrt(Distances)
        # return (Distances)
    X_ACP = X
    
    # # #
    # On veut ces distances :
    Distances = distance_souhaitée(Distances)
    # return (Distances)
    # # #
    
    while p > nouv_dim:
        
        # Combien de dimensions va-t'on supprimer ? i+1 (de sorte qu'on supprime moins de seuil_var de l'énergie)
        acp = PCA(n_components=p)
        acp.fit(X)
        sigmas = acp.explained_variance_ratio_[::-1]
        var = sigmas[0]
        i = 0
        while (nouv_dim+i+1) <= p and var + sigmas[i+1] < seuil_var:
            var += sigmas[i+1]
            i += 1
        
        p -= i+1
        
        
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
            # print(k, Diff)
            if k == 0:
                print('k = 0')
                print(Diff)
            if k == (nb_iter-1):
                print('k = nb_iter-1')
                print(Diff)
            for i in range(n):
                for j in range(n):
                    d = X_ACP[j] - X_ACP[i]
                    # La vitesse change de l'accélération (somme des forces)
                    c = d * rapport(Diff[i,j])
                    V[i] += c
            
            for i in range(n):
                V[i] *= restant
                X_ACP[i] += V[i]
    return X_ACP

A = np.array([
[1,1,1],
[1,0,1],
[0,1,1],
[-1,-2,0]
])


r = reduit_dim(Gram/11,nouv_dim=3)
# Dt = np.reshape(D,(n*n,1))
# Dt = sorted(Dt)
# Dt[int(n*n/5*2)]
# Out[21]: array([ 3.65966034])
## 
# G2 = Gram[np.ix_(list(range(0,100)) + list(range(200,250)),list(range(0,100)) + list(range(200,250)))]
G2 = Gram[np.ix_(list(range(0,100)) ,list(range(0,100)))]
r2 = reduit_dim(G2/11,nouv_dim=3)


acp = ACP(G2/11, n_components = 3)
trace_ACP3D(r2,[50]*3)
trace_ACP3D(acp,[50]*3)
## 
acp = ACP(Gram/11, n_components = 3)
trace_ACP3D(r,[50]*5)
trace_ACP3D(acp,[50]*5)