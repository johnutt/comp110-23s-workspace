"""Exercise 5 Tests!"""

__author__ = "730579193"

from exercises.utils import only_evens
from exercises.utils import sub
from exercises.utils import concat


def test_empty_only_evens()-> None:
    """Tests the only_evens function when the input is an empty list"""
    test_list: list[int] = []
    only_evens(test_list)
    assert only_evens(test_list) == []



def test_only_evens_with_negatives()-> None:
    """Tests the only_evens function when the input has negatives"""
    test_list: list[int] = [2,-2,-6]
    assert only_evens(test_list) == [2, -2, -6]



def test_only_evens_with_one()-> None:
    """Tests the only_evens function when the input is a list with odd and even integers"""
    test_list: list[int] = [2, 3, 5, 6, 4, 8]
    assert only_evens(test_list) == [2,6,4,8]





