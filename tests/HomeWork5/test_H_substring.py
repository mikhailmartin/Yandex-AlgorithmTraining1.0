import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.H_substring.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3 1", "abb"], (2, 1), id="example1"),
        param(["5 2", "ababa"], (4, 1), id="example2"),
        param(["10 10", "aaaaaaaaaa"], (10, 1), id="test3"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
