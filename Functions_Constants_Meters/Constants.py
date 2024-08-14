# Number of Neurons (N)
N = 10000

# Extern Input (h) Element of [0, 0.1, 0.01, 0.001, 0.0001]
h = 0.01

# Target-rate (r*) = 1 second
r_target = 1

# timestep (d_t) = 1 Millisecond
delta_t = 0.001

# timestep for Activity Tracker
delta_t_act = 0.004

# Homeostatic-scaling-constant (tau_hp) = 1 hour = 10**3 is in paper
tau_hp = 10**3

# Running Time
Seconds = 30