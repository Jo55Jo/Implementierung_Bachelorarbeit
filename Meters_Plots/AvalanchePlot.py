import matplotlib.pyplot as plt 
import numpy as np
from Functions_Constants_Meters import Constants as cons
import os


# Subplot-Konfigurationseinstellungen
plt.rcParams['figure.subplot.left'] = 0.185
plt.rcParams['figure.subplot.right'] = 0.785
plt.rcParams['figure.subplot.bottom'] = 0.185
plt.rcParams['figure.subplot.top'] = 0.785
plt.rcParams['figure.subplot.wspace'] = 0.2
plt.rcParams['figure.subplot.hspace'] = 0.2


def plot_log_histogram(data, title):
    """
    Plots a histogram with logarithmically distributed bins from 10^0 to 10^6 and normalizes the counts to probabilities.
    
    Parameters:
    data (array-like): The data to plot (event sizes).
    """
    # Define logarithmic bins from 10^0 to 10^6
    bin_edges = np.logspace(0, 6, num=50)
    
    # Compute the histogram
    counts, bin_edges = np.histogram(data, bins=bin_edges)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    # Calculate the probabilities
    bin_widths = bin_edges[1:] - bin_edges[:-1]
    probabilities = counts / counts.sum()
    
    # Filter non-zero bins
    non_zero = counts > 0
    bin_centers = bin_centers[non_zero]
    probabilities = probabilities[non_zero]
    
    # Plot the histogram on a log-log scale
    plt.figure(figsize=(5, 3))
    plt.scatter(bin_centers, probabilities, color='blue', label='Data')
    
    # Set log-log scale
    plt.xscale('log')
    plt.yscale('log')
    
    # Add reference line for s^-2/3
    ref_x = np.logspace(0, 6, num=100)
    ref_y = ref_x ** (-2/3)
    plt.plot(ref_x, ref_y, 'r--', label=r'Reference line $s^{-2/3}$')
    
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    # Making only the left and bottom axes visible
    plt.gca().spines['left'].set_visible(True)
    plt.gca().spines['bottom'].set_visible(True)

    # Labels and title
    plt.xlabel('Avalanche Size', fontsize=16)
    plt.ylabel('Probability', fontsize=16)
    plt.title(title, fontsize=20)
    plt.legend()

        # Saving the Plot in a plots directory
    output_dir = "plots"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Basis-Dateiname ohne Erweiterung
    base_filename = "Avalanches"
    file_extension = ".png"

    # Finde einen nicht vorhandenen Dateinamen durch Anhängen einer Zahl
    counter = 1
    output_file = os.path.join(output_dir, base_filename + file_extension)
    while os.path.exists(output_file):
        output_file = os.path.join(output_dir, f"{base_filename}_{counter}{file_extension}")
        counter += 1

    # Speichere das Plot im angegebenen Verzeichnis
    plt.savefig(output_file)

    plt.show()
