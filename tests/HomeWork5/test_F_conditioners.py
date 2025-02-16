import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.F_conditioners import preprocessed, main


@pytest.mark.parametrize(
    ("powers", "power_price", "expected"),
    [
        param([800], [(800, 1000)], 1000),
        param([1, 2, 3], [(1, 10), (1, 5), (10, 7), (2, 3)], 13),
    ],
)
def test_F_main(powers, power_price, expected):

    assert main(powers, power_price) == expected


@pytest.mark.parametrize(
    ("power_price", "expected"),
    [
        param([(800, 1000)], [(800, 1000)]),
        param([(1, 10), (1, 5), (10, 7), (2, 3)], [(1, 3), (2, 3), (10, 7)])
    ],
)
def test_F_preprocessed(power_price, expected):

    assert preprocessed(power_price) == expected
