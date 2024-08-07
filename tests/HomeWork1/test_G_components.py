import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.G_components import recursive, not_recursive


@pytest.mark.parametrize(
    ("n", "k", "m", "expected"),
    [
        param(10, 5, 2, 4),
        param(13, 5, 3, 3),
        param(14, 5, 3, 4),
    ],
)
def test_G_components_recursive(n, k, m, expected):

    assert recursive(n, k, m) == expected


@pytest.mark.parametrize(
    ("n", "k", "m", "expected"),
    [
        param(10, 5, 2, 4),
        param(13, 5, 3, 3),
        param(14, 5, 3, 4),
    ],
)
def test_G_components_not_recursive(n, k, m, expected):

    assert not_recursive(n, k, m) == expected
