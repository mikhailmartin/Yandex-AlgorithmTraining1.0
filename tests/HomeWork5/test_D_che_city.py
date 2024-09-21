import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork5.D_che_city import main


@pytest.mark.parametrize(
    ("n", "r", "monuments", "expected"),
    [
        param(4, 4, [1, 3, 5, 8], 2),
    ],
)
def test_D(n, r, monuments, expected):

    assert main(n, r, monuments) == expected
