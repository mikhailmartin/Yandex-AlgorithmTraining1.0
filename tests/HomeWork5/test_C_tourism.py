import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.C_tourism.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "7",
                "2 1",
                "4 5",
                "7 4",
                "8 2",
                "9 6",
                "11 3",
                "15 3",
                "1",
                "2 6",
            ],
            [4],
            id="example1",
        ),
        param(
            [
                "6",
                "1 1",
                "3 2",
                "5 6",
                "7 2",
                "10 4",
                "11 1",
                "3",
                "5 6",
                "1 4",
                "4 2",
            ],
            [0, 5, 4],
            id="example2",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
