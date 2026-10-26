import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.B_sum_of_numbers.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["5 17", "17 7 10 7 10"], 4),
        param(["5 10", "1 2 3 4 1"], 2),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
