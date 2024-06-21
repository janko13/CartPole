import pytest
from io import StringIO
import sys

from cart_pole import CartPole


def test_initialization():
    """ Test the initialization of CartPole with default and custom parameters. """
    # Test with default parameters
    cp_default = CartPole()
    assert cp_default.F == 10.0
    assert cp_default.M == 1.0
    assert cp_default.m == 0.1
    assert cp_default.l == 1.0

    # Test with custom parameters
    cp_custom = CartPole(F=20.0, M=2.0, m=0.2, l=1.5)
    assert cp_custom.F == 20.0
    assert cp_custom.M == 2.0
    assert cp_custom.m == 0.2
    assert cp_custom.l == 1.5

def test_print():
    """ Test the print method of CartPole class to ensure it prints correctly. """
    cp = CartPole(F=15.0, M=1.5, m=0.15, l=0.75)
    expected_output = "F: 15.0, M: 1.5, m: 0.15, l: 0.75\n"

    # Redirect stdout to capture print outputs
    captured_output = StringIO()
    sys.stdout = captured_output
    cp.print()
    sys.stdout = sys.__stdout__  # Reset redirect

    # Check if the print output matches the expected output
    assert captured_output.getvalue() == expected_output