import sys
sys.path.append("..")

import pytest
from pytest import param
from F_arangment_of_laptops import main


@pytest.mark.parametrize(
    ("a1", "b1", "a2", "b2", "expected"),
    [
        param(10, 2, 2, 10, (10, 4)),
        param(5, 7, 3, 2, (9, 5)),
        param(3, 2, 5, 7, (9, 5)),
    ],
)
def test_F_arangment_of_laptops(a1, b1, a2, b2, expected):

    assert main(a1, b1, a2, b2) == expected
