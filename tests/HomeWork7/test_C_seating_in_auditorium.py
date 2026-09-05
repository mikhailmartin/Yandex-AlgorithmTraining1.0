import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.C_seating_in_auditorium import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4 1",
                "11 1 12 2",
            ],
            (2, [1, 1, 2, 2]),
            id="example1"
        ),
        param(
            [
                "4 0",
                "11 1 12 2",
            ],
            (1, [1, 1, 1, 1]),
            id="example2"
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
