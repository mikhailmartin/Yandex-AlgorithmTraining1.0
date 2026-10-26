import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.D_che_city.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4 4", "1 3 5 8"], 2),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
