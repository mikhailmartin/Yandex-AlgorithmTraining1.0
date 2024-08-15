import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork2.J_Maxim_triangle import main


@pytest.mark.parametrize(
    ("previous_frequency", "frequencies_answers", "expected"),
    [
        param(440, [(220, "closer"), (300, "further")], (30., 260.)),
        param(554, [(880, "further"), (440, "closer"), (622, "closer")], (531., 660.)),
        param(400, [], (30., 4000.)),
        param(3072.7508920475825, [(3087.2740875071913, "further"), (2376.1007719516238, "further"), (2376.1007719516238, "further"), (3719.8803250966535, "further"), (1575.5506732924753, "further")], (2731.6874297294075, 3047.990548524139)),
    ],
)
def test_J_Maxim_triangle(previous_frequency, frequencies_answers, expected):

    assert main(previous_frequency, frequencies_answers) == expected
