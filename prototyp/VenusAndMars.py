# Entnommen aus den Panda3D-Samples
# Author: Shao Zhang and Phil Saltzman
# Last Updated: 4/20/2005

import direct.directbase.DirectStart
from direct.showbase import DirectObject
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from Ambience import *
import sys

class World(DirectObject):

    def __init__(self):

        # Globale Variablen
        self.yearscale = 65
        self.dayscale = self.yearscale / 365.0 * 5
        self.orbitscale = 15
        self.sizescale = 1
        self.amb = Ambience(base, loader, 0.8, 1.0, -0.5, 0.5)

        self.amb.initbg()

        self.title = OnscreenText(text="Venus and Mars - Taschner | Weinberger 5BHIT", style=1, fg=(1, 1, 1, 1), pos=(0.9, -0.95), scale=.03)

        self.loadPlanets()  # Load, texture, and position the planets
        self.rotatePlanets()  # Set up the motion to start them moving

        self.simRunning = True  # boolean to keep track of the
        # state of the global simulation

        self.amb.startsound() #Sound soll erst beginnen, wenn alles fertig geladen

        self.accept('escape', sys.exit)  # Exit the program when escape is pressed

    # end __init__

    def toggleInterval(self, interval):
        if interval.isPlaying():
            interval.pause()
        else:
            interval.resume()

    # end toggleInterval

    def handleEarth(self):
        self.togglePlanet("Earth", self.day_period_earth,
                          self.orbit_period_earth, self.ekeyEventText)
        self.togglePlanet("Moon", self.day_period_moon,
                          self.orbit_period_moon)

    # end handleEarth

    def loadPlanets(self):

        dlight = DirectionalLight('dlight')
        dlight.setColor(VBase4(1, 1, 1, 1))
        dlnp = render.attachNewNode(dlight)
        dlnp.setHpr(0, 10, 0)
        render.setLight(dlnp)

        self.orbit_root_mercury = render.attachNewNode('orbit_root_mercury')
        self.orbit_root_venus = render.attachNewNode('orbit_root_venus')
        self.orbit_root_mars = render.attachNewNode('orbit_root_mars')
        self.orbit_root_earth = render.attachNewNode('orbit_root_earth')
        self.orbit_root_test = render.attachNewNode('orbit_root_test')
        self.orbit_root_vadertie = render.attachNewNode('orbit_root_vadertie')

        self.orbit_root_moon = (
            self.orbit_root_earth.attachNewNode('orbit_root_moon'))

        self.sky = loader.loadModel("models/solar_sky_sphere")

        self.sky_tex = loader.loadTexture("models/galaxie.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(40)

        self.sun = loader.loadModel("models/planet_sphere")
        self.sun_tex = loader.loadTexture("models/todesstern.jpg")
        self.sun.setTexture(self.sun_tex, 1)
        self.sun.reparentTo(render)
        self.sun.setScale(3 * self.sizescale)

        self.mercury = loader.loadModel("models/planet_sphere")
        self.mercury_tex = loader.loadTexture("models/planet1.jpg")
        self.mercury.setTexture(self.mercury_tex, 1)
        self.mercury.reparentTo(self.orbit_root_mercury)
        self.mercury.setPos(0.38 * self.orbitscale, 0, 0)
        self.mercury.setScale(0.15 * self.sizescale)

        self.venus = loader.loadModel("models/planet_sphere")
        self.venus_tex = loader.loadTexture("models/planet2.png")
        self.venus.setTexture(self.venus_tex, 1)
        self.venus.reparentTo(self.orbit_root_venus)
        self.venus.setPos(0.72 * self.orbitscale, 0, 0)
        self.venus.setScale(0.923 * self.sizescale)

        self.mars = loader.loadModel("models/planet_sphere")
        self.mars_tex = loader.loadTexture("models/planet3.png")
        self.mars.setTexture(self.mars_tex, 1)
        self.mars.reparentTo(self.orbit_root_mars)
        self.mars.setPos(1.52 * self.orbitscale, 0, 0)
        self.mars.setScale(0.515 * self.sizescale)

        self.earth = loader.loadModel("models/planet_sphere")
        self.earth_tex = loader.loadTexture("models/planet4.png")
        self.earth.setTexture(self.earth_tex, 1)
        self.earth.reparentTo(self.orbit_root_earth)
        self.earth.setScale(self.sizescale)
        self.earth.setPos(self.orbitscale, 0, 0)

        self.orbit_root_moon.setPos(self.orbitscale, 0, 0)

        self.moon = loader.loadModel("models/planet_sphere")
        self.moon_tex = loader.loadTexture("models/planet5.png")
        self.moon.setTexture(self.moon_tex, 1)
        self.moon.reparentTo(self.orbit_root_moon)
        self.moon.setScale(0.4 * self.sizescale)
        self.moon.setPos(0.1 * self.orbitscale, 0, 0)

        self.test = loader.loadModel("models/planet_sphere")
        self.test_tex = loader.loadTexture("models/planet7.jpg")
        self.test.setTexture(self.test_tex, 1)
        self.test.reparentTo(self.orbit_root_test)
        self.test.setScale(self.sizescale)
        self.test.setPos(1.3 * self.orbitscale, 0, 0)

        self.vadertie = loader.loadModel("models/xwing.x")
        self.vadertie.reparentTo(self.orbit_root_vadertie)
        self.vadertie.setPos(0.3 * self.orbitscale, 0, 0)
        self.vadertie.setScale(0.05 * self.sizescale)
        self.vadertie.setHpr(0, 180, 0)

    def rotatePlanets(self):

        self.day_period_sun = self.sun.hprInterval(20, Vec3(360, 0, 0))

        self.orbit_period_mercury = self.orbit_root_mercury.hprInterval(
            (0.241 * self.yearscale), Vec3(360, 0, 0))
        self.day_period_mercury = self.mercury.hprInterval(
            (59 * self.dayscale), Vec3(360, 0, 0))

        self.orbit_period_venus = self.orbit_root_venus.hprInterval(
            (0.615 * self.yearscale), Vec3(360, 0, 0))
        self.day_period_venus = self.venus.hprInterval(
            (243 * self.dayscale), Vec3(360, 0, 0))

        self.orbit_period_earth = self.orbit_root_earth.hprInterval(self.yearscale, Vec3(360, 0, 0))
        self.day_period_earth = self.earth.hprInterval(1.881 * self.dayscale, Vec3(360, 0, 0))

        self.orbit_period_moon = self.orbit_root_moon.hprInterval(
            (.0749 * self.yearscale), Vec3(360, 0, 0))
        self.day_period_moon = self.moon.hprInterval(
            (.0749 * self.yearscale), Vec3(360, 0, 0))

        self.orbit_period_mars = self.orbit_root_mars.hprInterval(
            (1.881 * self.yearscale), Vec3(360, 0, 0))
        self.day_period_mars = self.mars.hprInterval(
            (1.03 * self.dayscale), Vec3(360, 0, 0))

        self.orbit_period_test = self.orbit_root_test.hprInterval(
            (0.7 * self.yearscale), Vec3(360, 0, 0))

        self.day_period_test = self.test.hprInterval(
            (4 * self.dayscale), Vec3(360, 0, 0))

        self.orbit_period_vadertie = self.orbit_root_vadertie.hprInterval(
            (0.1 * self.yearscale), Vec3(360, 0, 0))

        self.day_period_vadertie = self.vadertie.hprInterval(
            (25000 * self.dayscale), Vec3(360, 0, 0))

        self.day_period_sun.loop()
        self.orbit_period_mercury.loop()
        self.day_period_mercury.loop()
        self.orbit_period_venus.loop()
        self.day_period_venus.loop()
        self.orbit_period_earth.loop()
        self.day_period_earth.loop()
        self.orbit_period_moon.loop()
        self.day_period_moon.loop()
        self.orbit_period_mars.loop()
        self.day_period_mars.loop()
        self.orbit_period_test.loop()
        self.day_period_test.loop()
        self.orbit_period_vadertie.loop()
        self.day_period_vadertie.loop()

# end RotatePlanets()  # end class world

w = World()

run()