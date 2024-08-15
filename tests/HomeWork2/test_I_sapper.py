import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork2.I_sapper import main


@pytest.mark.parametrize(
    ("n", "m", "mines", "expected"),
    [
        param(3, 2, [(1, 1), (2, 2)], "* 2\n2 *\n1 1"),
        param(2, 2, [], "0 0\n0 0"),
        param(4, 4, [(1, 3), (2, 1), (4, 2), (4, 4)], "1 2 * 1\n* 2 1 1\n2 2 2 1\n1 * 2 *")
    ],
)
def test_I_sapper(n, m, mines, expected):

    assert main(n, m, mines) == expected
