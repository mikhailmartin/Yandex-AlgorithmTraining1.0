import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.H_substring import main


@pytest.mark.parametrize(
    ("k", "string", "expected"),
    [
        param(1, "abb", (2, 1)),  # тест 1
        param(2, "ababa", (4, 1)),  # тест 2
        param(10, "aaaaaaaaaa", (10, 1)),  # тест 3
    ],
)
def test_H_main(k, string, expected):

    assert main(k, string) == expected
