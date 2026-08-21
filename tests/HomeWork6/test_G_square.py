import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.G_square import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["6", "7", "38"],
            2,
            id="тест 1",
        ),
        param(
            ["1600000000", "1450000000", "2310000003500000805"],
            700000007,
            id="тест 17",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
