from RESEARCH_fluctuatingH import Run_Model_fluctuatingH as Run_model_h
from RESEARCH_fluctuatingH import ActivityPlot_fluctuatingH as act_plot
from Functions_Constants_Meters import Constants as cons
import Runtime_Data.Make_RuntimeData as rd

# subset should be false, fluctuating true
cons.Subset = False
cons.Fluctuating_h = True

# Running the model, please set variables in Constants.py
Global_act, Branching_global, Autocorrelation, Average_Activity, Average_Alpha, Avalanche_Distribution, Fluctuating_h = Run_model_h.Run_Model_h("AA", cons.N, cons.Seconds, h=cons.h)



# getting the title h and the plotting color 
if cons.h == 10:
    title_h = r'$10^1$'
    color = '#FF1493'
if cons.h == 1:
    title_h = r'$10^0$'
    color = "green"
elif cons.h == 0.1:
    title_h = r'$10^{-1}$'
    color = '#BFA004'
elif cons.h == 0.01:
    title_h = r'$10^{-2}$'
    color = '#CB7600'
elif cons.h == 0.001:
    title_h = r'$10^{-3}$'
    color = "#BF0404"
elif cons.h == 0.0001:
    title_h = r'$10^{-4}$'
    color = "#8404D9"
elif cons.h == 0.00001:
    title_h = r'$10^{-5}$'
    color = "blue"
else:
    title_h = r'$10^{-6}$'
    color = "brown"


# plot the average Activity
act_plot.create_activityplot_h(Average_Activity, Fluctuating_h, color, title_h)

# you have to import this later because of the subconfigurations of the plots
from Ploting import AvalanchePlot as ava_plot
ava_plot.plot_log_histogram(Avalanche_Distribution, r'$\frac{h}{r^*} = $' + title_h, color)

# Save some data from the run in the Runtime_Data folder
rd.save_run_data(Global_act, Branching_global, Autocorrelation, Average_Activity, Average_Alpha, Avalanche_Distribution)

# Print some statistics at the end
print("")
print("Used Modell: ", cons.model)
print("Number of Neurons: ", cons.N)
print("Running Time: ", cons.Seconds)
print("Time Step Size: ", cons.delta_t)
print("Input rate h:", cons.h)
print("Target Spiking Rate: ", cons.r_target)
print("Homeostatic Constant: ", cons.tau_hp)
#print("last branching parameter: ", Branching_global[-1])
#print("last autocorrelation time: ", Autocorrelation[-1])
#print("Average_Alpha:", np.average(Alpha))
#plot.create_activityplot(Branching_global, "Branching Parameter every 100 Milliseconds", "green")
#plot.create_activityplot(Average_Alpha, "Mean homeostatic value", "green")
#plot.create_activityplot(Autocorrelation, "Autocorrelation", "green")