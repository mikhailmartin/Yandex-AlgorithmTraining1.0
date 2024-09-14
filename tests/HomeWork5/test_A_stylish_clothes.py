import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork5.A_stylish_clothes import main


@pytest.mark.parametrize(
    ("n", "shirts", "m", "pants", "expected"),
    [
        param(2, [3, 4], 3, [1, 2, 3], (3, 3)),
        param(2, [4, 5], 3, [1, 2, 3], (4, 3)),
        param(5, [1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5], (1, 1)),
        param(1, [10], 10, [1, 3, 8, 11, 13, 20, 25, 100, 1000, 100000], (10, 11)),
        param(10, [8, 16, 76, 116, 311, 413, 826, 838, 939, 944], 10, [22, 85, 229, 286, 453, 475, 487, 744, 784, 883], (16, 22)),
    ],
)
def test_A(n, shirts, m, pants, expected):

    assert main(n, shirts, m, pants) == expected
