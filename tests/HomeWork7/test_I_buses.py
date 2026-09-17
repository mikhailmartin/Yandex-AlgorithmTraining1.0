import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.I_buses import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "2 2",
                "2 20:00 1 10:00",
                "1 08:00 2 21:00",
            ],
            3,
            id="example1"
        ),
        param(
            [
                "2 2",
                "1 09:00 2 20:00",
                "2 20:00 1 09:00",
            ],
            1,
            id="example2"
        ),
        param(
            [
                "3 4",
                "3 03:52 1 08:50",
                "1 18:28 3 21:53",
                "2 03:58 3 09:00",
                "3 14:59 2 21:13",
            ],
            2,
            id="example3"
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
