import numpy as np
import math
from Functions_Constants_Meters import Constants as cons

# np.ndarray -> int
# counts how many Neurons are activ at a given time
def Global_Activity(state_value_new: list):
    A = len(state_value_new)
    return A

# int(global activity), int(momentan iteration (seconds/delta_t)), int(average_constant), float (delta_t) -> float(average_activity)
# returns the average activity for every "average_constant" iteration (every delta_t)
def Average_Activity(N: int, glob: int, iteration: int, average_constant = 4, delta_t = cons.delta_t):
    average_activity = 0
    if iteration % 4 == 0:
        average_activity = glob/N*delta_t
    return average_activity

#TODO how does this work?
def avalanche_size(glob: int):
    pass


# np.ndarray (matrix), np.ndarray (state_values) --> int (global branching parameter), np.array of ints (individual branching parameter)
# calculates the branching parameters.
#! ist eine Matrix auch ein np.ndarray?
def Branching_Parameters(N: int, Connection_arr: np.ndarray, state_value_new: list):
    # Initialize array of individual branching_parameters. It has the same size as state_value_new.
    Branching_Parameter_ind = np.zeros(N)
    
    # for every Neuron
    for i in range(N):
        # initialize the count of branching for the individual neuron
        Branching_count = 0

        # for every connected neuron
        for connection in Connection_arr[i]:
            # If there is activity in that neuron increment the individual count
            if connection in state_value_new:
                Branching_count += 1
        
        # Entry the individual Branching count into the Array Branching_Parameter_ind
        Branching_Parameter_ind[i] == Branching_count

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

