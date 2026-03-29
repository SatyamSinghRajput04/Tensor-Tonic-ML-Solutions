def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Write code here
    # U = np.array(U, dtype=float)
    # V = np.array(V, dtype=float)

    
    # pred = U[0]*V[0] + U[1]*V[1]

    
    # e = r - pred

    
    # U0 = U[0]
    # U1 = U[1]
    # V0 = V[0]
    # V1 = V[1]

  
    # U[0] = U0 + lr * (e * V0 - reg * U0)
    # U[1] = U1 + lr * (e * V1 - reg * U1)

    
    # V[0] = V0 + lr * (e * U0 - reg * V0)
    # V[1] = V1 + lr * (e * U1 - reg * V1)

    # return U , V


    
    U = np.array(U , dtype = float)
    V = np.array(V , dtype = float)

    pred = np.dot(U , V)

    e = r - pred 

    U_old = U.copy()
    V_old = V.copy()

    for i in range(len(U)):
        U[i] = U_old[i] + lr * (e * V_old[i] - reg * U_old[i])
        V[i] = V_old[i] + lr * (e * U_old[i] - reg * V_old[i])

    return U ,V     