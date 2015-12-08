# coding=utf-8
__author__ = 'Taschner | Weinberger'

"""
Zusammenfassung der Ambience, des Hintergrunds und des Sounds
"""


class Ambience:

    """
    Setzt die Hintergrundfarbe, initialisiert die Umgebungssphere mit Sternenhimmel
    """
    def initbg(self):
        # Hintergrundfarbe setzen
        self.base.setBackgroundColor(0, 0, 0)

        # Limitierung der Kamera, flüssigere Kamerafahrten
        #base.useDrive()

    """
    Startet den Imperial March & den Ambience-Sound mit kämpfenden X-Wings
    """
    def startsound(self):

        theme = self.loader.loadSfx("models/starwars.mp3")
        theme.setVolume(0.8) #etwas leiser als Ambiance
        theme.setBalance(-0.5) #linker Audiokanal
        theme.play()

        ambience = self.loader.loadSfx("models/ambience.mp3")
        ambience.setVolume(1.0)
        ambience.setBalance(0.5) #rechter Audiokanal
        ambience.play()

    def __init__(self, base, loader):
        self.base = base
        self.loader = loader
