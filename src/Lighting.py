from panda3d.core import *
__author__ = 'Taschner | Weinberger'


"""
Die Beleuchtung des Solarsystems, da der Todesstern keine Lichtquelle ist, und als einzige Beleuchtungsform
der gegebenen realistisch aussieht.
"""


class Lighting:

    def activateshadows(self):

        dlight = DirectionalLight('dlight')
        dlight.setColor(VBase4(1, 1, 1, 1))
        dlnp = render.attachNewNode(dlight)
        dlnp.setHpr(0, 10, 0)
        render.setLight(dlnp)

    def __init__(self, render):
        self.render = render
