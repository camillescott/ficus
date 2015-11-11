#!/usr/bin/env python

from ficus import set_no_xserver
set_no_xserver()
from ficus import FigureManager

import os
from unittest import TestCase

from matplotlib import axes
from matplotlib import figure

from utils import TemporaryDirectory, Move, TestData, touch, TemporaryFile


class TestFigureManager(TestCase):

    @classmethod
    def setup_class(cls):
        pass

    def test_save(self):
        '''Test that FigureManager saves a plot.
        '''
        with TemporaryDirectory() as td:
            with TemporaryFile(td) as filename:
        
                with FigureManager(filename=filename) as (fig, ax):
                    ax.plot(xrange(10), xrange(10))
                
                self.assertTrue(os.path.isfile(filename + '.png'))

                with FigureManager(filename=filename+'.svg') as (fig, ax):
                    ax.plot(xrange(10), xrange(10))
                
                self.assertTrue(os.path.isfile(filename + '.svg'))

       

    def test_subplots_nrows(self):
        '''Test that FigureManager generates multiple subplots with nrows.
        '''
        
        with FigureManager(nrows=3) as (fig, ax):
            self.assertEquals(len(ax), 3)
            self.assertIs(type(fig), figure.Figure)
            for axis in ax:
                self.assertIsInstance(axis, axes.Axes)

    def test_subplots_ncols(self):
        '''Test that FigureManager generates multiple subplots with ncols.
        '''
        
        with FigureManager(ncols=3) as (fig, ax):
            self.assertEquals(len(ax), 3)
            self.assertIsInstance(fig, figure.Figure)
            for axis in ax:
                self.assertIsInstance(axis, axes.Axes)

    def test_subplots_nrows_ncols(self):
        '''Test that FigureManager generates multiple subplots with nrows and
        ncols.
        '''
        
        with FigureManager(nrows=3, ncols=3) as (fig, ax):
            self.assertEquals(len(ax), 3)
            self.assertEquals(len(ax[0]), 3)
            self.assertIsInstance(fig, figure.Figure)
            for axrow in ax:
                for axis in axrow:
                    self.assertIsInstance(axis, axes.Axes)

    def test_exception(self):
        '''Test that FigureManager handles internal exceptions properly.
        '''
        with TemporaryDirectory() as td:
            with TemporaryFile(td) as filename:

                # now we test the manager
                with self.assertRaisesRegexp(RuntimeError, 'TEST'):
                    with FigureManager(filename=filename) as (fig, ax):
                        raise RuntimeError('TEST')
                self.assertFalse(os.path.isfile(filename),
                                 msg='Should not have saved a file.')
