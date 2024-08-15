import numpy as np
import matplotlib.pyplot as plt
import Spacial_Clustered as SC
import time

start_time = time.time()
Connection_Arr, Somata, Axons = SC.Spacial_Clustered(1000)

end_time = time.time()
total_time = end_time - start_time


print("Spacial Clustered Time: ", total_time)



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

print("Connection arr: ", Connection_Arr)

# Feldgröße definieren
field_size = 5000

# Beispiel-Koordinaten (Tupel) und Radius
radius = 20

# Erstelle ein leeres Feld
field = np.zeros((field_size, field_size))


# Zeichne Kreise an den Koordinaten ein
for Soma in Somata:
    circle = plt.Circle(Soma, radius, color='lightblue', fill=True)
    plt.gca().add_patch(circle)


for i, Soma in enumerate(Somata):
    plt.text(Soma[0], Soma[1], str(i), fontsize=12, color='blue', ha='center', va='center')


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


