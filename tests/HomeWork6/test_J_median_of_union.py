import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.J_median_of_union import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3 6",
                "1 4 7 10 13 16",
                "0 2 5 9 14 20",
                "1 7 16 16 21 22",
            ],
            [7, 10, 9],
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
