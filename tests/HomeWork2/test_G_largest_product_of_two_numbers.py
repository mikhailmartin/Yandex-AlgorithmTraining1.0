import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.G_largest_product_of_two_numbers.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4 3 5 2 5"], (5, 5)),
        param(["-4 3 -5 2 5"], (-5, -4)),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
