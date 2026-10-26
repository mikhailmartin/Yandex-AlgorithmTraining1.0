import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.I_subbotnik.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "8 2 3",
                "170", "205", "225", "190", "260", "130", "225", "160",
            ],
            30,
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
