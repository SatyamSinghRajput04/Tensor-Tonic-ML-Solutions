import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    # pass
    v = np.array(v)
    n = len(v)

    D = np.zeros((n,n) , dtype = v.dtype)

    for i in range(n):
        D[i][i] = v[i]
    return D
    
