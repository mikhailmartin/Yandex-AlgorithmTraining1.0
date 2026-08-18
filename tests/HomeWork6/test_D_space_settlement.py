import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.D_space_settlement import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["1 1 1 1 1"],
            0,
        ),
        param(
            ["1 1 1 3 3"],
            1,
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
