"""
This file contains the implementation of the trapezoidal rule
"""

import numpy as np

def trapz(x, f):
    """ 
    Compute a 1D definite integral using the trapezoidal rule
    Parameters
    ----------
    f : function
        User defined function.
    x : numpy array
        Integration domain.
    Returns
    -------
    I : float
        Integration result.
    """   
    a = x[0]
    b = x[1]
    ya = f(a)
    yb = f(b)
    I = (b-a) * (ya + yb) / 2
    return I
