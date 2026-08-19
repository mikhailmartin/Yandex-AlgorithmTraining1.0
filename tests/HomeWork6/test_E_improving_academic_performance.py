import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.E_improving_academic_performance import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "2",
                "0",
                "0",
            ],
            2,
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
