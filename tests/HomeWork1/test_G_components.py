import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.G_components.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["10 5 2"], 4),
        param(["13 5 3"], 3),
        param(["14 5 3"], 4),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
