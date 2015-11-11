#!/usr/bin/env python
__version__ = '0.0.1'

from manager import FigureManager

def set_no_xserver(backend='Agg'):
    import matplotlib as mpl
    mpl.use(backend)
