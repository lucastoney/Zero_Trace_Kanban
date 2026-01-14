Grundsätzlich einfach gehalten:

Inkrementalismus beschreibt einen Ansatz in der Entwicklung von Systemen und Organisationen,
bei dem Fortschritt in kleinen, klar abgegrenzten Schritten erfolgt. Im Gegensatz zum rein iterativen
Vorgehen, bei dem bestehende Lösungen wiederholt verbessert werden, besteht das Ziel des
inkrementellen Arbeitens darin, ein System **Stück für Stück aufzubauen** und idealerweise jede
dieser kleinen Erweiterungen früh nutzbar bereitzustellen. Die Grundlage dafür ist stets ein modular
aufgebautes System, dessen Einzelkomponenten unabhängig voneinander weiterentwickelt und
ersetzt werden können.


Inkrementelles Arbeiten setzt voraus, dass Änderungen gefahrlos durchgeführt werden können.
Daher gibt es zwei effektive Strategien: **1. Technische Entkopplung** Mittels Ports-&-Adapters
(Hexagonale Architektur) werden Schnittstellen so gestaltet, dass sich intern viel ändern kann,
ohne dass äußere Komponenten betroffen sind. **2. Schnelles Feedback durch Continuous
Integration** Je schneller ein Fehler entdeckt wird, desto geringer ist der Schaden. Wird ein Fehler
erst Monate später sichtbar, kann er katastrophale Folgen haben. Wird er innerhalb weniger
Minuten erkannt, ist die Behebung trivial. Die Kombination beider Strategien schafft robuste
Systeme, die auch unter hoher Entwicklungsgeschwindigkeit stabil bleiben.


### Was heits das für uns. 

Trotz nahezu "Zero" Erfahrung in der Softwareentwicklung haben wir diesen Ansatz bestmöglich verfolgt. 
Wir haben versucht den Code in Module aufzutrennen und entsprehcend zu schreiben, auch die Abtrennung von GUI und "backend"
war eine Entscheidung die sich auf dieses Thema stütze!

Unser Code sollte recht einfach sein nach dem Ports und Adapers Modell zu testen sein (wenn man automatisierte tests schreiben kann!!!!!)
Die einsteiger Komplexität wird selbst von Vernon als klarer Nachteil dargestellt. 
Nichts desto trotz, wird dadurch eine hohw Testbarkeit durch entkopplung garantiert! 


**AChtung, wenn hier Vernon und Ports und Adapters erwähnt wird im BEricht, muss der Code nach 
Application Core und Aussenweld eindeutig untersucht und dokumentiert werden!!!!!** 
