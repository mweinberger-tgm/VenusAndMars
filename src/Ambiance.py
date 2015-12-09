"""
Diese Klasse dient zum Laden von Assets, die nicht direkt mit den Planeten in Verbindung stehen.
Dazu gehoert das Setzen einer Hintergrundfarbe, aber auch das Laden von Musik, welche im Hintergrund spielt.
"""

__author__ = 'Thomas Taschner, Michael Weinberger'
__date__ = 20151209
__version__ = 1.0


class Ambiance:
    def __init__(self, base, loader, volumeimpmarch, volumeambience, balanceimpmarch, balanceambience):
        """
        Nimmt die Basis, auf der die Methoden aufbauen, zusammen mit den Parametern fuer die Lautstaerke und und die
        Position der Audiostreams im Stereomix entgegegen.
        :param base: das Basis-Objekt, auf dem alles aufbaut
        :param loader: das Loader-Objekt, welches zum Laden von bestimmten Eigenschaften verwendet wird
        :param volumeimpmarch: Pfad zu einer Audiodatei
        :param volumeambience: Pfad zu einer Audiodatei
        :param balanceimpmarch: Position des Files im Stereomix
        :param balanceambience: Position des Files im Stereomix
        """
        self.base = base
        self.loader = loader
        self.volumeimpmarch = volumeimpmarch
        self.volumeambience = volumeambience
        self.balanceimpmarch = balanceimpmarch
        self.balanceambience = balanceambience

    def initbg(self):
        """
        Setzt die Hintergrundfarbe
        Hier: 000, also schwarz
        """
        self.base.setBackgroundColor(0, 0, 0)

    def startsound(self):
        """
        Startet den Imperial March und den Ambiance-Sound mit kaempfenden X-Wings
        """
        theme = self.loader.loadSfx("models/starwars.mp4")
        theme.setVolume(self.volumeimpmarch)
        theme.setBalance(self.balanceimpmarch)
        theme.setLoop(True)  # Sonst nur 1 Play!
        theme.play()

        ambiance = self.loader.loadSfx("models/ambience.mp4")
        ambiance.setVolume(self.volumeambience)
        ambiance.setBalance(self.balanceambience)
        ambiance.setLoop(True)
        ambiance.play()
