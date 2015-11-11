#!/usr/bin/env python

import matplotlib as mpl
import matplotlib.pyplot as plt
import sys


class FigureManager(object):

    def __init__(self, filename=None, show=False, 
                 nrows=1, ncols=1, figsize=(18,12), tight_layout=False,
                 **fig_kwds):

        self.fig, self.ax = plt.subplots(nrows=nrows, ncols=ncols,
                                         figsize=figsize,
                                         tight_layout=tight_layout, **fig_kwds)

        self.filename = filename
        self.show = show

        if self.fig != plt.gcf():
            self.clear()
            raise RuntimeError('Figure does not match active mpl figure')

    def __enter__(self):
        return self.fig, self.ax

    def __exit__(self, exc_type, exc_value, traceback):
        if not exc_type:
            if self.filename is not None:
                self.fig.savefig(self.filename)

            if self.show:
                plt.show(self.fig)
            self.clear()
        else:
            self.clear()
            return False

    def clear(self):
        plt.close(self.fig)
        del self.ax
        del self.fig
