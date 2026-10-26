import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.F_conditioners.main import main, preprocessed


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1", "800", "1", "800 1000"], 1000),
        param(["3", "1 2 3", "4", "1 10", "1 5", "10 7", "2 3"], 13),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected


@pytest.mark.parametrize(
    ("power_price", "expected"),
    [
        param([(800, 1000)], [(800, 1000)]),
        param([(1, 10), (1, 5), (10, 7), (2, 3)], [(1, 3), (2, 3), (10, 7)])
    ],
)
def test_F_preprocessed(power_price, expected):
    assert preprocessed(power_price) == expected
