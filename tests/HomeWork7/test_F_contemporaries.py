import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.F_contemporaries import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "2 5 1988 13 11 2005",
                "1 1 1 1 1 30",
                "1 1 1910 1 1 1990",
            ],
            [frozenset([2]), frozenset([3])],
            id="example1"
        ),
        param(
            [
                "3",
                "2 5 1968 13 11 2005",
                "1 1 1 1 1 30",
                "1 1 1910 1 1 1990",
            ],
            [frozenset([2]), frozenset([1, 3])],
            id="example2",
        ),
        param(
            [
                "3",
                "2 5 1988 13 11 2005",
                "1 1 1 1 1 10",
                "2 1 1910 1 1 1928",
            ],
            [frozenset([0])],
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
