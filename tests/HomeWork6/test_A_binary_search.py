import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.A_binary_search import left_binary_search


@pytest.mark.parametrize(
    (),
    [],
)
def test_A_left_binary_search():

    assert left_binary_search() == ...
