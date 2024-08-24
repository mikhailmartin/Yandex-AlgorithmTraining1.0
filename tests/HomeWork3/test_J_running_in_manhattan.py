import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork3.J_running_in_manhattan import main


@pytest.mark.parametrize(
    ("t", "d", "navigator_points", "expected"),
    [
        param(2, 1, [(0, 1)], [(0, 0), (0, 1), (0, 2), (1, 1), (-1, 1)]),
        param(2, 1, [(0, 1), (-2, 1), (-2, 3), (0, 3), (2, 5)], [(1, 5), (2, 4)]),
    ],
)
def test_J(t, d, navigator_points, expected):

    assert set(main(t, d, navigator_points)) == set(expected)
