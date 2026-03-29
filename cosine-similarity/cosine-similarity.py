import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    # pass
    a = np.array(a)
    b = np.array(b)
    dot_prod = 0

    for i in range(len(a)):
        
        dot_prod += a[i] * b[i] 
    # np.dot(a, b)
    
    # norm_a = np.linalg.norm(a)
    norm_a = np.sqrt(np.sum(a**2))
    norm_b = np.linalg.norm(b)
        
    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot_prod / (norm_a * norm_b)

     