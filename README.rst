ficus
=====

.. image:: https://travis-ci.org/camillescott/ficus.svg?branch=master
    :align: right
    :target: https://travis-ci.org/camillescott/ficus

About
-----

Ficus provides a context manager for matplotlib figures. It finds particular utility in jupyter
notebooks, where the user might prefer that figures are not automatically displayed but still wants
the option to embed them inline -- such behavior can be accomplished with:

.. code:: python

    %config InlineBackend.close_figures = False

However, the user is now responsible for making new `Figure` objects and closing them, which is a
pain. The ficus context manager takes care of this boilerplate of opening, showing, saving, and
closing figures for you.

Example
-------

Some very basic usage:

.. code:: python

    from ficus import FigureManager
    import numpy as np
    
    X = np.arange(0, 10, .1)
    Y = np.exp(X)
    
    with FigureManager(filename='myplot.png', show=True) as (fig, ax):
        ax.plot(X, Y)
        ax.set_title('The Exponential Function')

`FigureManager` uses the `pyplot.subplots(..)` to generate its axes. Thus, you can specify rows and
columns and get an array of `Axes` objects:

.. code:: python

    with FigureManager(show=True, nrows=3, ncols=4) as (fig, ax_mat):
        for i, row in enumerate(ax_mat):
            for j, ax in enumerate(row):
                ax.plot(X, X**(i+j))
                ax.set_title(r'$y = x^{0}$'.format(i+j), fontsize=14)

In fact, you can pass any keyword arguments you'd like to `subplots`:

.. code:: python

    with FigureManager(filename='myplot.png', show=True, figsize=(12,8)) as (fig, ax):
        ax.plot(X, Y)

Take a look at the `examples <Examples.ipynb>`__ to see it being used in a jupyter notebook.
