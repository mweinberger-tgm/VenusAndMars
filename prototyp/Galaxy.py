__author__ = 'Taschner | Weinberger'

"""
Laden der Galaxie
In Folge: Laden des Modells, Laden der Textur, Festlegen des Galaxiedurchmessers (Scale)
"""


class Galaxy:

    def __init__(self, pathmodel, pathtexture, galaxysize, loader, render):

        self.pathmodel = pathmodel
        self.pathtexture = pathtexture
        self.galaxysize = galaxysize
        self.loader = loader
        self.render = render

    def loadenvironment(self):

        sky = self.loader.loadModel(self.pathmodel)

        sky_tex = self.loader.loadTexture(self.pathtexture)
        sky.setTexture(sky_tex, 1)
        sky.reparentTo(self.render)
        sky.setScale(self.galaxysize)
