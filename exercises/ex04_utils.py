"""Exercise 04: Lists"""
__author__ = "730579193"

def all(input: list[int](), number: int) -> bool:
    all_idx: int = 0

    while all_idx < len(input):
        if input[all_idx] == number:
            return True
        all_idx += 1
    return False



def max(input: list[int]()) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_idx: int = 0
    current_max = input[0]
    while max_idx < len(input):
        if current_max < input[max_idx]:
            current_max = input[max_idx] 
        max_idx += 1
    return current_max

def is_equal(input1: list(), input2: list()) -> bool:
    ie_idx: int = 0
    if len(input1) != len(input2):
        return False
    while ie_idx < len(input1):
        if input1[ie_idx] != input2[ie_idx]:
            return False
        ie_idx += 1
    return True

