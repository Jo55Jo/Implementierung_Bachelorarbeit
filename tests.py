import Run_Model
import numpy as np
import math
from Meters_Plots import Plots as plot
from Functions_Constants_Meters import Constants as cons
from Models import Erdos_Network as ER
from Models import Spacial_Clustered as SC
import time
import sqlite3


'''
N = 10000
# Tests
start_time = time.time()

ConList = SC.Spacial_Clustered(N)

end_time = time.time()
total_time = end_time - start_time
print("Gesamtzeit:", total_time)

[print(ConList[i]) for i in range(100)]

conn = sqlite3.connect('Compiled_Models/SS_compiled.db')
cursor = conn.cursor()
'''
global_act, Branching_ind, Branching_global, Autocorrelation, Average_Activity, Alpha = Run_Model.Run_Model("SC_10000_0", 10000, 30, 0.001)

Average_Activity_herz = [activity * cons.delta_t for activity in Average_Activity]

plot.create_barplot(Average_Activity_herz)
print("Average_Alpha:", np.average(Alpha))

#! neuestes Problem ist, einen Abruf von der SQL Datenbank zu machen. 

#! Was die dynamik angeht hängt ganz ganz viel davon ab wie Alpha initialisiert wird und wie groß die Zeitkonstante gewählt wird.
#! Wie soll ich Alpha initialisieren? Oder einfach mal lange laufen lassen udn schauen worauf es sich einpendelt?

#! Der Branching parameter ist natürlich noch müll