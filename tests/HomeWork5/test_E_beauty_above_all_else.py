import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork5.E_beauty_above_all_else import main


@pytest.mark.parametrize(
    ("n", "k", "trees", "expected"),
    [
        param(5, 3, [1, 2, 1, 3, 2], (2, 4)),
        param(6, 4, [2, 4, 2, 3, 3, 1], (2, 6)),
        param(12, 5, [5, 1, 1, 2, 2, 4, 4, 4, 3, 2, 1, 5], (8, 12)),
    ],
)
def test_E(n, k, trees, expected):

    assert main(n, k, trees) == expected
