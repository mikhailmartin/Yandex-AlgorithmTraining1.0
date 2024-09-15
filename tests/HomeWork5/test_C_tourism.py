import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork5.C_tourism import main


@pytest.mark.parametrize(
    ("n", "mountain_chain", "tracks", "expected"),
    [
        param(7, [(2, 1), (4, 5), (7, 4), (8, 2), (9, 6), (11, 3), (15, 3)], [(2, 6)], [4]),
        param(6, [(1, 1), (3, 2), (5, 6), (7, 2), (10, 4), (11, 1)], [(5, 6), (1, 4), (4, 2)], [0, 5, 4]),
    ],
)
def test_C(n, mountain_chain, tracks, expected):

    assert main(n, mountain_chain, tracks) == expected
