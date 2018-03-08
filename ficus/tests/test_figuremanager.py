#!/usr/bin/env python

from matplotlib import axes
from matplotlib import figure

import os
from unittest import TestCase

from utils import TemporaryDirectory, Move, touch, TemporaryFile
from ficus import FigureManager

class TestFigureManager(TestCase):

    def test_save(self):
        '''Test that FigureManager saves a plot.
        '''
        with TemporaryDirectory() as td:
            with TemporaryFile(td) as filename:
                with FigureManager(filename=filename + '.pdf') as (fig, ax):
                    ax.plot(range(10), range(10))
                
                assert os.path.isfile(filename + '.pdf')

    def test_subplots_nrows(self):
        '''Test that FigureManager generates multiple subplots with nrows.
        '''
        
        with FigureManager(nrows=3) as (fig, ax):
            assert len(ax) == 3
            assert type(fig) is figure.Figure
            for axis in ax:
                assert isinstance(axis, axes.Axes)

    def test_subplots_ncols(self):
        '''Test that FigureManager generates multiple subplots with ncols.
        '''
        
        with FigureManager(ncols=3) as (fig, ax):
            assert len(ax) == 3
            assert isinstance(fig, figure.Figure)
            for axis in ax:
                assert isinstance(axis, axes.Axes)

    def test_subplots_nrows_ncols(self):
        '''Test that FigureManager generates multiple subplots with nrows and
        ncols.
        '''
        
        with FigureManager(nrows=3, ncols=3) as (fig, ax):
            assert len(ax) == 3
            assert len(ax[0]) == 3
            assert isinstance(fig, figure.Figure)
            for axrow in ax:
                for axis in axrow:
                    assert isinstance(axis, axes.Axes)

    def test_exception(self):
        '''Test that FigureManager handles internal exceptions properly.
        '''
        with TemporaryDirectory() as td:
            with TemporaryFile(td) as filename:

                # now we test the manager
                try:
                    rregexp = self.assertRaisesRegex
                except AttributeError:
                    rregexp = self.assertRaisesRegexp
                with rregexp(RuntimeError, 'TEST'):
                    with FigureManager(filename=filename) as (fig, ax):
                        raise RuntimeError('TEST')
                assert not os.path.isfile(filename), 'Should not have saved a file.'
