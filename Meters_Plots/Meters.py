import numpy as np
import math
from Functions_Constants_Meters import Constants as cons



# np.ndarray -> int
# counts how many Neurons are activ at a given time
def Global_Activity(state_value_new: list):
    A = len(state_value_new)
    return A

#! Das ist irgendwie komisch gemacht. Das ergibt glaube ich wenig Sinn
# int(global activity), int(momentan iteration (seconds/delta_t)), int(average_constant), float (delta_t) -> float(average_activity)
# returns the average activity for every "average_constant" iteration (every delta_t)
average_activity = 0

def Average_Activity(N: int, glob: int, iteration: int, average_constant = 4, delta_t = cons.delta_t):
    
    if iteration % 4 == 0:
        average_activity = glob/N*delta_t
    return average_activity

        

    


# np.ndarray (matrix), list (state_values) --> int (global branching parameter), np.array of ints (individual branching parameter)
# calculates the branching parameters.
def Branching_Parameters(N: int, Connection_arr: np.ndarray, Alpha: np.array):
    # Initialize array of individual branching_parameters. It has the same size as state_value_new.
    Branching_Parameter_ind = np.zeros(N)
    
    # for every Neuron
    for i in range(N):
        # initialize the count of branching for the individual neuron
        Branching_count = 0.0

        # for every connected neuron
        for connection in Connection_arr[i]:
            # If there is activity in that neuron increment the individual count
            Branching_count += Alpha[connection]


        
        # Entry the individual Branching count into the Array Branching_Parameter_ind
        Branching_Parameter_ind[i] = Branching_count

    # calculate the global_branching_parameter
    Branching_Parameter_global = Branching_Parameter_ind.mean()
    return Branching_Parameter_global, Branching_Parameter_ind


# float (Timeconstant), float (Branching_Parameter_gloabal) --> float (Autocorrelation_time)
# calculates Autocorrelation time
def Autocorrelation_Time(del_t: float, Branch_glob: float):
    if Branch_glob == 0:
        return 0
    else:
        tau = del_t/math.log(Branch_glob)

    return tau

