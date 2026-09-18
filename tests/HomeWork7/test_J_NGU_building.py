import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.J_NGU_building import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "1 10 10",
                "0 0 0 10 10 10",
            ],
            [1],
            id="example1"
        ),
        param(
            [
                "2 10 10",
                "0 0 0 10 5 5",
                "0 5 5 10 10 10",
            ],
            [],
            id="example2"
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
