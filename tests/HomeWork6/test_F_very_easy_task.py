import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.F_very_easy_task.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4 1 1"], 3, id="example1"),
        param(["5 1 2"], 4, id="example2"),
        param(["34854 4 3"], 59751, id="test7"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
