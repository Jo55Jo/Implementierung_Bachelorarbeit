---
Ressource:
  - "[[Homeostatic Plasticity and External Input Shape Neural Network Dynamics.pdf]]"
tags:
  - BachelorThesis
---
>We consider, in addition, a network with k dynamically changing random connections (annealed average). The connections are distinguishable, exclude self-connections, and are redrawn every time step. This model approximates the otherwise numerically expensive fully connected network (ER with $p_{con} = 1$) with a global $m_t$ by choosing $α_{j,t} = \frac{m_t}{k}$. In practice, we chose $k = 4$, which produces analogous dynamics to the fully connected ($k ≈ 10^4$) network as long as $m_t < 4$. 

Struktur.
- Nicht Räumlich.

Verbindungen.
- k sich dynamisch ändernde zufällige Verbindungen
	- k = 4.

Homöostatischer Faktor.
- Homöostatischer Wert: $α_{j,t} = \frac{m_t}{k}$ 
	- Für die Implementation wird der [[Begriffe und zugehörige Formeln (Bachelorarbeit)#Branching parameter (m)|Branching Parameter]] zum Zeitpunkt t, $m_t$, gebraucht. 

Dynamik.
- Das Paper verspricht ähnliche Dynamiken zu einem voll Verbundenen Netzwerk ($k ≈ 10^4$) solange der Branching Parameter $m_t$ < 4.
- Approximiert Vollverbundenes [[Directed Erdös Modell (ER) (Bachelorarbeit)|ER]] Netzwerk mit $p_{con} = 1$. 

Ideen dazu. 
- Es ist zwar ein Dünn verbundenes Netzwerk aber irgendwie meint das Paper würde durch das neuziehen der Verbindungen in jedem Zeitschritt ein voll Verbundenes Netzwerk approximiert. 
- Komisch sind zwei Dinge: 
	- (I) Der Homöostatische Faktor ist ein ganz anderer als bei den anderen Modellen.
	- (II) Das Paper gibt gar keine Referenzen und keine Ideen dazu wie es genauer zu verstehen ist. 
		- Das zeigt aber auch das es ziemlich sicher genau so zu verstehen ist. Was mich ja nur stört ist die Inkonsistenz und die Willkürlichkeit mit der diese Werte scheinbar erstellt sind. Außerdem ist das Netzwerk ja ganz weit von jeder biologischen Plausibilität entfernt.
- Ich glaube es wird sich während der Implementation zeigen warum sich so ähnliche Dynamiken wie bei einem voll verbundenen ER zeigen. Das AA ist vielleicht so eine Art theoretisches Konstrukt an dem die Theorie nochmal überprüft werden kann. Ein bisschen so wie das Markov Model bei [[Barascud, sound, sensitivity to auditive patterns.pdf|Barascud et. al.]].