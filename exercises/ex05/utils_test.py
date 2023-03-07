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



def test_concat_with_two_positive_lists()-> None:
    """Tests the concat function with two positive lists"""
    test_list1: list[int] = [2,3,4]
    test_list2: list[int] = [3,2,5]
    assert concat(test_list1, test_list2) == [2,3,4,3,2,5]



def test_concat_with_empty_lists()-> None:
    """Tests the concat function with empty lists"""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_concat_with_neg_and_pos_numbers()-> None:
    """Tests the concat function with lists including negatives and positives"""
    test_list1: list[int] = [2,3,-1]
    test_list2: list[int] = [-2,5,-3]
    assert concat(test_list1, test_list2) == [2,3,-1,-2,5,-3]



def test_sub_with_postives()-> None:
    """Tests the sub function with only positive integers"""
    test_list1: list[int] = [2,3,5,7,2,5,7]
    sidx: int = 1
    eidx: int = 4
    assert sub(test_list1, sidx, eidx) == [3,5,7]



def test_sub_with_empty_list()-> None:
    """Tests the sub function with an empty list"""
    test_list1: list[int] = []
    sidx: int = 1
    eidx: int = 4
    assert sub(test_list1, sidx, eidx) == []



def test_sub_with_pos_and_neg()-> None:
    """Tests the sub function with a list including positive and negatives"""
    test_list1: list[int] = [5,3,-2,-1,-5,9,7]
    sidx: int = 1
    eidx: int = 6
    assert sub(test_list1, sidx, eidx) == [3,-2,-1,-5,9]