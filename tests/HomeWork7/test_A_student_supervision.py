import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.A_student_supervision import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "10 3",
                "1 3",
                "2 4",
                "9 9",
            ],
            5,
            id="example1",
        ),
        param(
            [
                "10 2",
                "1 1",
                "1 2",
            ],
            8,
            id="example2",
        ),
        param(
            [
                "2 1",
                "0 0",
            ],
            1,
            id="custom1"
        ),
        param(
            [
                "2 1",
                "1 1",
            ],
            1,
            id="custom2"
        ),
        param(
            [
                "2 1",
                "0 1",
            ],
            0,
            id="custom3"
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
