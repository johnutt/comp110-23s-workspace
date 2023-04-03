"""Challenge question 04!"""

__author__ = "730579193"


def zip(input1: list[str], input2: list[int]) -> dict[str, int]:
    """Makes a dictionary out of two lists!"""
    output: dict[str, int] = {}
    idx: int = 0
    if len(input1) != len(input2):
        return output
    if input1 == () or input2 == ():
        return output
    for elem in input1:
        output[elem] = input2[idx]
        idx += 1
    return output

