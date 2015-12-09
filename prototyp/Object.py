from Constants import *
__author__ = 'Taschner | Weinberger'

"""
Planeten
"""


class Object:

    def __init__(self, name, pathmodel, pathtexture, planetsize, loader, render):

        self.name = name
        self.pathmodel = pathmodel
        self.pathtexture = pathtexture
        self.planetsize = planetsize
        self.loader = loader
        self.render = render
        #####
        self.orbit_root = None
        self.tex = None

    def loadobject(self):

        self.orbit_root = self.render.attachNewNode('orbit_root_' + self.name)

        self.name = self.loader.loadModel(self.pathmodel)
        self.tex = self.loader.loadTexture(self.pathtexture)
        self.name.setTexture(self.tex, 1)
        self.name.reparentTo(self.render)
        self.name.setScale(self.planetsize * GlobalVar.SIZESCALE)
