---
Ressource:
  - "[[Homeostatic Plasticity and External Input Shape Neural Network Dynamics.pdf]]"
tags:
  - BachelorThesis
---
3 verschiedene Modell für die Netzwerktopologie.
- [[Directed Erdös Modell (ER) (Bachelorarbeit)]]
- [[Spacial Clustered Modell (SC) (Bachelorarbeit)]]
- [[Annealed Average Modell (AA) (Bachelorarbeit)]]

# Variablen und Konstanten.
## Anzahl an Neuronen (N)[^3]
$N = 10^4$ 


## Zeitkonstante ($\Delta t$)[^4]
$\Delta t = 1ms$ 


## Externer Input (h)[^5]
$h \in [0, 0.1, 0.01, 0.001, 0.0001]$ 
- Ist die unabhängige Variable die man Einstellt.

- Wahrscheinlichkeit für Spike: $1-e^{-h\Delta t}$. 
	- Wird jeden Zeitschritt neu Berechnet und ist daher ein [[Poisson Prozess]]. 

## Target Rate ($r^*$)[^6]
r* = 1Hz = ( $1 \frac{Spike}{Sekunde}$)

## State variable (s)[^2]
$s_{i,t} \in {[0,1]}$ 
- Wenn 0, dann kein Spike. (Ruhezustand)
- Wenn 1, dann Spike und direkt wieder 0. (Spikingzustand)

## Homöostatische Zeitkonstante ($\tau_{hp}$)[^1]
$\tau_{hp} = 10^3s = 1hour$ 



# Funktionen
## Homöostatischer Scaling-factor ($\alpha_{i,j}$)[^7]
$\Delta \alpha_{j,t} = (\Delta t r_{j}^* - s_{j,t})(\frac{\Delta t}{\tau_{hp}})$ (6)

#FrageBachelorarbeit Mit welchem Wert aber beginnt $\alpha$? Mit 0? oder 0.5? Das Paper gibt dazu keine Auskunft. Vielleicht sollte ich dazu ein bisschen experimentieren.

## Spike Propagation[^8]
$p_{i,j} = w_{i,j}\alpha_{j,t}$ 

# Metriken
## Globale/Populations Aktivität ($A_t$)[^11]
$A_t =  \sum_{i=1}^{N}s_{i,t}$ 

## Branching parameter (m)[^10]
Individuell zum Zeitpunkt t:
- $m_{i,t} = \sum_{j=1}^{N}w_{ij}{\alpha_{j,t}}$  

Globaler Durchschnitt zum Zeitpunkt t:
- $\overline{m} = \frac{1}{N} \sum_{i=1}^{N}{m_{i,t}}$  

## Autokorrelation Time ($\tau$)[^9]
$\tau = \frac{-\Delta t}{ln(m)}$ (5)

## Exemplary spiking activity ($a_t$)[^12]
$a_t = \frac{A_t}{N \Delta t}$ 
- In [[Grafiken (Bachelorarbeit)#Grafik 1 In vivo Vs in Vitro Dynamiken|Grafik 1]] und [[Grafiken (Bachelorarbeit)#Grafik 3 Aktivitäten eines Annealed Average (AA) Netzwerkes bei dem External input rate (h) h / Angestrebte Feuerrate (r*) r* moduliert wurde.|Grafik 3]] angegeben.
## Subsampled Avalanche-size Distribution ($P_{sub}$)[^15]

# Interpretation der Metriken
## Exponential Tails
Exponentielle Schänze kann man in den In-Vivo Populationen in [[#Grafik 1 In vivo Vs in Vitro Dynamiken|Grafik 1]] beobachten.
- (III.II) Sie indizieren eine leicht subkritikale Dynamik: [[Spike Avalanches in Vivo Suggest a Driven, Slightly Subcritical Brain State.pdf]] 
- Die Unterschiede dieser Tails wird durch subsampling verstärkt: [[Subsampling Scaling.pdf]] (Anna Levina)
	![[Pasted image 20240326115613.png]] 
## Subcritical Aktivität (m < 1)

m < 1

## Kritische Aktivierung (m = 1)
m = 1

## Superkritische Aktivierung (m > 1)
m > 1

## Error Bars
>Error bars are obtained as statistical errors from the fluctuations between independent simulations, which include random network realizations $\{w_{ij}\}$ for ER and SC. (IV)

- Wichtig für das erstellen von Grafiken. 
# Grafiken
Zu den $P_{sub}$ und $a_t$ kommen auch noch in manchen Grafiken als vergleich: 
- Power law Distribution[^13] [^14] 
- Analytische Lösungen der Avalanche-size Distribuition 
# Footnotes

[^1]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Homöostatische Zeitkonstante ($ tau_{hp}$)]]
[^2]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#State variable (s)]]
[^3]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Anzahl an Neuronen (N)]]
[^4]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Diskrete Zeitschritte $ Delta t$]]
[^5]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#External input rate (h)]]
[^6]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Angestrebte Feuerrate (r*)]]
[^7]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Homöostatische Plastizität, Implementierung]] 
[^8]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Spike Propagation.]] 
[^9]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Autokorrelation Time ($ tau$)]] 
[^10]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Branching parameter (m)]]
[^11]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Globale/Populations Aktivität ($A_t$)]]
[^12]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Exemplary spiking activity ($a_t$)]]
[^13]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Power law]]
[^14]: [[Grafiken (Bachelorarbeit)#Grafik 3 Aktivitäten eines Annealed Average (AA) Netzwerkes bei dem External input rate (h) h / Angestrebte Feuerrate (r*) r* moduliert wurde.]]
[^15]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Subsampled Avalanche-size Distribution ($P_{sub}$)]] 