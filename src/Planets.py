"""
Definition aller Planeten. Jeder Planet hat seine eigene Klasse, in dem der Name, der Pfad zum Modell und zur Textur,
die Position, die Groesse und das Render- und Loader-Objekt gesetzt werden.
"""

from Object import *

__author__ = 'Taschner | Weinberger'


class Deathstar(Object):
    """
    Initialisiert den Todesstern (die Sonne)
    """

    def __init__(self):
        """
        Initialisiert den Todesstern
        """
        self.name = "deathstar"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/todesstern.jpg"
        self.position = 0
        self.planetsize = 3
        self.loader = loader
        self.render = render


class Mercury(Object):
    """
    Initialisiert den Planeten Merkur
    """

    def __init__(self):
        """
        Initialisiert den Planeten Merkur
        """
        self.name = "mercury"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet1.jpg"
        self.position = 0.38
        self.planetsize = 0.15
        self.loader = loader
        self.render = render


class Venus(Object):
    """
    Initialisiert den Planeten Venus
    """

    def __init__(self):
        """
        Initialisiert den Planeten Venus
        """
        self.name = "venus"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet2.jpg"
        self.position = 0.72
        self.planetsize = 0.923
        self.loader = loader
        self.render = render


class Mars(Object):
    """
    Initialisiert den Planeten Mars
    """

    def __init__(self):
        """
        Initialisiert den Planeten Mars
        """
        self.name = "mars"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet3.jpg"
        self.position = 1.52
        self.planetsize = 0.515
        self.loader = loader
        self.render = render


class Earth(Object):
    """
    Initialisiert den Planeten Erde
    """

    def __init__(self):
        """
        Initialisiert den Planeten Erde
        """
        self.name = "earth"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet4.jpg"
        self.position = 1
        self.planetsize = 1
        self.loader = loader
        self.render = render


class Moon(Object):
    """
    Initialisiert den Mond
    """

    def __init__(self):
        """
        Initialisiert den Mond
        """
        self.name = "moon"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet5.jpg"
        self.position = 0.1
        self.planetsize = 0.4
        self.loader = loader
        self.render = render


class Tatooine(Object):
    """
    Initialisiert den Planeten Tatooine
    """

    def __init__(self):
        """
        Initialisiert den Planeten Tatooine
        """
        self.name = "tatooine"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet6.jpg"
        self.position = 5
        self.planetsize = 8
        self.loader = loader
        self.render = render


class Mordor(Object):
    """
    Initialisiert den Planeten Mordor
    """

    def __init__(self):
        """
        Initialisiert den Planeten Mordor
        """
        self.name = "mordor"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet7.jpg"
        self.position = 1.3
        self.planetsize = 1.5
        self.loader = loader
        self.render = render


class Xwing(Object):
    """
    Initialisiert den Xwing.
    """

    def __init__(self):
        """
        Initialisiert den Xwing.
        """
        self.name = "xwing"
        self.pathmodel = "models/xwing.x"
        self.pathtexture = None
        self.position = 0.3
        self.planetsize = 0.05
        self.loader = loader
        self.render = render
