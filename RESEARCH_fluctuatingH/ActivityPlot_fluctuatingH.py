import matplotlib.pyplot as plt 
import numpy as np
from Functions_Constants_Meters import Constants as cons
import os

# Subplot-Konfigurationseinstellungen
plt.rcParams['figure.subplot.left'] = 0.265
plt.rcParams['figure.subplot.right'] = 0.623
plt.rcParams['figure.subplot.bottom'] = 0.27
plt.rcParams['figure.subplot.top'] = 0.64
plt.rcParams['figure.subplot.wspace'] = 0.2
plt.rcParams['figure.subplot.hspace'] = 0.2

import matplotlib.pyplot as plt
import os

def create_activityplot_h(activity_list: list, fluctuating_h: list, color_plot: str, h_string: str):
    # Erstellen der Figur und Zugriff auf ihre Größe
    fig, ax1 = plt.subplots(figsize=(6, 3), dpi=200)
    fig_width, fig_height = fig.get_size_inches()

    # Dynamisch berechnete Schriftgrößen basierend auf der Plotgröße
    title_fontsize = fig_height * 7  # Beispiel: 13.3 mal die Höhe der Figur
    label_fontsize = fig_height * 5   # Beispiel: 8.3 mal die Höhe der Figur
    tick_fontsize_y = fig_height * 5.0    # Beispiel: 5.0 mal die Höhe der Figur
    tick_fontsize_x = fig_height * 3.0    # Beispiel: 5.0 mal die Höhe der Figur

    # X-Achse: Zeit in diskreten Zeitschritten (Sekunden / delta_t)
    x = range(len(activity_list))
    # Normalize with N/4 because delta_t is 4 for average activity in the paper
    normalize =  cons.N/4 

    # Y-Achse: Aktivitätswerte
    y = activity_list

    # Plot the primary activity data
    ax1.plot(x, y, color=color_plot, linewidth=1)

    # Nur die linke und untere Achse sichtbar machen
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(True)
    ax1.spines['bottom'].set_visible(True)

    # X-Achse festlegen
    ax1.set_xlabel('Seconds', fontsize=label_fontsize, fontweight=500)

    # Y-Achse für Aktivitätswerte
    ax1.set_ylabel(r'$a_t$ (Hz)', fontsize=label_fontsize, fontweight=500, labelpad=20, rotation=0)  
    ax1.yaxis.set_label_position("left")
    ax1.yaxis.set_label_coords(0.05, 1.0)  # Position der Y-Achsenbeschriftung anpassen
    ax1.set_ylim(0, 40)  # Setze das Maximum der Y-Achse auf 40

    # Y-Achse nur bei 0 und 20 beschriften
    ax1.set_yticks([0, 20])
    ax1.tick_params(axis='y', labelsize=tick_fontsize_y)

    # Set custom x-ticks to display only integer labels
    x_tick_positions = [i for i in range(len(x)+1) if i / normalize % 10 == 0]  # Plotte nur X-Werte, die ganze Zahlen sind
    x_tick_labels = [int(pos / normalize) for pos in x_tick_positions]
    ax1.set_xticks(ticks=x_tick_positions)
    ax1.set_xticklabels(x_tick_labels, fontsize=tick_fontsize_x)

    # Secondary y-axis for fluctuating_h data
    ax2 = ax1.twinx()
    ax2.plot(x, fluctuating_h, color='blue', linewidth=1)  # Plot the fluctuating_h data

    ax2.set_ylabel(r'$h$', fontsize=label_fontsize, fontweight=500, labelpad=20, rotation=0)
    ax2.yaxis.set_label_position("right")
    ax2.yaxis.set_label_coords(0.95, 1.0)  # Position der Y-Achsenbeschriftung anpassen

    # remove top achses
    ax2.spines['top'].set_visible(False)

    # Fixing y-axis range for fluctuating_h and setting log scale
    ax2.set_ylim(0.0001, 0.1)
    ax2.set_yscale('linear')
    ax2.set_yticks([0.0001, 0.05, 0.1])
    ax2.get_yaxis().set_major_formatter(plt.ScalarFormatter())
    ax2.tick_params(axis='y', labelsize=tick_fontsize_y)



    # Titel hinzufügen
    if not cons.log_r:
        plt.title(r'$\frac{h}{r^*} = $' + h_string, color=color_plot, fontsize=title_fontsize, pad=40, fontweight='bold')
    else:
        plt.title(r'$\frac{h}{r^*} = $' + h_string + " log_r", color=color_plot, fontsize=title_fontsize, pad=40)

    # Saving the Plot in a plots directory
    output_dir = "Ploting/plots"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Basis-Dateiname ohne Erweiterung
    base_filename = "Activity"
    file_extension = ".png"

    # Finde einen nicht vorhandenen Dateinamen durch Anhängen einer Zahl
    counter = 1
    output_file = os.path.join(output_dir, base_filename + file_extension)
    while os.path.exists(output_file):
        output_file = os.path.join(output_dir, f"{base_filename}_{counter}{file_extension}")
        counter += 1

    # Speichere das Plot im angegebenen Verzeichnis
    plt.savefig(output_file)

    # Diagramm anzeigen
    plt.show()
