# VenusAndMars
Solarsystem in Python | Taschner/Weinberger 5BHIT | 2015/16

Beschreibung
====
Wir wollen unser Wissen aus SEW nutzen, um eine kreative Applikation zu erstellen. Die Aufgabenstellung:

Erstelle eine einfache Animation unseres Sonnensystems!

![Angabe](http://i66.tinypic.com/156e1e1.jpg)

In einem Team (2) sind folgende Anforderungen zu erfüllen.

Ein zentraler Stern
Zumindest 2 Planeten, die sich um die eigene Achse und in elliptischen Bahnen um den Zentralstern drehen
Ein Planet hat zumindest einen Mond, der sich zusätzlich um seinen Planeten bewegt
Kreativität ist gefragt: Weitere Planeten, Asteroiden, Galaxien,...
Zumindest ein Planet wird mit einer Textur belegt (Erde, Mars,... sind im Netz verfügbar)
Events:

Mittels Maus kann die Kameraposition angepasst werden: Zumindest eine Überkopf-Sicht und parallel der Planentenbahnen
Da es sich um eine Animation handelt, kann diese auch gestoppt werden. Mittels Tasten kann die Geschwindigkeit gedrosselt und beschleunigt werden.
Mittels Mausklick kann eine Punktlichtquelle und die Textierung ein- und ausgeschaltet werden.
Schatten: Auch Monde und Planeten werfen Schatten.
Wählt ein geeignetes 3D-Framework für Python (Liste unter https://wiki.python.org/moin/PythonGameLibraries) und implementiert die Applikation unter Verwendung dieses Frameworks.

Abgabe
====
Die Aufgabe wird uns die nächsten Wochen begleiten und ist wie ein (kleines) Softwareprojekt zu realisieren, weshalb auch eine entsprechende Projektdokumentation notwendig ist. Folgende Inhalte sind in jedem Fall verpflichtend:

Projektbeschreibung (Anforderungen, Teammitglieder, Rollen, Tools, ...)
GUI-Skizzen und Bedienkonzept (Schnittstellenentwürfe, Tastaturbelegung, Maussteuerung, ...)
Evaluierung der Frameworks (zumindest 2) inkl. Beispielcode und Ergebnis (begründete Entscheidung)
Technische Dokumentation: Architektur der entwickelten Software (Klassen, Design Patterns)
Achtung: Bitte überlegt euch eine saubere Architektur!
Den gesamten Source Code in 1 Klasse zu packen ist nicht ausreichend!
Kurze Bedienungsanleitung
Sauberes Dokument (Titelblatt, Kopf- und Fußzeile, ...)

Hinweise zu OpenGL und glut:

Ein Objekt kann einfach mittels glutSolidSphere() erstellt werden.
Die Planten werden mittels Modelkommandos bewegt: glRotate(), glTranslate()
Die Kameraposition wird mittels gluLookAt() gesetzt
Bedenken Sie bei der Perspektive, dass entfernte Objekte kleiner - nahe entsprechende größer darzustellen sind.
Wichtig ist dabei auch eine möglichst glaubhafte Darstellung. gluPerspective(), glFrustum()
Für das Einbetten einer Textur kann die Library Pillow verwendet werden! Die Community unterstützt Sie bei der Verwendung.

Viel Spaß und viel Erfolg! Happy Working und Hands On!