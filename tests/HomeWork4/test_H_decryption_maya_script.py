import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork4.H_decryption_maya_script import main


@pytest.mark.parametrize(
    ("len_word", "len_string", "word", "string", "expected"),
    [
        param(4, 11, "cAda", "AbrAcadAbRa", 2),
        param(3, 100, "OOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", 98),
    ],
)
def test_H(len_word, len_string, word, string, expected):

    assert main(len_word, len_string, word, string) == expected
