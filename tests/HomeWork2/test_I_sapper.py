import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.I_sapper.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3 2 2", "1 1", "2 2"], "* 2\n2 *\n1 1"),
        param(["2 2 0"], "0 0\n0 0"),
        param(["4 4 4", "1 3", "2 1", "4 2", "4 4"], "1 2 * 1\n* 2 1 1\n2 2 2 1\n1 * 2 *")
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
