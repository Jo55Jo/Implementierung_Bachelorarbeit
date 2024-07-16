import numpy as np


# int, int -> np.ndarray of lists
# Takes the size of the Matrix N, and the number of connections k, and creates a NxN matrix with k random connections per neuron.
#! At the moment it allows selfconnections. No problem, is it? The paper does not mention.
def Annealed_Average(N: int, k = 4):
    # Connection-Homeostatic Matrix <- Quatratic with size N
    Connection_List = np.empty(N, dtype=object)

    # draw random conections per Neuron
    for i in range(N):
        connections = np.random.choice(N, size=k, replace=False).tolist()
        connections.sort()
        Connection_List[i] = connections
    
    return Connection_List