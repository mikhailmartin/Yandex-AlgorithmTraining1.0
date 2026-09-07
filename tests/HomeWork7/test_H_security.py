import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.H_security import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "2",
                "3 0 3000 2500 7000 2700 10000",
                "2 0 3000 2700 10000",
            ],
            ["Wrong Answer", "Accepted"],
            id="example1"
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
