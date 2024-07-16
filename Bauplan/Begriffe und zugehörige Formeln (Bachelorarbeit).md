---
Ressource:
  - "[[Homeostatic Plasticity and External Input Shape Neural Network Dynamics.pdf]]"
---
#BachelorThesis 
# Power law
$P(s) \approx s^{-\frac{3}{2}}$ 

- (III.I) (Power law *expected für kritischen Branching Process*: [[The Theory of Branching Processes (Springer, Berlin, 1963.pdf]] <- Leider ganzes Buch) - (Erwartet für Synchrone-irreguläre Zustände: [[Power-Law Statistics and Universal Scaling in the Absence of Criticality.pdf]])
# External input rate (h) 
- Es wird von einem uniformen Input ausgegangen: $h_i = h$ 
- h wird in jedem Durchgang neu eingestellt, denn das ist ja was untersucht werden soll.
	- $\frac{h}{r^*} = 10^{[0,-1,-2,-3,-4]}$ (V)
	- Mit $r^* = 1Hz = ( 1 \frac{Spike}{Sekunde}) = 1$ folgt: 
		- $h \in [0, 0.1, 0.01, 0.001, 0.0001]$
- Ergebnisse sind Bursting für -4, -3.
- Kritisch/fluctuating für -2,-1.
- Irregulär für 0.

>Wahrscheinlichkeit für Spike durch Externen Input ergibt sich aus einem Poisson Prozess mit Wahrscheinlichkeit $1-e^{-h\Delta t}$. 

- Die Wahrscheinlichkeit für einen Spike der durch externen Input ausgelöst wird ist durch $1-e^{-h\Delta t}$ gegeben.
	- Es ist also sehr einfach zu implementieren. Einfach nur ein Wert. 

- #FrageBachelorarbeit Was soll das jetzt heißen. Ist das jetzt die Wahrscheinlichkeit dafür das der Prozess stattfindet oder ist die Wahrscheinlichkeit für den Spike selbst? 
	- *Ich glaube die Antwort ist, das es schon die Wahrscheinlichkeit selbst ist. Wenn man sich die Definition eines [[Poisson Prozess]] auf Wikipedia anschaut dann sieht man das es alle 3 Eigenschaften Erfüllt.* 




# Angestrebte Feuerrate (r*) 
>In order to further reduce complexity, we assume a uniform target rate $r_j^* = r^*$, while in fact experiments show a broad log-normal spike rate distribution.
- #IdeeBachelorarbeit Sie haben diese log-normal distribution der target-rate auch "preliminary" untersucht, und konsistente results gefunden ($p_{con} = 0.1$ *also mit dem ER*). Dasselbe könnte man auch nochmal machen.
	- [[The Log-Dynamic Brain, How Skewed Distributions Affect Network Operations.pdf]] 
	- [[Neuronal Firing Rate Homeostasis Is Inhibited by Sleep and Promoted by Wake.pdf]] 
- r* = 1Hz = ( $1 \frac{Spike}{Sekunde}$)


# State variable (s)
>Zustand des Neurons.

$s_{i,t} \in {[0,1]}$ 
- Wenn 0, dann kein Spike. (Ruhezustand)
- Wenn 1, dann Spike und direkt wieder 0. (Spikingzustand)

## Spike Propagation.
>Stochastischer Prozess in diskreten Zeitschritten.[^1] Dabei wird die State variable (s) entweder auf 1 (spiking) oder 0 (ruhe) gesetzt. Die Wahrscheinlichkeit mit der das Neuron dann feuert folgt der homöostatischen Verteilung. 

Probability: $p_{i,j} = w_{i,j}\alpha_{j,t}$ 
- $w_{i,j} \in [0, 1]$
	- 0 für nicht verbunden.
	- 1 für verbunden.
- $\alpha_{j,t}$ ist der [[Begriffe und zugehörige Formeln (Bachelorarbeit)#**Homöostatische Plastizität (Formel 6, IV)**|homöostatische Skalierungsfaktor]]. 

Wenn ich es richtig verstehe dann kann ein Neuron nur entweder aktiviert werden oder nicht aktiviert werden ([[#State variable (s)|s]]) Ob ein Neuron aktiviert wird oder nicht hängt aber von ganz vielen Unabhängigen $p_{i,j}$ sowie [[#External input rate (h)|dem externen Input h]] ab. 
- Werden diese Wahrscheinlichkeiten summiert und dann ein spike mit dieser Wahrscheinlichkeit ausgelöst? Dann könnte die Wahrscheinlichkeit ja über 1 gehen. 
	- Das würde bedeuten ein paar Kugeln in einem Glas für jedes presynaptische Neuron einzufärben und dann am Ende aus dem glas eine Kugel zu ziehen das für aktivität oder nicht aktivität steht.
- Oder wird für jeden einzelnen Schritt eine Kugel aus einem Glas gezogen mit eben der Gegebenen Wahrscheinlichkeit und sobald ich eine Kugel ziehe die "spike" sagt brauche ich nicht mehr weiter zu berechnen....
- Macht das überhaupt einen Unterschied? 
	- Ja! Bei dem einen werden die Wahrscheinlichkeiten Addiert. Das wäre wie wenn man sagen würde, es sei 100% warhscheinlich Kopf zu werfen wenn ich zwei mal eine Münze werfe. Es ist aber $\frac{3}{4}$ wahrscheinlich. 
- Eine dritte Option wäre die Spikes zu summieren. Also alle Einzelprozesse aufzuaddieren und dann das Neuron mehrere Spikes abgeben lassen. $\Delta t$ ist aber so gewählt und die State Variable s so definiert das pro Zeitschritt genau 0 oder 1 Spike ausgelöst werden können. 

#FrageBachelorarbeit Ein Problem das allerdings auftritt ist dann beim berechnen des [[#**Individueller branching Parameter (Formel 1, III) **|indivduellen Branching Parameters]]. Das ist ja im Prinzip die Summe der Wahrscheinlichkeiten das presynaptisches Neuron ein postsynaptisches aktiviert. Aber was hier nicht mit einberechnet wird ist der Umstand dass das Spike manchmal überhaupt nichts Wert ist weil das Neuron bereits durch einen anderes Neuron oder durch externen Input (h) aktiviert wurde. 
Kann das vernachlässigt werden weil die Wahrscheinlichkeit dafür das zwei Prozesse ein postsynaptisches Neuron aktivieren so gering ist?

# Autokorrelation Time ($\tau$) 
>Die Autokorrelationszeit gibt an wie lange es braucht bis das System sich von dem vorherigen Zustand unterscheidet. Deshalb ist sie auch größer wenn $m \to 1$. Sobald $m \to 0$ oder $m \to \inf$ wird die Zeit die das System dafür braucht sich von seinem vorherigen zustand zu unterscheiden immer geringer. 

> Man erhält $\tau$  indem man mit der [[#Autocorrelation Formel|Autocorrelation Formel]] vergleicht und mit einem exponentiellen Decay $C(l) = e^{-\frac{l\Delta t}{\tau}}$ ([[Inferring collective dynamical states from widely unobserved systems.pdf]]) 

$\tau = \frac{-\Delta t}{ln(m)}$ (5)
- $\tau$ ist hierbei die Autokorrelationszeit. 
- Divergiert für $m \to 1$.[^3] 
- Ist Positiv für m < 1 und negativ für m > 1. (weil es im Paper für Subkritikale Regime gegeben wird. Würde es für Superkritikale Systeme gegeben wäre es wahrscheinlich ohne das -)

# Anzahl an Neuronen (N)
$N = 10^4$ 
Jede Node = *exitatorisches Neuron*

>For the computational model, we consider a network of n equals $10^4$ neurons, which represent the size of in vitro cultures and in vivo cortical hypercolumns. 
- Das ist natürlich nur eine ungenaue Repräsentation ohne Anspruch auf genaue Abbildung von Cortical Collumns zu machen die Wahrscheinlich in ihrer Größe auch noch stark variieren.
# Autocorrelation Formel
- $C(l) = m^l$ 
	- m = [[#Branching parameter (m)]]
	- l = Verzögerung der Zeiteinheit.

# Branching parameter (m)
- [[The Theory of Branching Processes (Springer, Berlin, 1963.pdf]]
## m ergibt sich aus der Erwartungswert von $A_{t+1} | A_t$ 
$E(A_{t+1}|A_t) = mA_t$ 
- *Das heißt, m ist der Parameter den man an die globale Aktivität in $t_0$ rann multiplizieren muss um  $A_{t+1}$ zu erhalten.*
## **Individueller branching Parameter (Formel 1, III):**
>This local branching parameter, $m_{i,t}$, thus quantifies the impact of a spike in neuron i on the network.
- $m_{i,t} = \sum_{j=1}^{N}w_{ij}{\alpha_{j,t}}$  



## **Time-dependent network branching parameter (Formel 2, III)**
- $\overline{m} = \sum_{i=1}^{N}{m_{i,t}}$  

# Globale/Populations Aktivität ($A_t$)
## $A_t$ (Formel)
>$A_t$ ergibt sich aus der Summe der Individuellen Zustände ([[#State variable (s)|s]]) 

$A_t = \sum_{i=1}^{N}s_{i,t}$ 

# Erwartete Aktivität zum Zeitpunkt t+1. 
Erwartete Aktivität: $E(A_{t+1}|A_{t}) = m A_t + N h \Delta t$ 

# Subcritical Aktivität (m < 1)
> Ein Zustand ist Subcritical wenn m < 1. Die gesamte Aktivität konvergiert gegen $N h \Delta t$ wenn m gegen 0 geht. 

- $\langle A \rangle = \frac{1}{T}\sum_{t=1}^{T}{A_{t} \xrightarrow[{T \to \inf}]{}  \frac{N h \Delta t}{1-m}}$ 
	- $\langle \cdot \rangle$ steht für *temporal average*. 
- #FrageBachelorarbeit Wenn m aber ungefähr 1 ist sollte das Netzwerk ja eigentlich stabil sein. Stattdessen geht es dafür aber gegen Unendlich... Das heißt es sollte eine Verzerrung der Formel geben die umso größer ist umso weiter m von 0 entfernt ist.  ^ebe910

## Subkritikales Verhalten und Autokorrelationszeit. 

## Mean spike rate im subcriticalen Regime (r)
Wenn man $\langle A \rangle$ durch $N\Delta t$ teilt erhält man eine Konstante. Die Mean spike rate r. Allerdings gilt dies nur im subcritical Regime und selbst da nicht wirklich weil [[#^ebe910|die Formel ungenau ist]] umso mehr m gegen 1 geht. 

$\frac{\langle A \rangle}{N\Delta t} \to r = \frac{h}{1-m}$ 

- Das Paper meint dies sei eine Biologische Restriktion (III) die man durch das Einstellen von h oder m Einstellen kann, wobei $m \in [0,1\}$ und $h \in [0, \inf\}$. Die Formel passt also nicht weil m nicht 1 werden darf aber in Wirklichkeit 1 werden kann.  

## Autokorrelationsfunktion des Subcriticalen Regime 
>Der subkritikale branching process (m < 1) ist stationary (statistische Variablen ändern sich nicht) mit der Autokorrelationsfunktion 

$C(l) = m^l$ 
- Ich glaube $l \in$ Natürliche Zahlen und steht dafür wie schnell sich das System verändert.  

# Kritische Aktivierung
>Branching Parameter (m) ist 1. Das Netzwerk wächst linear mit Rate [[#External input rate (h)|h]]. Dieses Wachstum ergibt sich daraus das h ja immer noch zusätzlich zu m auf die Netzwerkaktivität Einfluss nimmt. In dieser Grafik[^3] sieht man das m = 1 ein Wert ist der nicht von der Autokorrelationszeit abgebildet wird denn es würde unendlich lange brauchen bis das System sich von seinem Jetzigen Zeitpunkt unterscheidet. 

# Superkritische Aktivierung
>Für m > 1 ist die Aktivität Superkritisch. Die Netzwerk Aktivität $A_t$ kann ins Unendliche wachsen. 

>For a finite network, this, of course, is not possible and will manifest in a peak of avalanche size distribution at large avalanche sizes. (IV.I)

- Das bedeutet das die [[Grafiken (Bachelorarbeit)#Grafik 1 In vivo Vs in Vitro Dynamiken|größten der Lawinen]] durch einen solchen Superkritikalen Zustand ausgelöst werden. 



# Homöostatische Plastizität ($\Delta \alpha_{j,t}$) 
>This can be implemented biologically as autonomous synaptic processes or somatic processes such as translation and transcription.

>We consider a linear negative feedback with time constant $\tau_{hp}$, which depends solely on the local activity of the postsynaptic neuron $s_{j,t}$. That's why adapting a neuron's synaptic strength does not rely on information about the population activity $A_t$.

- $\Delta \alpha_{j,t} = (\Delta t r_{j}^* - s_{j,t})(\frac{\Delta t}{\tau_{hp}})$ (6)

	- Es hängt nur von $s_{j,t}$ ab weil alle anderen Faktoren, $r_j^*, \Delta t, \tau_{hp}$ fest sind. 
	- $\alpha_{j,t} ≥ 0$, weil Wahrscheinlichkeit.



# Homöostatische Zeitkonstante ($\tau_{hp}$)
>Die Zeitkonstante gibt an wie schnell das System bei einem Abweichen von dem Target-Wert r* wieder zu diesem zurück findet. In unserem Fall wird ein $\tau_{hp} = 10^3s = 1hour$ gewählt.  

- $\tau_{hp} = 10^3s = 1hour$
	- Umso größer die Zeitkonstante, umso langsamer die Anpassung an die Target rate r*. Man kann so also einstellen wie schnell das Neuron adaptiert. 
		- #IdeeBachelorarbeit Man könnte mehrere Homöostatische Mechanismen haben die auf unterschiedlichen Zeitstufen arbeiten, so wie es im biologischen Gehirn der Fall ist. 

# Exemplary spiking activity ($a_t$)
>In order to present the spiking activity over time, we partition the time axis of experimental or numerical data into discrete bins of size $\Delta t$. For the time discrete simulations, the time bin naturally matches the time step. For experimental data, we set $\Delta t = 4 ms$. In each time bin, we count the total number of spikes $A_t$ and normalize with the number of neurons $N$ to obtain the average spiking activity $a_t = \frac{A_t}{N \Delta t}$. Note that experimental preparations were inevitably subsampled as spikes were recorded only from a small number of all neurons. (Appendix B)

- $a_t = \frac{A_t}{N \Delta t}$
	- Es ist ein Wert der ungefähr den Durchschnittlichen Spike eines Neurons pro $\Delta t$ angibt.  
# Subsampled Avalanche-size Distribution ($P_{sub}$)
>We define the avalanche size $s$ as the number of spikes enclosed along the discrete time axis by bins with zero activity. ([[Neuronal Avalanches in Neocortical Circuits.pdf]]) To test for criticality in terms of a branching process, one compares $P(s)$ to the expected $P(s) \approx s^{-\frac{3}{2}}$. This is a valid approach in the limit $h \to  0$, where avalanches can be clearly identified and for fully sampled systems. However, experiments are limited to record only from n out of N neurons. As a result, the distributions for subsampled activity $P_{sub}$ differ due to subsampling bias. Therefore, we numerically measure both full (n = N) and subsampled (n < N) avalanche size distribution to qualitatively compare $P(s)$ to the theory and $P_{sub}(s)$ to experimental data.

- Eine Lawine ist definiert als eine Phase der Aktivität die von Boxen mit 0-Aktivität umgeben sind.
	- #FrageBachelorarbeit Gibt es wirklich Zeitpunkte zu denen die Aktivität vollkommen 0 ist?
		- Ansonsten müsste man einen kritischen Wert bestimmen der als 0 Aktivität gilt. 

- $P_{sub}(s)$ ist ein runter gesampelte Avalanche weil man nicht alle Neurone messen kann (zu rechenaufwendig wahrscheinlich)
- $(n = 100, triangles)$ ist die Art und Weise wie runter gesampelt wird. 
	- #FrageBachelorarbeit Laut ChatGPT bedeutet das $(n = 100, triangles)$ das immer nur die ersten 100 Spikes betrachtet werden einer Lawine um diese zu berechnen. Ich bin mir nicht sicher ob das stimmt. 
		- Es hat auch einmal vorgeschlagen das triangles bedeutet wie viele sich gegenseitig stimulierende Cluster von 3 Neuronen vorkommen (würde aber denke ich weniger Sinn ergeben).

- Erwartet wird: $P(s) \approx s^{-\frac{3}{2}}$ (Powerlaw)

- 

#FrageBachelorarbeit 


# Spike Propagation.
>Stochastischer Prozess in diskreten Zeitschritten.[^1] Dabei wird die State variable (s) entweder auf 1 (spiking) oder 0 (ruhe) gesetzt. Die Wahrscheinlichkeit mit der das Neuron dann feuert folgt der homöostatischen Verteilung. 

Probability: $p_{i,j} = w_{i,j}\alpha_{j,t}$ 
- $w_{i,j} \in [0, 1]$
	- 0 für nicht verbunden.
	- 1 für verbunden.
- $\alpha_{j,t}$ ist der [[Begriffe und zugehörige Formeln (Bachelorarbeit)#**Homöostatische Plastizität (Formel 6, IV)**|homöostatische Skalierungsfaktor]]. 
# Exponential Tails
Exponentielle Schänze kann man in den In-Vivo Populationen in [[#Grafik 1 In vivo Vs in Vitro Dynamiken|Grafik 1]] beobachten.
- (III.II) Sie indizieren eine leicht subkritikale Dynamik: [[Spike Avalanches in Vivo Suggest a Driven, Slightly Subcritical Brain State.pdf]] 
- Die Unterschiede dieser Tails wird durch subsampling verstärkt: [[Subsampling Scaling.pdf]] (Anna Levina)
	![[Pasted image 20240326115613.png]]
# Diskrete Zeitschritte $\Delta t$ 
>Das ganze System läuft in diskreten Zeitschritten $\Delta t$ 

Man kann es auch als das kleinste Betrachtete Zeitintervall des Systems verstehen.

### **(welchen Wert könnte delta t zum Beispiel annehmen?)**

ChatGPT: *Das ΔtΔt in einem Poisson-Prozess kann jeden Wert größer als Null annehmen, jedoch wird es oft als sehr kleiner Wert angenommen, insbesondere wenn man den Übergang zu einem kontinuierlichen Zeitmodell betrachtet. In der Praxis hängt die Wahl von ΔtΔt von der spezifischen Anwendung des Poisson-Prozesses ab und davon, wie genau Sie die Ereignisse innerhalb des Prozesses betrachten möchten.*

*Hier sind einige Beispiele:*

- *In vielen Anwendungen der Warteschlangentheorie könnte ΔtΔt in Sekunden oder sogar Bruchteilen einer Sekunde gemessen werden, je nachdem, wie genau Sie den Fluss von Kunden oder Aufträgen analysieren möchten.*
    
- *In der Physik oder der Biologie könnte ΔtΔt Bruchteile einer Sekunde oder sogar Millisekunden betragen, um die Reaktionsraten oder das Auftreten von bestimmten Ereignissen im Detail zu untersuchen.*
    
- *In der Finanzmathematik könnte ΔtΔt als ein Tag (24 Stunden) oder sogar als ein Bruchteil eines Tages betrachtet werden, je nachdem, ob Sie den Handel oder die Preisbewegungen von Finanzinstrumenten modellieren möchten.*
    

*Die Wahl von ΔtΔt hängt also stark von den spezifischen Anforderungen Ihrer Analyse ab und davon, wie genau Sie die Ereignisse innerhalb des Poisson-Prozesses betrachten möchten.*

## Spike Propagation.
>Stochastischer Prozess in diskreten Zeitschritten.[^1] Dabei wird die State variable (s) entweder auf 1 (spiking) oder 0 (ruhe) gesetzt. Die Wahrscheinlichkeit mit der das Neuron dann feuert folgt der homöostatischen Verteilung. 

Probability: $p_{i,j} = w_{i,j}\alpha_{j,t}$ 
- $w_{i,j} \in [0, 1]$
	- 0 für nicht verbunden.
	- 1 für verbunden.
- $\alpha_{j,t}$ ist der [[Begriffe und zugehörige Formeln (Bachelorarbeit)#**Homöostatische Plastizität (Formel 6, IV)**|homöostatische Skalierungsfaktor]]. 

# Poisson Prozess, Modell der externen Aktivierung ($h \Delta t$), ($N h \Delta t$)
>[[Poisson Prozess]] <- bringt nicht so viel. Der Poisson Prozess ist eine Art und Weise die Wahrscheinlichkeit für das Auftreten eines Ereignisses in einem bestimmten Zeitschritt ($\Delta t$ in unserem Fall) zu berechnen. Es hängt dabei  von der Rate ([[#External input rate (h)|h]]) ab, also der Menge an erwarteten Ereignissen in dem Zeitintervall.

$P(h, t) = 1-e^{-h\Delta t}$[^2]
- P(h,t) das Ergebnis ist eine Wahrscheinlichkeit dafür das ein Spike auftritt oder nicht. 
- $P(h,t) \to 1$ für $h \to \inf$.
- $P(h,t) \to 0$ für $h \to 0$ 
- $P(h,t) \approx h \Delta t$ 
	- sagt das Paper aber das ist schein ein ziemlich ungenaues ungefähr wie mir scheint. 
	- $h \Delta t$ $:\approx$ die Wahrscheinlichkeit dafür das ein externer Input einen Spike in einem individuellen Neuron auslöst. 
	- $N h \Delta t$ ist die Gesamtmenge an Spikes die Ausgelöst wird (aber auch nur eine Summation von Wahrscheinlichkeiten. Ein Wert von 4,37 würde zum Beispiel sagen das es wahrscheinlich ist das 4,37 Spikes ausgelöst werden. Der Grund dafür das hier die Wahrscheinlichkeiten Summiert werden können ist, das es sich um unabhängige Ziehungen handelt, mehrere Gewinne also möglich sind).




# Footnotes
[^1]: [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Diskrete Zeitschritte $ Delta t$]] 
[^2]: ![[Pasted image 20240327093909.png]] Umso größer $h \Delta t$ umso näher bei 1 die Wahrscheinlichkeit.
[^3]: ![[Pasted image 20240327143603.png]]
