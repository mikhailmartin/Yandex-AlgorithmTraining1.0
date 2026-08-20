import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.F_very_easy_task import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4 1 1"], 3, id="тест 1"),
        param(["5 1 2"], 4, id="тест 2"),
        param(["34854 4 3"], 59751, id="тест 7"),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
