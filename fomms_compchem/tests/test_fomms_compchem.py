"""
Unit and regression test for the fomms_compchem package.
"""

# Import package, test suite, and other packages as needed
import fomms_compchem as integrate
import pytest
import sys
import numpy as np

def test_fomms_compchem_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "fomms_compchem" in sys.modules


def g(x):
    return 3.0 * x

def f(x):
    return np.power(x, 2)

def h(x):
    return np.ones(x.size)

def volume(x):
    squares = np.power(x, 2)
    return np.sum(squares, axis=1)

def test_trapz():
    x = np.array([0, 10])
    I = integrate.newton_cotes.trapz(x, g)
    assert I == 150.00

# def test_monte1d():
#     x = np.array([0, 3])
#     I = integrate.stochastic.monte_1d(x, f, 100000)
#     assert np.allclose(I, 9.00, 1e-2)

# def test_simpson():
#     x = np.array([0, 3])
#     I = integrate.simpson(x, f)
#     assert I == 9.00
# 
def test_monte2d():
    domain = np.array([[-1, -1], [1, 1]])
    I = integrate.monte_2d(h, volume, domain, 1000000)
    assert np.allclose(I, np.pi, 1e-2)
