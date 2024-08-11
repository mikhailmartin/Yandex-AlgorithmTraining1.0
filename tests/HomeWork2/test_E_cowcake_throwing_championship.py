import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork2.E_cowcake_throwing_championship import (
    find_best_Vasya_place, find_left_winner_index, find_best_Vasya_result
)


@pytest.mark.parametrize(
    ("results", "expected"),
    [
        param([10, 20, 15, 10, 30, 5, 1], 6),
        param([15, 15, 10], 1),
        param([10, 15, 20], 0),
        # param([], 0),
        # param([1, 1, 1], 0),
        # param([5, 5, 5], 0),
        # param([5, 5, 6], 0),
    ],
)
def test_E_find_best_Vasya_place(results, expected):

    assert find_best_Vasya_place(results) == expected


@pytest.mark.parametrize(
    ("results", "expected"),
    [
        param([10, 20, 15, 10, 30, 5, 1], 4),
        param([15, 15, 10], 0),
        param([10, 15, 20], 2),
    ],
)
def test_E_find_left_winner_index(results, expected):

    assert find_left_winner_index(results) == expected


@pytest.mark.parametrize(
    ("results", "left_winner_index", "expected"),
    [
        param([10, 20, 15, 10, 30, 5, 1], 4, 5),
        param([15, 15, 10], 0, 15),
        param([10, 15, 20], 2, float("-inf")),
    ],
)
def test_E_find_best_Vasya_result(results, left_winner_index, expected):

    assert find_best_Vasya_result(results, left_winner_index) == expected
