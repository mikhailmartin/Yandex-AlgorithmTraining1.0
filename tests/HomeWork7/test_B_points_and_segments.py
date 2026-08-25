import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.B_points_and_segments import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3 2",
                "0 5",
                "-3 2",
                "7 10",
                "1 6",
            ],
            [2, 0],
            id="test1"
        ),
        param(
            [
                "1 3",
                "-10 10",
                "-100 100 0",
            ],
            [0, 0, 1],
            id="test2",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
