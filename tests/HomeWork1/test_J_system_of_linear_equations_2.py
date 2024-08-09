import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.J_system_of_linear_equations_2 import main


@pytest.mark.parametrize(
    ("a", "b", "c", "d", "e", "f", "expected"),
    [
        param(1, 0, 0, 1, 3, 3, "2 3.0 3.0"),
        param(1, 1, 2, 2, 1, 2, "1 -1.0 1.0"),
        param(0, 2, 0, 4, 1, 2, "4 0.5"),
    ],
)
def test_J_systemm_of_linear_equations_2(a, b, c, d, e, f, expected):

    assert main(a, b, c, d, e, f) == expected
