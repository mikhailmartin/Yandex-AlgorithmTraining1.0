import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork2.F_symmetric_sequence import find_index_start_palindrome, main


@pytest.mark.parametrize(
    ("sequence", "expected"),
    [
        param([1], 0),
        param([1, 2, 1], 0),
        param([1, 2, 2, 1], 0),
        param([1, 2, 3, 2, 1], 0),
        param([1, 2], 1),
        param([1, 2, 3], 2),
        param([1, 2, 3, 2], 1),
        param([1, 2, 3, 4, 5, 4, 3, 2, 1], 0),
        param([1, 2, 1, 2, 2], 3),
        param([1, 2, 3, 4, 5], 4),
    ],
)
def test_F_find_index_start_palindrome(sequence, expected):

    assert find_index_start_palindrome(sequence) == expected


@pytest.mark.parametrize(
    ("sequence", "expected"),
    [
        param([1], (0, "")),
        param([1, 2, 1], (0, "")),
        param([1, 2, 2, 1], (0, "")),
        param([1, 2, 3, 2, 1], (0, "")),
        param([1, 2], (1, "1")),
        param([1, 2, 3], (2, "2 1")),
        param([1, 2, 3, 2], (1, "1")),
        param([1, 2, 3, 4, 5, 4, 3, 2, 1], (0, "")),
        param([1, 2, 1, 2, 2], (3, "1 2 1")),
        param([1, 2, 3, 4, 5], (4, "4 3 2 1")),
    ],
)
def test_F_main(sequence, expected):

    assert main(sequence) == expected
