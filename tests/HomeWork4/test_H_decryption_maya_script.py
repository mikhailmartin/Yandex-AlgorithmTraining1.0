import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.H_decryption_maya_script.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4 11", "cAda", "AbrAcadAbRa"], 2),
        param(["3 100", "OOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"], 98),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
