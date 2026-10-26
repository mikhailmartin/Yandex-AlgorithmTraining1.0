import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.J_Maxim_triangle.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["3", "440", "220 closer", "300 further"],
            (30., 260.),
            id="example1",
        ),
        param(
            ["4", "554", "880 further", "440 closer", "622 closer"],
            (531., 660.),
            id="example2",
        ),
        param(["1", "400"], (30., 4000.), id="custom1"),
        param(
            [
                "6",
                "3072.7508920475825",
                "3087.2740875071913 further",
                "2376.1007719516238 further",
                "2376.1007719516238 further",
                "3719.8803250966535 further",
                "1575.5506732924753 further",
            ],
            (2731.6874297294075, 3047.990548524139),
            id="test",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
