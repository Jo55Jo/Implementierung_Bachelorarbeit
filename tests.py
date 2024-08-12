import Run_Model
import numpy as np
import math

from Meters_Plots import ActivityPlot as act_plot
from Functions_Constants_Meters import Constants as cons

print("h: ", cons.h)
global_act, Branching_global, Autocorrelation, Average_Activity, Alpha, Average_Alpha, Avalanche_Distribution = Run_Model.Run_Model("AA", cons.N, cons.Seconds, h=cons.h)

print(len(Average_Activity))
global_act = [act/10 for act in global_act]
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
act_plot.create_activityplot(Average_Activity, "green")
#plot.create_activityplot(Branching_global, "Branching Parameter every 100 Milliseconds", "green")
#plot.create_activityplot(Average_Alpha, "Mean homeostatic value", "green")
#plot.create_activityplot(Autocorrelation, "Autocorrelation", "green")


from Meters_Plots import AvalanchePlot as ava_plot
ava_plot.plot_log_histogram(Avalanche_Distribution, "Avalanche Distribution - h=1")

#! Was will ich als nächstes machen? 

#! Ich möchte gerne gute Plots kreieren. Plots die optisch was hergeben. 

#! Dann über nach 1000 Iterationen laufen lassen mit enorm niedrigem homöostatischer Konstate 
#! Dann noch eine ganze Menge