# ficus

Ficus provides a context manager for matplotlib figures. It finds particular utility in jupyter
notebooks, where the user might prefer that figures are not automatically displayed but still wants
the option to embed them inline. This is accomplished with:

    %config InlineBackend.close_figures = False

However, the user is now responsible for making new `Figure` objects and closing them, which is a
pain. The ficus context manager takes care of this boilerplate for you.
