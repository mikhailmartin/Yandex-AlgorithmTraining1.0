import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.A_is_ascending.main import main


STOP = -2_000_000_000


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["-530", "-530", "-530", "-530", "-530", "-530", STOP],
            "YES",
            id="example1",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
