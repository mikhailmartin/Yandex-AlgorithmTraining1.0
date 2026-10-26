import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.G_turtles.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3", "2 0", "0 2", "2 2"], 2),
        param(["5", "0 4", "1 3", "2 2", "3 1", "4 0"], 5),
        param(
            [
                "10",
                "9 1",
                "8 1",
                "7 2",
                "6 2",
                "5 3",
                "4 4",
                "3 6",
                "2 7",
                "1 9",
                "0 8",
            ],
            4,
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
