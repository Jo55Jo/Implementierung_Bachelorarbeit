import numpy as np
import matplotlib.pyplot as plt
import Spacial_Clustered as SC
import time
import math
import sys
import os
# append parent directory for importing constants
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from Functions_Constants_Meters import Constants as cons

# Funktion zum Berechnen des Abstands zwischen zwei Punkten
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

start_time = time.time()
Connection_Arr, Somata, Axons = SC.Spacial_Clustered(cons.N)

end_time = time.time()
total_time = end_time - start_time


print("Spacial Clustered Time: ", total_time)

print("Axons: ", np.mean([len(Axon) for Axon in Axons]))



# Bestimme die Längen der inneren Arrays
lengths = [len(inner_array) for inner_array in Connection_Arr]

# Berechne den Mittelwert und die Standardabweichung
mean_length = np.mean(lengths)
sd_length = np.std(lengths)

# Sortiere die Längen
sorted_lengths = sorted(lengths)

# Bestimme die 10 längsten und 10 kürzesten Längen
longest_10 = sorted_lengths[-10:]
shortest_10 = sorted_lengths[:10]

print("Mean Length of array: ", mean_length)
print("Standard deviation of array: ", sd_length)
print("Shortest 10: ", shortest_10)
print("Longest 10: ", longest_10)


# Feldgröße definieren
field_size = int(5000*math.sqrt(cons.N/10000))

# Beispiel-Koordinaten (Tupel) und Radius
radius = 20

# Erstelle ein leeres Feld
field = np.zeros((field_size, field_size))


# Zeichne Kreise an den Koordinaten ein
# Prüfen, ob Subset aktiv ist
if cons.Subset:
    for i, Soma in enumerate(Somata):
        if i < cons.Subset_size:
            # Zeichne die ersten 'Subsetsize' Somata rot
            circle = plt.Circle(Soma, radius, color='red', fill=True)
        else:
            # Zeichne die verbleibenden Somata blau
            circle = plt.Circle(Soma, radius, color='blue', fill=True)

        plt.gca().add_patch(circle)
else:
    for Soma in Somata:
        circle = plt.Circle(Soma, radius, color='lightblue', fill=True)
        plt.gca().add_patch(circle)





# Zeichne die Axon-Pfade ein
for path in Axons:
    # Entpacke die Koordinatenpaare in separate x und y Listen
    x_coords, y_coords = zip(*path)
    
    for i in range(1, len(x_coords)):
        # Berechne den Abstand zwischen den aktuellen und vorherigen Punkten
        distance = calculate_distance(x_coords[i-1], y_coords[i-1], x_coords[i], y_coords[i])

        if distance <= field_size-10:
            plt.plot([x_coords[i-1], x_coords[i]], [y_coords[i-1], y_coords[i]], color='black', linewidth=0.3)

# Setze die Feldgrenzen
plt.xlim(0, field_size)
plt.ylim(0, field_size)

# Achsen ausblenden für eine klarere Darstellung
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')

# Feld anzeigen
plt.show()


