import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.I_robot import main


@pytest.mark.parametrize(
    ("k", "operations", "expected"),
    [
        param(2, "zabacabab", 5),  # тест 1
        param(2, "abc", 0),  # тест 2
        param(1, "abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabac", 0),  # тест 4
    ],
)
def test_I_main(k, operations, expected):

    assert main(k, operations) == expected
