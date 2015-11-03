# VenusAndMars
Solarsystem in Python | Taschner/Weinberger 5BHIT | 2015/16

Beschreibung
====
Wir wollen unser Wissen aus SEW nutzen, um eine kreative Applikation zu erstellen. Die Aufgabenstellung:

Erstelle eine einfache Animation unseres Sonnensystems!

![Angabe](http://i66.tinypic.com/156e1e1.jpg)

In einem Team (2) sind folgende Anforderungen zu erf�llen.

Ein zentraler Stern
Zumindest 2 Planeten, die sich um die eigene Achse und in elliptischen Bahnen um den Zentralstern drehen
Ein Planet hat zumindest einen Mond, der sich zus�tzlich um seinen Planeten bewegt
Kreativit�t ist gefragt: Weitere Planeten, Asteroiden, Galaxien,...
Zumindest ein Planet wird mit einer Textur belegt (Erde, Mars,... sind im Netz verf�gbar)
Events:

Mittels Maus kann die Kameraposition angepasst werden: Zumindest eine �berkopf-Sicht und parallel der Planentenbahnen
Da es sich um eine Animation handelt, kann diese auch gestoppt werden. Mittels Tasten kann die Geschwindigkeit gedrosselt und beschleunigt werden.
Mittels Mausklick kann eine Punktlichtquelle und die Textierung ein- und ausgeschaltet werden.
Schatten: Auch Monde und Planeten werfen Schatten.
W�hlt ein geeignetes 3D-Framework f�r Python (Liste unter https://wiki.python.org/moin/PythonGameLibraries) und implementiert die Applikation unter Verwendung dieses Frameworks.

Abgabe
====
Die Aufgabe wird uns die n�chsten Wochen begleiten und ist wie ein (kleines) Softwareprojekt zu realisieren, weshalb auch eine entsprechende Projektdokumentation notwendig ist. Folgende Inhalte sind in jedem Fall verpflichtend:

Projektbeschreibung (Anforderungen, Teammitglieder, Rollen, Tools, ...)
GUI-Skizzen und Bedienkonzept (Schnittstellenentw�rfe, Tastaturbelegung, Maussteuerung, ...)
Evaluierung der Frameworks (zumindest 2) inkl. Beispielcode und Ergebnis (begr�ndete Entscheidung)
Technische Dokumentation: Architektur der entwickelten Software (Klassen, Design Patterns)
Achtung: Bitte �berlegt euch eine saubere Architektur!
Den gesamten Source Code in 1 Klasse zu packen ist nicht ausreichend!
Kurze Bedienungsanleitung
Sauberes Dokument (Titelblatt, Kopf- und Fu�zeile, ...)

Hinweise zu OpenGL und glut:

Ein Objekt kann einfach mittels glutSolidSphere() erstellt werden.
Die Planten werden mittels Modelkommandos bewegt: glRotate(), glTranslate()
Die Kameraposition wird mittels gluLookAt() gesetzt
Bedenken Sie bei der Perspektive, dass entfernte Objekte kleiner - nahe entsprechende gr��er darzustellen sind.
Wichtig ist dabei auch eine m�glichst glaubhafte Darstellung. gluPerspective(), glFrustum()
F�r das Einbetten einer Textur kann die Library Pillow verwendet werden! Die Community unterst�tzt Sie bei der Verwendung.

Viel Spa� und viel Erfolg! Happy Working und Hands On!