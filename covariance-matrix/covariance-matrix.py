import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """

    X = np.array(X, dtype=float)

    
    if X.ndim != 2:
        return None

    N = X.shape[0]

    
    if N <= 1:
        return None

    
    mu = np.mean(X, axis=0)

    
    X_centered = X - mu

    
    cov = (X_centered.T @ X_centered) / (N - 1)

    return cov