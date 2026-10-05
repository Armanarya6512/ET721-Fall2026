"""
Name: Arman Arya 
Lab : 09
Date: October,05, 2026
"""

import pytest

from math_utils import multiply, divide

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 3) == 3.33
    with pytest.raises(ValueError):
        divide(10, 0) 