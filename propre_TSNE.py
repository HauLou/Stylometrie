##

import numpy as np
from fonctions_ACP import *

##

def reduit_dim(X, Distances, nouv_dim = 2):
    n,p = np.shape(X)
    if p > nouv_dim:
        X_ACP = ACP(X,n_components=p)
        nouv_Distances = X_ACP.dot(X_ACP.t)
        return (Distances-nouv_Distances)