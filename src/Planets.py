from Object import *

__author__ = 'Taschner | Weinberger'

"""
Planeten
"""

class Deathstar(Object):
    def __init__(self):
        self.name = "deathstar"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/todesstern.jpg"
        self.position = 0
        self.planetsize = 3
        self.loader = loader
        self.render = render

class Mercury(Object):
    def __init__(self):
        self.name = "mercury"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet1.jpg"
        self.position = 0.38
        self.planetsize = 0.15
        self.loader = loader
        self.render = render

class Venus(Object):
    def __init__(self):
        self.name = "venus"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet2.jpg"
        self.position = 0.72
        self.planetsize = 0.923
        self.loader = loader
        self.render = render

class Mars(Object):
    def __init__(self):
        self.name = "mars"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet3.jpg"
        self.position = 1.52
        self.planetsize = 0.515
        self.loader = loader
        self.render = render

class Earth(Object):
    def __init__(self):
        self.name = "earth"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet4.jpg"
        self.position = 1
        self.planetsize = 1
        self.loader = loader
        self.render = render

class Moon(Object):
    def __init__(self):
        self.name = "moon"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet5.jpg"
        self.position = 0.1
        self.planetsize = 0.4
        self.loader = loader
        self.render = render

class Tatooine(Object):
    def __init__(self):
        self.name = "tatooine"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet6.jpg"
        self.position = 5
        self.planetsize = 8
        self.loader = loader
        self.render = render

class Mordor(Object):
    def __init__(self):
        self.name = "mordor"
        self.pathmodel = "models/planet_sphere"
        self.pathtexture = "models/planet7.jpg"
        self.position = 1.3
        self.planetsize = 1.5
        self.loader = loader
        self.render = render

class Xwing(Object):
    def __init__(self):
        self.name = "xwing"
        self.pathmodel = "models/xwing.x"
        self.pathtexture = None
        self.position = 0.3
        self.planetsize = 0.05
        self.loader = loader
        self.render = render
