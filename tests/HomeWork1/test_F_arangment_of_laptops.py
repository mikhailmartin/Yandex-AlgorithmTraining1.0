import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.F_arangment_of_laptops.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["10 2 2 10"], (10, 4)),
        param(["5 7 3 2"], (9, 5)),
        param(["3 2 5 7"], (9, 5)),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
