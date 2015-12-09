from Object import *
__author__ = 'Taschner | Weinberger'

"""
Die Factory fuer oft initialisierte Objekte
"""


class BodyFactory(object):
    @staticmethod
    def create_object(object_name):
        if object_name == 'deathstar':
            return Deathstar()
        elif object_name == 'Deluxe':
            return None
