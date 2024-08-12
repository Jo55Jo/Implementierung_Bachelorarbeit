import numpy as np

# int, float -> np.ndarray of lists 
# Creates a N list of lists with a probability p for connection
def Erdos_Network(N: int, p = 10**(-3)):
    Connection_arr = np.empty(N, dtype=object)
    Connection_arr = [list() for _ in range(N)]
    
    # itterate through whole Matrix
    for i in range(N):
        for j in range(N):
            #do not draw self conncetions
            if i != j:
                #making a Connection with probability p
                if np.random.binomial(1, p) == 1:
                    Connection_arr[i].append(j)
                    
    #Converting from array of lists to array of arrays 
    Connection_arr = [np.array(sublist) for sublist in Connection_arr]

    return Connection_arr


