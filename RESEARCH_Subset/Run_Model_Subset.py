import numpy as np
import math
from Models import Annealed_Average as AA
from Models import Erdos_Network as ER
from Models import Spacial_Clustered as SC
import RESEARCH_Subset.Subset as research
from Functions_Constants_Meters import Functions as funs
from Functions_Constants_Meters import Constants as cons
from Functions_Constants_Meters import Meters as meters

import sqlite3
import pickle

# String (modell), int (size), int(iterations), float (input is one of: [0, 0.1, 0.01, 0.001, 0.0001]) -> , list (Population activity), list of np.ndarrays (individual activity), list (Branching Parameter), list (Autocorrelation Time)
# model is one of: "AA", "ER", "SC", "SC_10000_{i}"
# all meters are set to true by default. 
# Population_activity --> int; returns the global activity
# Branching_Parameters --> np.ndarray, int; returns list of individual branchingP  and int = global_mean_of_branchingP
# Autocorrelation_tiem --> int; returns int giving the autocorrelation time
# runs the whole model. Individual Parameters for models or functions have to be adjusted in the according files
def Run_Model_subset(model: str, N: int, Seconds: int, h: float):
    # initialize state_value_old, Alphaa (homostatic array)
    state_value_old = []
    # initializing Alpha. As k = 4 in the models we use 0.25 for h≠1 (h=1 we use 0 so that it doesnt take so long until its giving resonable results)
    Alpha           = np.random.normal(cons.Alpha_init, cons.SD_init, N)
    # Alpha           = np.zeros(N)
    # Calculate Iterations given by Seconds/delta_t, cast to int with math.ceil
    Iterations = math.ceil(Seconds/cons.delta_t)

    # Initialize lists for meters
    Global_act = []
    Branching_ind = []
    Branching_global = []
    Autocorrelation = []
    Average_Activity_sub = []
    Average_Activity_rest = []
    Average_Alpha = []

    #Initializing
    state_value_new = np.random.choice(N, size=cons.Init_Activity, replace=False).tolist()


    #Avalanche distribution tracker initialized as 0 and updated once activity ≠ 0
    Avalanche_Tracker = 0
    Avalanche_Distribution = []

    #Activity Tracker for measuring average activity
    Activity_Tracker_sub = 0
    Activity_Tracker_rest = 0

    #Homeostatic value trackers
    Average_Alpha_sub = [] 
    Average_Alpha_rest = []

    for i in range(Iterations):        

        # get Connection Array
        # if it is the first iteration or AA is chosen we draw the Connection_arr
        if (model != "AA") and (i == 0): 
            Connection_arr = Get_connection_array(N, model)
        else:
            Connection_arr = AA.Annealed_Average(N)


        # nacheinander Funktionen ausführen
        state_value_new = research.External_Input_Subset(N, state_value_new, h)
        state_value_new = funs.Spike_Propagation(Connection_arr, state_value_new, state_value_old, Alpha)

        #! The homeostatic scaling is updated with the actual state_value_new. is that correct?
        Alpha = funs.Update_Alpha(state_value_new, Alpha)

        # meter global and subpopulation activity
        glob_t = len(state_value_new)
        sub_t = len([x for x in state_value_new if x < cons.Subset_size])


        # this meters the sub population that gets the input and the rest population
        Activity_Tracker_sub += sub_t
        Activity_Tracker_rest += glob_t-sub_t
        
        # we calculate the average global activity for time steps of 4 Milliseconds
        if i % 4 == 0:
            #Update average Activity and average Alpha
            AA_sub = Activity_Tracker_sub / (cons.Subset_size * cons.delta_t_act)
            AA_rest = Activity_Tracker_rest / ((N-cons.Subset_size) * cons.delta_t_act)


            # Reset the activity tracker to 0
            Activity_Tracker_sub = 0
            Activity_Tracker_rest = 0

            # append every 4 Seconds to the lists for average Activity and average alpha
            Average_Activity_sub.append(AA_sub)
            Average_Activity_rest.append(AA_rest)

            # caluclate and append the 
            average_alpha_sub = np.mean(Alpha[:cons.Subset_size])
            average_alpha_rest = np.mean(Alpha[cons.Subset_size:])
            Average_Alpha_sub.append(average_alpha_sub)
            Average_Alpha_rest.append(average_alpha_rest)
            


        # Collect activity in lists for later plotting
        Global_act.append(glob_t)

        
        #Do metering of Branching parameter and autocorrelation
        if i % 100 == 0:

            branch_glob = meters.Branching_Parameters(N, Connection_arr, Alpha)
            autocorr_t = meters.Autocorrelation_Time(cons.delta_t, branch_glob)

            # add meters to collection
            Branching_global.append(branch_glob)
            Autocorrelation.append(autocorr_t)


            print("Iteration:", i)
            print("Global Activity Now: ", glob_t)
            print("Branching Parameter:", branch_glob)
            print("Autocorrelation: ", autocorr_t)
        

        # If there is zero activity but the tracker is not 0, then the avalanche is over so return to 0 and 
        if (glob_t == 0) and (Avalanche_Tracker != 0):
            Avalanche_Distribution.append(Avalanche_Tracker)
            Avalanche_Tracker = 0
        if glob_t != 0:
            Avalanche_Tracker += glob_t
        


        # state_value_new becomes the new state_value_old
        state_value_old = state_value_new
        state_value_new = []


    return Global_act, Branching_global, Autocorrelation, Average_Activity_sub, Average_Activity_rest, Average_Alpha_sub, Average_Alpha_rest, Avalanche_Distribution

# string -> array of lists
# Choice is one of ["AA", "ER", "SC", "SC_10000_{i}"] <- "SC_10000_{i}" takes an already compiled Conn_array from a database where i is the specific array. 
def Get_connection_array(N, model: str):

    if model == "ER":
        Connection_array = ER.Erdos_Network(N)
    elif model == "SC":
        Connection_array = SC.Spacial_Clustered(N)
    else:
        try:
            # Verbindung zur Datenbank herstellen
            conn = sqlite3.connect('Models/Compiled_Models/SC_compiled.db')
            cursor = conn.cursor()

            # Abrufen der Daten aus der Datenbank
            cursor.execute("SELECT array_json FROM Spacial_Clustered_10000 WHERE array_key = ?", (model,))
            pickled_array = cursor.fetchone()[0]

            if pickled_array:
                Connection_array = pickle.loads(pickled_array)
            else:
                print("Array nicht gefunden.")
        finally:
            # closing connection
            if conn:
                conn.close()

         

    return Connection_array
        