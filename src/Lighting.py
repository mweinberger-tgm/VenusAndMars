"""
Die Beleuchtung des Solarsystems, da der Todesstern keine Lichtquelle ist, und als einzige Beleuchtungsform
der gegebenen realistisch aussieht.
"""

from panda3d.core import *

__author__ = 'Thomas Taschner, Michael Weinberger'
__date__ = 20151209
__version__ = 1.0


class Lighting:
    """
    Setzt das Render-Objekt
    :param render: das Render-Objekt
    """

    def __init__(self, render):
        """
        Setzt das Render-Objekt
        """
        self.render = render

    def activateshadows(self):
        """
        Setzt die Position und die Farbe der Punktlichtquelle
        """
        dlight = DirectionalLight('dlight')
        dlight.setColor(VBase4(1, 1, 1, 1))
        dlnp = render.attachNewNode(dlight)
        dlnp.setHpr(0, 10, 0)
        render.setLight(dlnp)
