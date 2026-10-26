import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.J_running_in_manhattan.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "2 1 5",
                "0 1",
                "-2 1",
                "-2 3",
                "0 3",
                "2 5",
            ],
            [(1, 5), (2, 4)],
        ),
        param(
            ["1 1 1", "0 0"],
            [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)],
        ),
        param(
            ["1 10 1", "0 0"],
            [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)],
        ),
    ],
)
def test_main(lines, expected):
    assert set(main(lines)) == set(expected)
