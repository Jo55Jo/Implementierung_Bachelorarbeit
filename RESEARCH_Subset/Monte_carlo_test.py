import numpy as np

def simulate_branching_process(threshold, p=0.263, max_generations=1000):
    active_neurons = 1  # Start mit einem aktiven Neuron
    total_neurons = 1
    
    for generation in range(max_generations):
        if active_neurons == 0:
            return False  # Prozess erlischt, ohne den Schwellenwert zu erreichen
        if active_neurons >= threshold:
            return True  # Der Schwellenwert wurde erreicht
        
        # Neue aktive Neuronen für die nächste Generation
        new_active_neurons = sum(np.random.binomial(4, p) for _ in range(active_neurons))
        active_neurons = new_active_neurons
    
    return False  # Schwellenwert wurde nicht erreicht

# Anzahl der Simulationen
num_simulations = 100000
threshold = 40
success_count = sum(simulate_branching_process(threshold) for _ in range(num_simulations))

probability = success_count / num_simulations
print(f"Wahrscheinlichkeit, dass der Schwellenwert {threshold} erreicht wird: {probability:.4f}")

print("How many neurons are activated by external input: ", 10000 * (1 - np.exp(-0.0001 * 0.001)))