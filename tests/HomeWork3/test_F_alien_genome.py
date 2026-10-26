import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.F_alien_genome.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["ABBACAB", "BCABB"], 4),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
