import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork2.B_identify_sequence_type import identify_sequence_type


@pytest.mark.parametrize(
    ("sequence", "expected"),
    [
        param([-530, -530, -530, -530, -530, -530], "CONSTANT"),
        param([1, 2, 3, 4, 5, 6], "ASCENDING"),
        param([1, 2], "ASCENDING"),
        param([1, 2, 2, 3, 3, 4], "WEAKLY ASCENDING"),
        param([6, 5, 4, 3, 2, 1], "DESCENDING"),
        param([6, 5], "DESCENDING"),
        param([6, 5, 5, 5, 1, 1], "WEAKLY DESCENDING"),
        param([1, 3, 2, 6, 4, 5], "RANDOM"),
        param([], "RANDOM"),
        param([1], "RANDOM"),
    ],
)
def test_B_identify_sequence_type(sequence, expected):

    assert identify_sequence_type(sequence) == expected
