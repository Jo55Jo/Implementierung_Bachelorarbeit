import numpy as np

def HierarchicalModel(level=13, p=1/4, alpha=1, M_0=2):
    #Number of Neurons
    N=2**level

    # The resulting array
    Connection_arr = [list() for _ in range(N)] 
    # Initial connections within blocks
    for n in range(0, N, M_0):
        for n1 in range(n, n + M_0):
            for n2 in range(n, n + M_0):
                if (n1 < N) and (n2 < N) and (n1 != n2):
                    Connection_arr[n1].append(n2)

    # Making connections between blocks of neurons
    for l in range(2, level + 1):
        for n in range(0, N, 2**l):
            conn = False
            for n1 in range(n, n + 2**l):
                for n2 in range(n + 2**l, n + 2**(l + 1)):
                    if n1 < N and n2 < N:
                        if np.random.random() < (alpha * (p**l)):
                            Connection_arr[n1].append(n2)
                            conn = True
                        if np.random.random() < (alpha * (p**l)):
                            Connection_arr[n2].append(n1)
                            conn = True
            # If no connection was made, force one
            if not conn:
                # Choose a random neuron from each block
                n1 = np.random.randint(n, n + 2**l)
                n2 = np.random.randint(n + 2**l, n + 2**(l + 1))
                if n1 < N and n2 < N:  # Ensure indices are within bounds
                    Connection_arr[n1].append(n2)




    # Remove duplicates
    Connection_arr = [list(set(i)) for i in Connection_arr]

    return Connection_arr

