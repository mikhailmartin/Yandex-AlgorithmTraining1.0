import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork8.I_genealogy_number_of_descendants import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "9",
                "Alexei Peter_I",
                "Anna Peter_I",
                "Elizabeth Peter_I",
                "Peter_II Alexei",
                "Peter_III Anna",
                "Paul_I Peter_III",
                "Alexander_I Paul_I",
                "Nicholaus_I Paul_I",
            ],
            [
                ("Alexander_I", 0),
                ("Alexei", 1),
                ("Anna", 4),
                ("Elizabeth", 0),
                ("Nicholaus_I", 0),
                ("Paul_I", 2),
                ("Peter_I", 8),
                ("Peter_II", 0),
                ("Peter_III", 3),
            ],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
