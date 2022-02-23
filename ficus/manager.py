#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Camille Scott, 2015
# File   : manager.py
# License: MIT
# Author : Camille Scott <camille.scott.w@gmail.com>
# Date   : 23.02.2022

from packaging.version import Version
import sys


class FigureManagerBase(object):

    def __init__(self, plt, fig, ax, filename, show, save_kwds):

        self.plt = plt
        self.fig = fig
        self.ax = ax
        self.filename = filename
        self.show = show
        self.save_kwds = save_kwds

        if self.fig != self.plt.gcf():
            self.clear()
            raise RuntimeError('Figure does not match active mpl figure')

    def __enter__(self):
        return self.fig, self.ax

    def __exit__(self, exc_type, exc_value, traceback):

        if not exc_type:
            if self.filename is not None:
                self.fig.savefig(self.filename, **self.save_kwds)

            if self.show:
                self.plt.show(self.fig)
            self.clear()
        else:
            self.clear()
            return False

    def clear(self):
        self.plt.close(self.fig)
        del self.ax
        del self.fig


class FigureManager(FigureManagerBase):

    def __init__(self, filename=None, show=False, 
                       nrows=1, ncols=1, figsize=(18,12),
                       tight_layout=False, constrained_layout=True,
                       save_kwds={}, **fig_kwds):

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(nrows=nrows,
                               ncols=ncols,
                               figsize=figsize,
                               tight_layout=tight_layout,
                               constrained_layout=constrained_layout,
                               **fig_kwds)

        super().__init__(plt, fig, ax, filename, show, save_kwds)


class SubFigureManager(FigureManagerBase):

    def __init__(self, filename=None, show=False,
                 nrows=1, ncols=1, figsize=(18,12),
                 constrained_layout=True, subfigs='row',
                 save_kwds={}, subfigure_kwds={}, subplot_kwds={},
                 **fig_kwds):

        from matplotlib import __version__ as mpl_version
        import matplotlib.pyplot as plt

        if Version(mpl_version) < Version('3.4.0'):
            raise RuntimeError(f'matplotlib version {mpl_version} does not '
                               f'support subfigures (need >= 3.4.0)')

        if subfigs not in ['row', 'col']:
            raise ValueError('subfigs must be "row" or "col"')

        sfig_nrows = nrows if subfigs == 'row' else 1
        sfig_ncols = ncols if subfigs == 'col' else 1
        splt_nrows = nrows if subfigs == 'col' else 1
        splt_ncols = ncols if subfigs == 'row' else 1

        fig = plt.figure(figsize=figsize,
                         constrained_layout=constrained_layout,
                         **fig_kwds)
        axes = []
        self.subfigs = fig.subfigures(nrows=sfig_nrows,
                                      ncols=sfig_ncols,
                                      **subfigure_kwds)
        for subfig in self.subfigs:
            axes.append(subfig.subplots(nrows=splt_nrows,
                                        ncols=splt_ncols,
                                        **subplot_kwds))

        super().__init__(plt, fig, axes, filename, show, save_kwds)

    def __enter__(self):
        return self.fig, self.subfigs, self.ax
