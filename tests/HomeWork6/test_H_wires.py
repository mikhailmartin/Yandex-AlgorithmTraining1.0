import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.H_wires.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4 11",
                "802", "743", "457", "539",
            ],
            200,
            id="example",
        ),
        param(
            [
                "7 13",
                "3318", "5775", "7318", "336", "9490", "5712", "2379",
            ],
            2372,
            id="test3",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
