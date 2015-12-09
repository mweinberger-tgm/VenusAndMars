"""
Fuer das Laden und Rotieren der Objekte verschiedenster Art zustaendig
"""
from Constants import *
from panda3d.core import *

__author__ = 'Thomas Taschner, Michael Weinberger'
__date__ = 20151209
__version__ = 1.0


class Object:
    """
    Laedt und rotiert die Sonne, Planeten und den Mond.
    """

    def __init__(self, name, pathmodel, pathtexture, position, planetsize, loader, render):
        """
        Initialisieren des Objekts im Sonnensystem
        :param name: der Name des Objekts
        :param pathmodel: Pfad zum Model-File
        :param pathtexture: Pfad zur Textur
        :param position: die Position des Objekts
        :param planetsize: die Groesse des Objekts
        :param loader: das Loader-Objekt
        :param render: das Render-Objekt
        """
        self.name = name
        self.pathmodel = pathmodel
        self.pathtexture = pathtexture
        self.planetsize = planetsize
        self.loader = loader
        self.render = render
        self.position = position
        #####
        self.orbit_root = None
        self.tex = None
        self.day_period = None
        self.orbit_period = None

    def loadobject(self):
        """
        Laedt den Planeten
        """
        self.orbit_root = self.render.attachNewNode(self.name)

        self.name = self.loader.loadModel(self.pathmodel)
        self.tex = self.loader.loadTexture(self.pathtexture)
        self.name.setTexture(self.tex, 1)
        self.name.reparentTo(self.orbit_root)
        self.name.setPos(self.position * GlobalVar.ORBITSCALE, 0, 0)
        self.name.setScale(self.planetsize * GlobalVar.SIZESCALE)

    def rotatesun(self):
        """
        Laedt die Sonne. Eigene Methode, da nur Eigenrotation vorhanden.
        """
        self.day_period = self.name.hprInterval(20, Vec3(360, 0, 0))
        self.day_period.loop()

    def rotateobject(self, year, day):
        """
        Rotiert einen Planeten
        :param year: Dauer in Jahren, die fuer eine volle Rotation um die Sonne benoetigt wird.
        :param day: Dauer in Tagen, die fuer eine volle Eigenrotation benoetigt wird.
        """
        self.orbit_period = self.orbit_root.hprInterval(
            (year * GlobalVar.YEARSCALE), Vec3(360, 0, 0))
        self.day_period = self.name.hprInterval(
            (day * GlobalVar.DAYSCALE), Vec3(360, 0, 0))

        self.orbit_period.loop()
        self.day_period.loop()

    def loadxwing(self):
        """
        Laedt das Xwing Modell
        """
        self.orbit_root = self.render.attachNewNode(self.name)

        self.name = self.loader.loadModel(self.pathmodel)
        self.name.reparentTo(self.orbit_root)
        self.name.setPos(self.position * GlobalVar.ORBITSCALE, 0, 0)
        self.name.setScale(self.planetsize * GlobalVar.SIZESCALE)
        self.name.setHpr(0, 180, 0)

    def loadmoon(self, earth):
        """
        Hingepfuschte Anwendung des Decorator-Patterns, bindet den Mond an die Erde
        :param earth: das Erde-Objekt
        """
        self.orbit_root = (earth.orbit_root.attachNewNode('orbit_root_moon'))
        self.orbit_root.setPos(GlobalVar.ORBITSCALE, 0, 0)
        ###
        self.name = self.loader.loadModel(self.pathmodel)
        self.tex = self.loader.loadTexture(self.pathtexture)
        self.name.setTexture(self.tex, 1)
        self.name.reparentTo(self.orbit_root)
        self.name.setPos(0.1 * GlobalVar.ORBITSCALE, 0, 0)
        self.name.setScale(self.planetsize * GlobalVar.SIZESCALE)
