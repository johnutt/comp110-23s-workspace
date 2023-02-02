"""Exercise 2: One Shot Wordle"""

__author__ = "730579193"

secret_word: str = "python"
word: str = input(f"What is your {len(secret_word)}-letter guess? ")
index: int = 0
result: str = ""
alt_index: int = 0

while len(word) != len(secret_word):
    word: str = input(f"That was not {len(secret_word)} letters! Try again: ")

if len(word) == len(secret_word) and word != secret_word:

    while index != len(secret_word):

        if word[index] != secret_word[index]: 
            
            found_in_word: bool = False 
            
            while found_in_word == False and alt_index != len(secret_word):
                if secret_word[alt_index] == word[index]:
                    result = str(f"{result}\U0001F7E8")
                    found_in_word = True
                alt_index = alt_index + 1
            alt_index = 0
            
            if found_in_word == False: 
                result = str(f"{result}\U00002B1C")
        
        if word[index] == secret_word[index]:
            result = str(f"{result}\U0001F7E9")
    
        index = index + 1
    
    print(result)
    print(f"Not quite. Play again soon!")


if word == secret_word:
    print(f"\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9")
    print(f"Woo! You got it!")

 
    

