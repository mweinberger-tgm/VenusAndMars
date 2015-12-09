"""
Beinhaltet lediglich nur Variablen, die auf gloabaler Ebene gueltig sein sollen.
"""
__author__ = 'Thomas Taschner, Michael Weinberger'
__date__ = 20151209
__version__ = 1.0


class GlobalVar:
    """
    Beinhaltet globale Variablen, die fuer beispielsweise die Geschwindigkeit der Planeten, Dauer eines Jahres,
    Groesse eines Objektes, ... zustaendig ist.
    """
    YEARSCALE = 65
    DAYSCALE = YEARSCALE / 365.0 * 5
    ORBITSCALE = 15
    SIZESCALE = 1
