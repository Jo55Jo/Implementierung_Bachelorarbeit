import Run_Model
import numpy as np
import math
from Meters_Plots import Plots as plot
from Functions_Constants_Meters import Constants as cons

print("h: ", cons.h)
global_act, Branching_global, Autocorrelation, Average_Activity, Alpha, Average_Alpha, Avalanche_Distribution = Run_Model.Run_Model("AA", cons.N, Seconds=10, h=cons.h)


print("")
print("Number of Neurons: 10000")
print("Running Time: 10 Seconds")
print("Time Step Size: ", cons.delta_t)
print("Input rate h:", cons.h)
print("Target Spiking Rate: ", cons.r_target)
print("Homeostatic Constant: ", cons.tau_hp)
print("last branching parameter: ", Branching_global[-1])
print("last autocorrelation time: ", Autocorrelation[-1])
print("Average_Alpha:", np.average(Alpha))
print("Used Modell: AA")
plot.create_activityplot(global_act, "External Input h = " + str(cons.h), "green")
plot.create_activityplot(Branching_global, "Branching Parameter every 100 Milliseconds", "green")
plot.create_activityplot(Average_Alpha, "Mean homeostatic value", "green")
plot.create_activityplot(Autocorrelation, "Autocorrelation", "green")
plot.plot_log_histogram(Avalanche_Distribution, "Avalanche Distribution - h=1")

#! Was will ich als nächstes machen? 

#! Ich möchte gerne gute Plots kreieren. Plots die optisch was hergeben. 

#! Dann über nach 1000 Iterationen laufen lassen mit enorm niedrigem homöostatischer Konstate 
#! Dann noch eine ganze Menge