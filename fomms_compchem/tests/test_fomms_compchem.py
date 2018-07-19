"""
Unit and regression test for the fomms_compchem package.
"""

# Import package, test suite, and other packages as needed
import fomms_compchem
import pytest
import sys

def test_fomms_compchem_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "fomms_compchem" in sys.modules
