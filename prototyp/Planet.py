__author__ = 'Taschner | Weinberger'

"""
Planeten
"""


class Planet:

    def __init__(self, name, render):

        self.name = name
        self.render = render
        #####
        self.orbit_root = None

    def loadplanets(self):

        self.orbit_root = self.render.attachNewNode('orbit_root_' + self.name)

