"""Exercise 5!"""

__author__ = "730579193"


def only_evens(inputs: list[int]) -> list[int]:
    """Returns only the even numbers in a set!"""
    idx: int = 0
    result: list[int] = []
    while idx < len(inputs):
        if inputs[idx] % 2 == 0:
            result.append(inputs[idx])
        idx += 1
    return result


def concat(input1: list[int], input2: list[int]) -> list[int]:
    """Combines two sets of numbers!"""
    result: list[int] = []
    idx1: int = 0
    idx2: int = 0
    while idx1 < len(input1):
        result.append(input1[idx1])
        idx1 += 1
    while idx2 < len(input2):
        result.append(input2[idx2])
        idx2 += 1
    return result


def sub(input: list[int], sidx: int, eidx: int) -> list[int]:
    """Determines the numbers within a given range of a set!"""
    result: list[int] = []
    if sidx < 0:
        sidx = 0
    if eidx > len(input) - 1:
        eidx = len(input)
    if len(input) == 0 or sidx >= len(input) - 1 or eidx <= 0:
        return result
    while sidx < eidx:
        result.append(input[sidx])
        sidx += 1
    return result