"""
Anwendung der Factory Patterns zwecks Instanzierung der Objekte im Solarsystem.
"""

from Planets import *

__author__ = 'Thomas Taschner, Michael Weinberger'
__date__ = 20151209
__version__ = 1.0


class BodyFactory(object):
    """
    Dient zur Instanzierung aller Objekte im Solarsystem. Nimmt einen Objektnamen entgegen und
    erstellt ein entsprechendes Objekt.
    """

    @staticmethod
    def create_object(object_name):
        """
        Statische Methode, die die Objekte instanziert.
        :param object_name: Name des zur instanzierenden Objekts
        :return: das entsprechende Objekt
        """
        if object_name == 'deathstar':
            return Deathstar()
        elif object_name == 'mercury':
            return Mercury()
        elif object_name == 'venus':
            return Venus()
        elif object_name == 'mars':
            return Mars()
        elif object_name == 'earth':
            return Earth()
        elif object_name == 'moon':
            return Moon()
        elif object_name == 'tatooine':
            return Tatooine()
        elif object_name == 'mordor':
            return Mordor()
        elif object_name == 'xwing':
            return Xwing()
