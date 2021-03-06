# Author: Shao Zhang and Phil Saltzman
# Last Updated: 4/20/2005
#
# This tutorial will cover events and how they can be used in Panda
# Specifically, this lesson will use events to capture keyboard presses and
# mouse clicks to trigger actions in the world. It will also use events
# to count the number of orbits the Earth makes around the sun. This
# tutorial uses the same base code from the solar system tutorial.

import direct.directbase.DirectStart
from direct.showbase import DirectObject
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
import sys


# We start this tutorial with the standard class. However, the class is a
# subclass of an object called DirectObject. This gives the class the ability
# to listen for and respond to events. From now on the main class in every
# tutorial will be a subclass of DirectObject

class World(DirectObject):
    # Macro-like function used to reduce the amount to code needed to create the
    # on screen instructions
    def genLabelText(self, text, i):
        return OnscreenText(text=text, pos=(-1.3, .95 - .05 * i), fg=(1, 1, 1, 1),
                            align=TextNode.ALeft, scale=.05, mayChange=1)

    def __init__(self):

        # The standard camera position and background initialization
        base.setBackgroundColor(0, 0, 0)
        #base.disableMouse()
        #camera.setPos(0, -50, 0)
        #base.useDrive()

        # The global variables we used to control the speed and size of objects
        self.yearscale = 65
        self.dayscale = self.yearscale / 365.0 * 5
        self.orbitscale = 15
        self.sizescale = 1

        self.loadPlanets()  # Load, texture, and position the planets
        self.rotatePlanets()  # Set up the motion to start them moving

        # The standard title text that's in every tutorial
        # Things to note:
        # -fg represents the forground color of the text in (r,g,b,a) format
        # -pos  represents the position of the text on the screen.
        #      The coordinate system is a x-y based wih 0,0 as the center of the
        #      screen
        # -align sets the alingment of the text relative to the pos argument.
        #      Default is center align.
        # -scale set the scale of the text
        # -mayChange argument lets us change the text later in the program.
        #       By default mayChange is set to 0. Trying to change text when
        #       mayChange is set to 0 will cause the program to crash.
        self.title = OnscreenText(text="Venus and Mars - Taschner | Weinberger 5BHIT",
                                  style=1, fg=(1, 1, 1, 1),
                                  pos=(0.9, -0.95), scale=.03)

        self.yearCounter = 0  # year counter for earth years
        self.simRunning = True  # boolean to keep track of the
        # state of the global simulation

        # Events
        # Each self.accept statement creates an event handler object that will call
        # the specified function when that event occurs.
        # Certain events like "mouse1", "a", "b", "c" ... "z", "1", "2", "3"..."0"
        # are references to keyboard keys and mouse buttons. You can also define
        # your own events to be used within your program. In this tutorial, the
        # event "newYear" is not tied to a physical input device, but rather
        # is sent by the function that rotates the Earth whenever a revolution
        # completes to tell the counter to update
        self.accept('escape', sys.exit)  # Exit the program when escape is pressed

    # end __init__

    # toggleInterval does exactly as its name implies
    # It takes an interval as an argument. Then it checks to see if it is playing.
    # If it is, it pauses it, otherwise it resumes it.
    def toggleInterval(self, interval):
        if interval.isPlaying():
            interval.pause()
        else:
            interval.resume()

    # end toggleInterval

    # Earth needs a special buffer function because the moon is tied to it
    # When the "e" key is pressed, togglePlanet is called on both the earth and
    # the moon.
    def handleEarth(self):
        self.togglePlanet("Earth", self.day_period_earth,
                          self.orbit_period_earth, self.ekeyEventText)
        self.togglePlanet("Moon", self.day_period_moon,
                          self.orbit_period_moon)

    # end handleEarth

    #########################################################################
    # Except for the one commented line below, this is all as it was before #
    # Scroll down to the next comment to see an example of sending messages #
    #########################################################################

    def loadPlanets(self):
        theme = loader.loadSfx("models/starwars.mp3")
        theme.setVolume(0.8);
        theme.setBalance(-0.5)
        theme.play()

        ambience = loader.loadSfx("models/ambience.mp3")
        ambience.setVolume(1.0)
        ambience.setBalance(0.5)
        ambience.play()

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