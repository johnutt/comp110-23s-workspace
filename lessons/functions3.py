
def mimic(my_words: str, letter_idx: int) -> str:
    """"Outputs the character of my_words at index letter_idx"""
    if letter_idx > len(my_words) - 1:
        return
    else:
        return my_words[letter_idx]

response: str = mimic("hello",3)
print(response)
