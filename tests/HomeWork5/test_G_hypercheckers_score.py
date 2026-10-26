import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.G_hypercheckers_score.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["5 2", "1 1 2 2 3"], 9, id="example1"),
        param(["8 99", "100 99 2 1 100 99 2 1"], 42, id="test14"),
        param(["100000 1", " ".join(["100000"] * 100_000)], 1, id="test30"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
