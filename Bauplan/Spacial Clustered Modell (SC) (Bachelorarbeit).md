---
Ressource:
  - "[[Homeostatic Plasticity and External Input Shape Neural Network Dynamics.pdf]]"
tags:
  - BachelorThesis
---
>Neural somata are randomly placed as hard disks with radius $R_s = 7.5 \mu m$  to account for the minimal distance between cell centers on a $5 \cdot 5 mm^2$ field.

Zellkörper.
- Zell Somata Zufällig platziert mit Mindestabstands-Radius: $R_s = 7.5 \mu m$ 
- Das ganze Feld ist insgesamt $5 \cdot 5 mm^2$ groß.

>From each soma, an axon grows into a random direction with a final length l given by Rayleigh distribution $p(l)=(\frac{l}{\sigma^2})e^{-\frac{l^2}{2\sigma^{2}_{l}}}$, with $\sigma_l = 900\mu m$ and average axonal length $\overline{l} \approx 1.1mm$. The axonal growth is a semi-flexible path with segments of size $\Delta l = 10 µm$ and orientations drawn from a Gaussian distribution relative to the previous segment with $µ = 15°$. 

Axon.
- Die Länge des Axon ist durch die Rayleigh distribution gegeben
	- $p(l)=(\frac{l}{\sigma^2})e^{-\frac{l^2}{2\sigma^{2}_{l}}}$        |        $\sigma_l = 900\mu m$;        $\overline{l} \approx 1.1mm$ 
		- random_values = np.random.rayleigh(0.9, size = 1.1) (Von ChatGPT)
- Der Axonwachstum ist semi-flexibel mit Segmenten $\Delta l = 10 µm$ 
- Die Orientatierung wird aus einer Gauss-Verteilung gezogen mit $µ = 15°$.

>A connection with another neuron is formed with probability $\frac{1}{2}$ if the presynaptic axon intersects with the dendritic tree of the postsynaptic neuron. The dendritic tree is modeled as a disk around the postsynaptic neuron with radius $R_d$, drawn from a Gaussian distribution with mean $R_d = 300 \mu m$ and $\sigma_d = 20 \mu m$. 

Verbindungen.
- Eine Verbindung entsteht mit $p=\frac{1}{2}$ wenn das Axon den dentritischen Baum eines Neurons durchkreuzt.
- Dentritischer Baum ist eine Disk um das Somata mit einem Radius der aus einer Gaus Verteilung mit $R_d = 300 \mu m$ and $\sigma_d = 20 \mu m$ gezogen wird.

![[Pasted image 20240327170131.png]]

# Motivation
>In order to consider more detailed topology with dominant short-range connections, we follow Orlandi et al., who developed a model based on experimental observations of in vitro cultures.
- [[Noise Focusing and the Emergence of Coherent Activity in Neuronal Cultures.pdf]] 
- [[Dominance of Metric Correlations in Two- Dimensional Neuronal Cultures Described through a Random Field Ising Model.pdf]] 

