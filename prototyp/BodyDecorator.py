from src.Object import *
from BodyFactory import *
__author__ = 'Taschner | Weinberger'

"""
Bestehende Objekte erweitern
"""


class BodyDecorator(Object):
    def __init__(self, decoratee_name):
        self.decoratee_name = decoratee_name

        decorate_me_with = BodyFactory.create_object(decoratee_name)

        self.orbit_root = (
            self.decoratee_name.attachNewNode(decorate_me_with.orbit_root)
        )