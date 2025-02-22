import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.G_hypercheckers_score import main


@pytest.mark.parametrize(
    ("k", "numbers", "expected"),
    [
        param(2, [1, 1, 2, 2, 3], 9),  # тест 1
        param(99, [100, 99, 2, 1, 100, 99, 2, 1], 42),  # тест 14
        param(1, [100_000] * 100_000, 1),  # тест 30
    ],
)
def test_G_main(k, numbers, expected):

    assert main(k, numbers) == expected
