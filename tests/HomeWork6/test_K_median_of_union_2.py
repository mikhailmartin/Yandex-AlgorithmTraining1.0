import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.K_median_of_union_2 import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3 6",
                "1 3 1 0 5",
                "0 2 1 1 100",
                "1 6 8 5 11",
            ],
            [7, 10, 9],
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
