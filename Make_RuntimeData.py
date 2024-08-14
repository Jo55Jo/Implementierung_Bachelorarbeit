import os
import numpy as np

def save_run_data(global_act, Branching_global, Autocorrelation, Average_Activity, Average_Alpha, Avalanche_Distribution):
    # Ordner erstellen, falls er nicht existiert
    directory = "Runtime_Data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Bestimme die höchste vorhandene Dateinummer und inkrementiere um 1
    existing_files = [f for f in os.listdir(directory) if f.startswith("Run_") and f.endswith(".txt")]
    if existing_files:
        highest_number = max([int(f.split('_')[1].split('.')[0]) for f in existing_files])
        file_number = highest_number + 1
    else:
        file_number = 1
    
    # Dateiname bestimmen
    filename = os.path.join(directory, f"Run_{file_number}.txt")
    
    # Daten in die Datei schreiben
    with open(filename, 'w') as file:
        #file.write("global_act:\n")
        #np.savetxt(file, global_act, fmt='%s', delimiter=',')
        file.write("\nBranching_global:\n")
        np.savetxt(file, Branching_global, fmt='%s', delimiter=',')
        file.write("\nAutocorrelation:\n")
        np.savetxt(file, Autocorrelation, fmt='%s', delimiter=',')
        file.write("\nAverage_Activity:\n")
        np.savetxt(file, Average_Activity, fmt='%s', delimiter=',')
        file.write("\nAverage_Alpha:\n")
        np.savetxt(file, Average_Alpha, fmt='%s', delimiter=',')
        file.write("\nAvalanche_Distribution:\n")
        np.savetxt(file, Avalanche_Distribution, fmt='%s', delimiter=',')
    
    print(f"Data saved to {filename}")