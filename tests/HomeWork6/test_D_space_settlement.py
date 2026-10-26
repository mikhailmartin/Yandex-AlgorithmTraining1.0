import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.D_space_settlement.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 1 1 1 1"], 0, id="example1"),
        param(["1 1 1 3 3"], 1, id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
