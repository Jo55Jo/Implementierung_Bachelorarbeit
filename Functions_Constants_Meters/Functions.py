import numpy as np
import Functions_Constants_Meters.Constants as cons

#----------------------------------------
# Necessary Constants
Timeconstant = cons.delta_t
Timeconstant_hp = cons.tau_hp
Target_Rate = cons.r_target
#----------------------------------------

# int, ndarray -> ndarray (updated state_values)
# Sets the State_value to active with a certain probability that depends on the external-input-rate h and the timeconstant tau
def External_Input(N: int, state_value: list, h: float, delta_t=Timeconstant):
    # probability for external spike to activate Neuron
    p = 1 - np.exp(-h * delta_t)

    # calculate Bernulli, number of trials per Bernouli experiment is 1, as only one external Input (represents summed input)
    Activations = np.random.binomial(1, p, size=N)

    # actualize the State_variable
    for i in range(N):
        if Activations[i] == 1:
            state_value.append(i)

    return state_value



# NxN Matrix, ndarray, ndarray, ndarray -> nd.array (updated Statevalues)
# Takes the Neuron matrix, the homeostatic-scaling-array, the old state-value-array, the actual state-value-array calculates the update of the state-value array
#! Because it is very unlikely that an neuron was activated by external input, we first calculate whether it is updated by previous activation and then check whether it is already active
def Spike_Propagation(Connection_arr: np.ndarray, state_value: list, state_value_old: list, Alpha: np.ndarray):
    #Für jedes Neuron
    for i in range(len(Connection_arr)):

        Spike_i = 0

        # for every connection with a neuron that was active in t_-1
        for connection in Connection_arr[i]:
            if connection in state_value_old:
                Spike_i += 1
    
        # Calculate the probability for Neuron i to be Active with homeostatic scaling factor of i and number of activated connections
        #! es gibt ein Problem, wenn Alpha > 1 dann funktioniert es nicht mehr und Alpha > 1 ist theoretisch möglich

        if np.random.binomial(Spike_i, Alpha[i]) == 1:
            #check whether the neuron is already activ
            if i not in state_value:
                state_value.append(i)


    return state_value


#ndarray, ndarray -> nd.array (update of homeostatic-scaling-values)
#takes the array of state-value and homeostatic-scaling-factor and returns the updated homeostatic-scaling-factor
def Update_Homeostatic_Scaling(state_value: list, Alpha: np.ndarray):
    # For every neuron ist homeostatic-scaling-factor is adjusted
    for i, Alpha_i in enumerate(Alpha):
        #calculate Delta_Alpha[i]
        if i in state_value:
            Alpha_updated = Alpha_i + Delta_Homeostatic_Scaling(1)
        else:
            Alpha_updated = Alpha_i + Delta_Homeostatic_Scaling(0)

        #! Alpha cannot be bigger then 1, can it? No, as it will create the probability for an activation which therefor has to be between 0/1
        if Alpha_updated > 1:
            Alpha_updated = 1

        if Alpha_updated < 0:
            Alpha_updated = 0

        #update Apha[i]
        Alpha[i] = Alpha_updated

    return Alpha



#int (0 or 1) -> float
#takes statevalue for individual neuron and returns the update value for homeostatic scaling factor
def Delta_Homeostatic_Scaling(state_value: int, r_target = Target_Rate, delta_t = Timeconstant, tau_hp = Timeconstant_hp):
    alpha = (delta_t*r_target-state_value)*(delta_t/tau_hp)
    return alpha

#! delta_alpha better name 
#! timestep better as delta_t