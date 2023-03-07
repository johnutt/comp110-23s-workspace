"""Exercise 3: Structured Wordle"""
__author__ = "730579193"


def contains_char(word: str, char: str) -> bool:
    """Determines whether or not a word contains a specific character"""
    assert len(char) == 1
    idx_cc: int = 0
    found_in_word: bool = False

    while idx_cc < len(word):
        idx_cc2: int = 0
        if word[idx_cc] == char:
            found_in_word = True
        idx_cc = idx_cc + 1
    
    if found_in_word == True:
        return True
    else:
        return False


def emojified(secret: str, word: str) -> str:
    """Updates the result of the guess"""
    assert len(secret) == len(word)
    
    result: str = ""
    idx_e: int = 0
    correct_letter: bool = False

    while idx_e < len(word):
        correct_letter = False
        if contains_char(secret, word[idx_e]) is False:
            result = f"{result}\U00002B1C"
        if contains_char(secret, word[idx_e]) is True: 
            if word[idx_e] == secret[idx_e]:
                result = f"{result}\U0001F7E9"
                correct_letter = True
            else:
                result = f"{result}\U0001F7E8"
            
        idx_e = idx_e + 1
    return result



def input_guess(letter_count: int) -> str:
    guess: str = input(f"Enter a {letter_count} letter word: ")
    while len(guess) != letter_count:
        guess = input(f"That wasn't {letter_count} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_count = 1
    secret_word: str = "codes"
    still_playing: bool = True

    while still_playing == True:
        guess: str = input_guess(len(secret_word))
        print(f"=== Turn {turn_count}/6 ===")
        print(emojified(secret_word, guess))
        if guess == secret_word: 
            print(f"You won in {turn_count}/6 turns!")
            still_playing = False    
        turn_count = turn_count + 1
        if turn_count > 6 and still_playing == True:
            print("X/6 - Sorry, try again tomorrow!")
            still_playing = False

if __name__ == "__main__":
    main()