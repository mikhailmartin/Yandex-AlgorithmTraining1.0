import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.J_triangles.main import main, get_symmetric


def test_J_get_symmetric():
    assert get_symmetric((1, 1), (0, 0)) == (-1, -1)
    assert get_symmetric((-1, 1), (0, 0)) == (1, -1)


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3", "0 0", "2 2", "-2 2"], 1, id="example1"),
        param(["4", "0 0", "1 1", "1 0", "0 1"], 4, id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
