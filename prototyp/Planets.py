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