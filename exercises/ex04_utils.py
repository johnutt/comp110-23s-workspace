"""Exercise 04: Lists!"""
__author__ = "730579193"


def all(input: list[int], number: int) -> bool:
    """Determines if a single number composes a list!"""
    all_idx: int = 0
    if len(input) == 0:
        return False
    while all_idx < len(input):
        if input[all_idx] != number:
            return False
        all_idx += 1
    return True


def max(input: list[int]) -> int:
    """Determines the max integer in a list!"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_idx: int = 0
    current_max = int(input[0])
    while max_idx < len(input):
        if current_max < input[max_idx]:
            current_max = int(input[max_idx])
        max_idx += 1
    return current_max


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Determines if 2 lists are equal!"""
    ie_idx: int = 0
    if len(input1) != len(input2):
        return False
    while ie_idx < len(input1):
        if input1[ie_idx] != input2[ie_idx]:
            return False
        ie_idx += 1
    return True