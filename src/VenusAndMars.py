"""
Die Main-Methode, die das 'Sonnensystem' startet.
Inspiriert von den Panda3D Samples.
Setzt alles zusammen und startet die Applikation.
"""

__author__ = 'Thomas Taschner, Michael Weinberger'
__date__ = 20151209
__version__ = 1.0

import direct.directbase.DirectStart
from direct.showbase import DirectObject
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from Ambiance import *
from Lighting import *
from Galaxy import *
from BodyFactory import *
import sys


class World(DirectObject):
    def __init__(self):
        self.amb = Ambiance(base, loader, 1.0, 0.6, -0.5, 0.5)
        self.lig = Lighting(render)

        self.amb.initbg()

        self.title = OnscreenText(text="Venus and Mars - Taschner | Weinberger 5BHIT", style=1, fg=(1, 1, 1, 1),
                                  pos=(0.9, -0.95), scale=.03)

        self.galaxy = Galaxy("models/solar_sky_sphere.egg", "models/galaxie.jpg", 1000, loader, render)
        self.galaxy.loadenvironment()

        deathstar = BodyFactory.create_object('deathstar')
        deathstar.loadobject()
        deathstar.rotatesun()

        mercury = BodyFactory.create_object('mercury')
        mercury.loadobject()
        mercury.rotateobject(0.241, 59)

        venus = BodyFactory.create_object('venus')
        venus.loadobject()
        venus.rotateobject(0.615, 243)

        mars = BodyFactory.create_object('mars')
        mars.loadobject()
        mars.rotateobject(1.5, 1.7)

        earth = BodyFactory.create_object('earth')
        earth.loadobject()
        earth.rotateobject(1, 1.5)

        moon = BodyFactory.create_object('moon')
        moon.loadmoon(earth)
        moon.rotateobject(.1, 1)

        tatooine = BodyFactory.create_object('tatooine')
        tatooine.loadobject()
        tatooine.rotateobject(10, 10)

        mordor = BodyFactory.create_object('mordor')
        mordor.loadobject()
        mordor.rotateobject(0.7, 4)

        xwing = BodyFactory.create_object('xwing')
        xwing.loadxwing()
        xwing.rotateobject(0.1, 25000)

        self.lig.activateshadows()

        self.amb.startsound()  # Sound soll erst beginnen, wenn alles fertig geladen ist

        self.accept('escape', sys.exit)  # Programm schliessen, wenn Escape gedrueckt wird


w = World()

run()
