"""
Laden der Galaxie, Laden des Modells, Laden der Textur, Festlegen des Galaxiedurchmessers (Scale)
"""
__author__ = 'Thomas Taschner, Michael Weinberger'
__date__ = 20151209
__version__ = 1.0


class Galaxy:
    """
    Initialisiert die Galaxy und ihre Einstellungen
    """

    def __init__(self, pathmodel, pathtexture, galaxysize, loader, render):
        """
        Initialisiert die Galaxy
        :param pathmodel: Pfad zum Model-File
        :param pathtexture: Pfad zur Textur
        :param galaxysize: Groesse der Galaxy
        :param loader: das Loader-Objekt
        :param render: das Render-Objekt
        """
        self.pathmodel = pathmodel
        self.pathtexture = pathtexture
        self.galaxysize = galaxysize
        self.loader = loader
        self.render = render

    def loadenvironment(self):
        """
        Laedt das Model, die Textur, die Groesse fuer das Objekt und legt fest, an wen das Objekt gebunden ist
        """
        sky = self.loader.loadModel(self.pathmodel)

        sky_tex = self.loader.loadTexture(self.pathtexture)
        sky.setTexture(sky_tex, 1)
        sky.reparentTo(self.render)
        sky.setScale(self.galaxysize)
