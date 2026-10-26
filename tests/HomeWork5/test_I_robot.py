import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.I_robot.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["2", "zabacabab"], 5, id="example1"),
        param(["2", "abc"], 0, id="example2"),
        param(["1", "abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabac"], 0, id="test4"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
