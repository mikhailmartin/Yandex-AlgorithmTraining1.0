import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.J_system_of_linear_equations_2.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1", "0", "0", "1", "3", "3"], "2 3.0 3.0"),
        param(["1", "1", "2", "2", "1", "2"], "1 -1.0 1.0"),
        param(["0", "2", "0", "4", "1", "2"], "4 0.5"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
