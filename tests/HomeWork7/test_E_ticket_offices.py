import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.E_ticket_offices import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "1 0 23 0",
                "12 0 12 0",
                "22 0 2 0",
            ],
            120,
            id="example1"
        ),
        param(
            [
                "2",
                "9 30 14 0",
                "14 15 21 0",
            ],
            0,
            id="example2",
        ),
        param(
            [
                "2",
                "14 00 18 00",
                "10 00 14 01",
            ],
            1,
            id="example3",
        ),
        param(
            [
                "1",
                "17 35 17 35",
            ],
            1440,
            id="test5",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
