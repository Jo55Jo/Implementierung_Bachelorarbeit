import pickle
import os
import sys
# append parent directory for importing constants
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from Functions_Constants_Meters import Constants as cons

with open("/Users/johanneswalka/Documents/Zeug/Anderes Zeugs/Implementierung_Bachelorarbeit/Runtime_Data/RunSubset_10_2.pkl", 'rb') as file:
    data_dict = pickle.load(file)
# Beispiel für den Zugriff auf die einzelnen Listen
h = data_dict["h"]
model =  data_dict["model"]
n =  data_dict["N"]
Alpha_init = data_dict["Alpha_init"]      
Targetrate =  data_dict["Targetrate"]     
Homeo_con =  data_dict["Homeo_con"]  
Seconds = data_dict["Sec"]    
global_act = data_dict["global_act"]
branching_global = data_dict["Branching_global"]
autocorrelation = data_dict["Autocorrelation"]
Avalanche_Distribution = data_dict["Avalanche_Distribution"]
if cons.Subset == True:
        Average_Activity_sub = data_dict["Average_Activity_sub"]
        Average_Activity_rest = data_dict["Average_Activity_rest"]
        Average_Alpha_sub = data_dict["Average_Alpha_sub"]
        Average_Alpha_rest = data_dict["Average_Alpha_rest"] 


# getting the title h and the plotting color 
if h == 10:
    title_h = r'$10^1$'
    color = '#FF1493'
if h == 1:
    title_h = r'$10^0$'
    color = "green"
elif h == 0.1:
    title_h = r'$10^{-1}$'
    color = '#BFA004'
elif h == 0.01:
    title_h = r'$10^{-2}$'
    color = '#CB7600'
elif h == 0.001:
    title_h = r'$10^{-3}$'
    color = "#BF0404"
elif h == 0.0001:
    title_h = r'$10^{-4}$'
    color = "#8404D9"
elif h == 0.00001:
    title_h = r'$10^{-5}$'
    color = "blue"
else:
    title_h = r'$10^{-6}$'
    color = "brown"




if cons.Subset:
    # plot the average Activity
    from RESEARCH_Subset import ActivityPlot_Subset as act_plot_sub
    act_plot_sub.create_activityplot_subset(Average_Activity_sub, Average_Activity_rest, color, title_h)

    from RESEARCH_Subset import Homeostatic_plot as homeo_plot
    homeo_plot.plot_homeostatic_subset(Average_Alpha_sub, Average_Alpha_rest, color, title_h)
else:
    # plot the average Activity
    from Ploting import ActivityPlot as act_plot
    act_plot.create_activityplot(Average_Activity, color, title_h)

# you have to import this later because of the subconfigurations of the plots
from Ploting import AvalanchePlot as ava_plot
ava_plot.plot_log_histogram(Avalanche_Distribution, r'$\frac{h}{r^*} = $' + title_h, color)


# Print the specifics used in the model
print("")
print("Used Modell: ", model)
print("Number of Neurons: ", n)
print("Running Time: ", Seconds)
print("Input rate h:", h)
print("Target Spiking Rate: ", Targetrate)
print("Homeostatic Constant: ", Homeo_con)
print("Alpha init: ", Alpha_init)