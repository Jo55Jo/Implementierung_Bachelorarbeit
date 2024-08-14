import Run_Model
import numpy as np
from Meters_Plots import ActivityPlot as act_plot
from Functions_Constants_Meters import Constants as cons
import Make_RuntimeData as rd

Global_act, Branching_global, Autocorrelation, Average_Activity, Average_Alpha, Avalanche_Distribution = Run_Model.Run_Model("AA", cons.N, cons.Seconds, h=cons.h)


print("Used Modell: AA")
act_plot.create_activityplot(Average_Activity, "green")
#plot.create_activityplot(Branching_global, "Branching Parameter every 100 Milliseconds", "green")
#plot.create_activityplot(Average_Alpha, "Mean homeostatic value", "green")
#plot.create_activityplot(Autocorrelation, "Autocorrelation", "green")

# you have to import this later because of the subconfigurations of the plots
from Meters_Plots import AvalanchePlot as ava_plot
ava_plot.plot_log_histogram(Avalanche_Distribution, f"Avalanche Distribution h = {cons.h}")


rd.save_run_data(Global_act, Branching_global, Autocorrelation, Average_Activity, Average_Alpha, Avalanche_Distribution)

print("")
print("Number of Neurons: 10000")
print("Running Time: 10 Seconds")
print("Time Step Size: ", cons.delta_t)
print("Input rate h:", cons.h)
print("Target Spiking Rate: ", cons.r_target)
print("Homeostatic Constant: ", cons.tau_hp)
#print("last branching parameter: ", Branching_global[-1])
#print("last autocorrelation time: ", Autocorrelation[-1])
#print("Average_Alpha:", np.average(Alpha))
