"""Example functions to learn definition and syntax"""

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of 2 numbers"""
    if number1 >= number2:
        return "hello"
    else: #number1 < number2
        return number2

max_number: int = my_max(3,10)
print(max_number)
other_max_number: int = my_max(11,3)
print(other_max_number)