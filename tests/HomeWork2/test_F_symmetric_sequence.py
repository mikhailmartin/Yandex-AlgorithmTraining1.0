import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.F_symmetric_sequence.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1", "1"], []),
        param(["3", "1 2 1"], []),
        param(["4", "1 2 2 1"], []),
        param(["5", "1 2 3 2 1"], []),
        param(["2", "1 2"], [1]),
        param(["3", "1 2 3"], [2, 1]),
        param(["4", "1 2 3 2"], [1]),
        param(["9", "1 2 3 4 5 4 3 2 1"], []),
        param(["5", "1 2 1 2 2"], [1, 2, 1]),
        param(["5", "1 2 3 4 5"], [4, 3, 2, 1]),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
