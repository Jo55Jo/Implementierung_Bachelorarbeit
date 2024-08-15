# Number of Neurons (N)
N = 10000

# Extern Input (h) Element of [0, 0.1, 0.01, 0.001, 0.0001]
h = 0.0001

# Running Time
Seconds = 30

# model one of: "AA", "ER", "SC"
model = "AA"

# Alpha Init: to shorten the burn in phase. In case fo AA with 4 connections, a value arround 0.25 makes sense. For big h it should be lower. For h = 1 it should be 0: Float
# Sigma Init: Standard deviation for the Alpha initialization: Float
# Init Activitiy: How many neurons should be active at the start 
Alpha_init = 0.25
SD_init = 0.0
Init_Activity = 0

# Homeostatic-scaling-constant (tau_hp) = 1 hour = 10**3 is in paper
tau_hp = 10**3


# ----- rarely adjusted - not in the paper at least --------

# Target-rate (r*) = 1 second
r_target = 1

# timestep (d_t) = 1 Millisecond
delta_t = 0.001

# timestep for Activity Tracker
delta_t_act = 0.004

