from matplotlib import axes
from matplotlib import figure

import os
import pytest

from ficus import FigureManager


@pytest.mark.usefixtures("use_agg")
class TestFigureManager(object):

    def test_save(self, tmpdir):
        '''Test that FigureManager saves a plot.
        '''
        with tmpdir.as_cwd():
            filename = str(tmpdir.join('test'))
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

    def test_exception(self, tmpdir):
        '''Test that FigureManager handles internal exceptions properly.
        '''
        with tmpdir.as_cwd():
            filename = str(tmpdir.join('test'))

            with pytest.raises(RuntimeError,
                               match='TEST'):
                with FigureManager(filename=filename) as (fig, ax):
                    raise RuntimeError('TEST')
            assert not os.path.isfile(filename), 'Should not have saved a file.'
