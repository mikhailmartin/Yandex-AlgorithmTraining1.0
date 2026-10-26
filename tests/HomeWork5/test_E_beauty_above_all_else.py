import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.E_beauty_above_all_else.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["5 3", "1 2 1 3 2"], (2, 4)),
        param(["6 4", "2 4 2 3 3 1"], (2, 6)),
        param(["12 5", "5 1 1 2 2 4 4 4 3 2 1 5"], (8, 12)),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
