"""Functions For Exercise07!"""
__author__ = 730579193


def invert(input: dict[str, str]) -> dict[str, str]:
    """Reverses a dictionary's keys and values."""
    output: dict[str, str] = {}
    
    for x in input:
        count: int = 0 
        for y in input:
            if input[x] == input[y]:
                count += 1
        if count > 1:    
            raise KeyError("Dictionaries should have unique keys!")
    for x in input:
        output[input[x]] = x
    return output    


def favorite_color(input: dict[str, str]) -> str:
    """Finds the most prevalent value in a dictionary."""
    output: dict[int] = {}
    for x in input:
        count: int = 0 
        for y in input:
            if input[x] == input[y]:
                count += 1
        color: str = input[x]
        output[color] = count

    current_max: int = 0
    current_max_str: str = ""
    for x in output:
        if output[x] > current_max:
            current_max = output[x]
            current_max_str = x
            
    return current_max_str


def count(input: list[str]) -> dict[str, int]:
    """Counts the amount of string values in a list."""
    output: dict[str, int] = {}
    for x in input:
        current: str = x
        if current in output:
            output[x] += 1
        else:
            output[x] = 1
    return output