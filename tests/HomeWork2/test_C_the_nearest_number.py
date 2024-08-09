import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork2.C_the_nearest_number import find_nearest_number


@pytest.mark.parametrize(
    ("lst", "x", "expected"),
    [
        param([1, 2, 3, 4, 5], 6, 5),
        param([5, 4, 3, 2, 1], 3, 3),
    ],
)
def test_C_the_nearest_number(lst, x, expected):

    assert find_nearest_number(lst, x) == expected
