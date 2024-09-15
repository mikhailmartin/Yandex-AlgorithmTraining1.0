import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork5.B_sum_of_numbers import main


@pytest.mark.parametrize(
    ("n", "k", "nums", "expected"),
    [
        param(5, 17, [17, 7, 10, 7, 10], 4),
        param(5, 10, [1, 2, 3, 4, 1], 2),
    ],
)
def test_B(n, k, nums, expected):

    assert main(n, k, nums) == expected
