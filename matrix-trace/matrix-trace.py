import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A)
    N = A.shape[0]

    trace = 0
    for i in range(N):
        trace += A[i][i]

    return trace