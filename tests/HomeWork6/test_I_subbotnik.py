import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.I_subbotnik import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "8 2 3",
                "170", "205", "225", "190", "260", "130", "225", "160",
            ],
            30,
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
