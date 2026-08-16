import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.B_approximate_binary_search import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5 5",
                "1 3 5 7 9",
                "2 4 8 1 6",
            ],
            [1, 3, 7, 1, 5],
        ),
        param(
            [
                "6 11",
                "1 1 4 4 8 120",
                "1 2 3 4 5 6 7 8 63 64 65",
            ],
            [1, 1, 4, 4, 4, 4, 8, 8, 8, 8, 120],
        ),
        param(
            [
                "10 10",
                "-5 1 1 3 5 5 8 12 13 16",
                "0 3 7 -17 23 11 0 11 15 7",
            ],
            [1, 3, 8, -5, 16, 12, 1, 12, 16, 8],
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
