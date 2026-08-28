import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.D_Advertisement_alt import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4",
                "1 11",
                "1 3",
                "6 15",
                "1 6",
            ],
            (3, 1, 6),
            id="test1"
        ),
        param(
            [
                "1",
                "1 10",
            ],
            (1, 1, 6),
            id="test2",
        ),
        param(
            [
                "3",
                "1 10",
                "11 20",
                "21 30",
            ],
            (2, 1, 11),
            id="test3",
        ),
        param(
            [
                "2",
                "1 6",
                "2 20",
            ],
            (2, 1, 15),
            id="test7",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
