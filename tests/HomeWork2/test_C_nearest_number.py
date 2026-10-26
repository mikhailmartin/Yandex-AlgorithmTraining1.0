import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.C_nearest_number.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["5", "1 2 3 4 5", "6"], 5),
        param(["5", "5 4 3 2 1", "3"], 3),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
