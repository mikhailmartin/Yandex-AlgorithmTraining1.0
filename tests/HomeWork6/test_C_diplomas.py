import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.C_diplomas.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["2 3 10"], 9, id="example"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
