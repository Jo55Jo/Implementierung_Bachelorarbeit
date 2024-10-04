import os
import pickle
from Functions_Constants_Meters import Constants as cons

def save_run_data(global_act, Branching_global, Autocorrelation, Average_Activity, Average_Alpha, Avalanche_Distribution):
    # Ordner erstellen, falls er nicht existiert
    directory = "Runtime_Data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Bestimme die höchste vorhandene Dateinummer und inkrementiere um 1
    existing_files = [f for f in os.listdir(directory) if f.startswith("Run_") and f.endswith(".pkl")]
    if existing_files:
        highest_number = max([int(f.split('_')[1].split('.')[0]) for f in existing_files])
        file_number = highest_number + 1
    else:
        file_number = 1
    
    # Dateiname bestimmen
    if cons.Subset == True:
        filename = os.path.join(directory, f"RunSubset_{cons.Subset_size}_{file_number}.pkl")

    elif cons.Fluctuating_h == True:
        filename = os.path.join(directory, f"RunFluctuating_{file_number}.pkl")

    else:
        filename = os.path.join(directory, f"Run_{file_number}.pkl")
    
    # Daten in ein Dictionary speichern
    data_dict = {
        "h":cons.h,
        "model":cons.model,
        "N":cons.N,
        "Targetrate":cons.r_target,
        "Homeo_con": cons.tau_hp,
        "Sec": cons.Seconds,
        "Alpha_init": cons.Alpha_init,
        "global_act": global_act,
        "Branching_global": Branching_global,
        "Autocorrelation": Autocorrelation,
        "Average_Activity": Average_Activity,
        "Average_Alpha": Average_Alpha,
        "Avalanche_Distribution": Avalanche_Distribution,
	"pcon": cons.pcon
    }
    
    # Dictionary in die Datei schreiben
    with open(filename, 'wb') as file:
        pickle.dump(data_dict, file)
    
    print(f"Data saved to {filename}")





def save_run_data_subset(global_act, Branching_global, Autocorrelation, Average_Activity_sub, Average_Activity_rest, Average_Alpha_sub, Average_Alpha_rest, Avalanche_Distribution):
    # Ordner erstellen, falls er nicht existiert
    directory = "Runtime_Data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Bestimme die höchste vorhandene Dateinummer und inkrementiere um 1
    existing_files = [f for f in os.listdir(directory) if f.endswith(".pkl")]
    
    if existing_files:
        highest_number = max([
            int(f.split('_')[-1].split('.')[0]) 
            for f in existing_files 
            if f.startswith('Run') or f.startswith('RunSubset_') or f.startswith('RunFluctuating_')
        ])
        file_number = highest_number + 1
    else:
        file_number = 1
    
    # Dateiname bestimmen
    if cons.Subset:
        filename = os.path.join(directory, f"RunSubset_{cons.Subset_size}_{file_number}.pkl")

    elif cons.Fluctuating_h:
        filename = os.path.join(directory, f"RunFluctuating_{file_number}.pkl")

    else:
        filename = os.path.join(directory, f"Run_{file_number}.pkl")
    
    # Daten in ein Dictionary speichern
    data_dict = {
        "h":cons.h,
        "model":cons.model,
        "N":cons.N,
        "Targetrate":cons.r_target,
        "Homeo_con": cons.tau_hp,
        "Sec": cons.Seconds,
        "Alpha_init": cons.Alpha_init,
        "global_act": global_act,
        "Branching_global": Branching_global,
        "Autocorrelation": Autocorrelation,
        "Average_Activity_sub": Average_Activity_sub,
        "Average_Activity_rest": Average_Activity_rest,
        "Average_Alpha_sub": Average_Alpha_sub,
        "Average_Alpha_rest": Average_Alpha_rest,
        "Avalanche_Distribution": Avalanche_Distribution
    }
    
    # Dictionary in die Datei schreiben
    with open(filename, 'wb') as file:
        pickle.dump(data_dict, file)
    
    print(f"Data saved to {filename}")
