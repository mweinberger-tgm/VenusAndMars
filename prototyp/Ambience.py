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
        theme.setVolume(self.volumeimpmarch)
        theme.setBalance(self.balanceimpmarch)
        theme.play()

        ambiance = self.loader.loadSfx("models/ambience.mp3")
        ambiance.setVolume(self.volumeambience)
        ambiance.setBalance(self.balanceambience)
        ambiance.play()

    def __init__(self, base, loader, volumeimpmarch, volumeambience, balanceimpmarch, balanceambience):
        self.base = base
        self.loader = loader
        self.volumeimpmarch = volumeimpmarch
        self.volumeambience = volumeambience
        self.balanceimpmarch = balanceimpmarch
        self.balanceambience = balanceambience
