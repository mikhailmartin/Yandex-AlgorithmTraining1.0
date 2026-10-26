import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.H_largest_product_of_three_numbers.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3 5 1 7 9 0 9 -3 10"], (10, 9, 9)),
        param(["-5 -30000 -12"], (-5, -12, -30000)),
        param(["1 2 3"], (3, 2, 1)),
    ]
)
def test_main(lines, expected):
    assert main(lines) == expected
