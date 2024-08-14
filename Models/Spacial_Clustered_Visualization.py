import numpy as np
import matplotlib.pyplot as plt
import Spacial_Clustered as SC
import time

start_time = time.time()
Connectaion_Arr, Somata, Axons = SC.Spacial_Clustered(10000)

end_time = time.time()
total_time = end_time - start_time


print("Spacial Clustered Time: ", total_time)

total_length = sum(len(inner_array) for inner_array in Connectaion_Arr)
print(total_length/10000)


# Feldgröße definieren
field_size = 5000

# Beispiel-Koordinaten (Tupel) und Radius
radius = 7.5

# Erstelle ein leeres Feld
field = np.zeros((field_size, field_size))

# Zeichne Kreise an den Koordinaten ein
for Soma in Somata:
    circle = plt.Circle(Soma, radius, color='blue', fill=True)
    plt.gca().add_patch(circle)


# Zeichne die Axon-Pfade ein
for path in Axons:
    # Entpacke die Koordinatenpaare in separate x und y Listen
    x_coords, y_coords = zip(*path)
    plt.plot(x_coords, y_coords, color='black', linewidth=0.1)

# Setze die Feldgrenzen
plt.xlim(0, field_size)
plt.ylim(0, field_size)

# Achsen ausblenden für eine klarere Darstellung
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')

# Feld anzeigen
plt.show()