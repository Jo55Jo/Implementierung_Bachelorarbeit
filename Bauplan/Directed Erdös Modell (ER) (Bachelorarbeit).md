---
Ressource:
  - "[[Homeostatic Plasticity and External Input Shape Neural Network Dynamics.pdf]]"
tags:
  - BachelorThesis
---
>Jede Verbindung zwischen 2 Neuronen in dem Netzwerk hat eine Wahrscheinlichkeit von $P_{con}$ bis auf Eigenverbindungen. 

- $w_{ij}$ mit Wahrscheinlichkeit $p_{con}$, Selbstverbindungen ausgenommen. 

>Then the degree distribution of outgoing as well as incoming connection follows a binomial distribution with average degree $\overline{k} = p_{con}(N-1) \approx p{con}N$.

- Die Durchschnittliche Verbindung ist gegeben durch: $\overline{k} = p_{con}(N-1) \approx p{con}N$ 
	- N-1 wegen keine Selbstverbindungen.

>We require $p_{con} > \frac{ln(N)}{N}$ to ensure that the graph is connected.[^1]

- $p_{con} = 10^{-3}$ = 0.001
	- Denn $\frac{ln(10000)}{10000} \approx 0.00092103403 < 0.001$ 
>The connectivity matrix $w_{ij}$ is fixed throughout each simulation, such that averaging over simulations with different network realizations results in a quenched average. 

- Die Verbindung ist mit einer Connectivity Matrix realisiert.
- Die Verbindungen sind über die ganze Simulation stabil. 
- ChatGPT: ***Quenched Average**: "Quenched" in this context means that something is fixed or frozen. In each simulation, the connectivity matrix wijwij​ remains fixed. Therefore, the behavior of the system during each simulation is influenced by this fixed connectivity pattern.*

![[Pasted image 20240327162336.png]]


# Footnotes

[^1]: [[On the Evolution of Random Graphs.pdf]]