def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Write code here
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