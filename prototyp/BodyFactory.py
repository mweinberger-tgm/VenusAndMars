from Planets import *
__author__ = 'Taschner | Weinberger'

"""
Die Factory fuer oft initialisierte Objekte
"""


class BodyFactory(object):
    @staticmethod
    def create_object(object_name):
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
