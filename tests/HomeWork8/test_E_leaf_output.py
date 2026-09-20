import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork8.E_leaf_output import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["7 3 2 1 9 5 4 6 8 0"],
            [1, 4, 6, 8],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
