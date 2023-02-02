"""Exercise 2: One Shot Wordle!"""

__author__ = "730579193"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
index: int = 0
result: str = ""
alt_index: int = 0

while len(guess) != len(secret_word):
    guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")

if len(guess) == len(secret_word) and guess != secret_word:

    while index != len(secret_word):

        if guess[index] != secret_word[index]: 
            
            found_in_word: bool = False 
            
            while found_in_word is False and alt_index != len(secret_word):
                if secret_word[alt_index] == guess[index]:
                    result = str(f"{result}\U0001F7E8")
                    found_in_word = True
                alt_index = alt_index + 1
            alt_index = 0
            
            if found_in_word is False: 
                result = str(f"{result}\U00002B1C")
        
        if guess[index] == secret_word[index]:
            result = str(f"{result}\U0001F7E9")
    
        index = index + 1
    
    print(result)
    print("Not quite. Play again soon!")

if guess == secret_word:
    print("\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9")
    print("Woo! You got it!")