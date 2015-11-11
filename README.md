# ficus

## About

Ficus provides a context manager for matplotlib figures. It finds particular utility in jupyter
notebooks, where the user might prefer that figures are not automatically displayed but still wants
the option to embed them inline. This is accomplished with:

    %config InlineBackend.close_figures = False

However, the user is now responsible for making new `Figure` objects and closing them, which is a
pain. The ficus context manager takes care of this boilerplate for you.

## Example

    from ficus import FigureManager
    import numpy as np
    
    X = np.arange(0, 10, .1)
    Y = np.exp(X)
    
    with FigureManager(filename='myplot.png', show=True) as (fix, ax):
        ax.plot(X, Y)
        ax.set_title('The Exponential Function')

---

[![Build Status](https://drone.io/github.com/camillescott/ficus/status.png)](https://drone.io/github.com/camillescott/ficus/latest)
