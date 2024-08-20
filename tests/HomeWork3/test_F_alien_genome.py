import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork3.F_alien_genome import get_proximity


@pytest.mark.parametrize(
    ("firt_genome", "second_genome", "expected"),
    [
        param("ABBACAB", "BCABB", 4)
    ],
)
def test_F_get_proximity(firt_genome, second_genome, expected):

    assert get_proximity(firt_genome, second_genome) == expected
