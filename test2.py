from Ploting import ActivityPlot as act_plot
from Functions_Constants_Meters import Constants as cons
from Functions_Constants_Meters import Functions as funs
import Runtime_Data.Make_RuntimeData as rd
from Models import Annealed_Average as aa
import numpy as np
import random


Conection_arr = aa.Annealed_Average(10000)
Alpha         = np.random.normal(0.3, 0.01, 10000)
count = 0

Trials = 1000


zufällige_zahl = random.randint(0, 9999)
state_value = [zufällige_zahl]


for n in range(Trials):
    count = 0
    for i in range(1000):
        count  += 1
        state_value = funs.Spike_Propagation(Conection_arr, [], state_value, Alpha)
        Alpha       = funs.Update_Alpha(state_value, Alpha)

        if len(state_value) > 40:
            count += 1
            print("yay: ", count)
            break
        if not state_value:
            break
        
print("In ", Trials, " Trials, ", count, " times the avalanche went over 40")


'''

print(Alpha[-1])
for n in range(Trials):
    print(state_value)
    print(Conection_arr[state_value[0]])
    state_value = funs.Spike_Propagation(Conection_arr, [], state_value, Alpha)
    print(state_value)

    Alpha       = funs.Update_Alpha(state_value, Alpha)
    if state_value:
        count += len(state_value)
    state_value = [random.randint(0, 9999)]
    
    

        
print("In ", Trials, " Trials, ", count, " times a spike was propagated")
'''
