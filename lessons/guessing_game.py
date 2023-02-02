"""Asks user for a number, goes until they get it right"""

SECRET: int = 4
guess: int = int(input("Guess a number! "))
playing: bool = True

while playing:
    if guess == SECRET:
        print("got it")
        playing = False
    else:
        print("wrong number")
        if guess % 2 == 1: #guess is odd
            print("your guess is odd, answer is even")
        if guess > SECRET:
            print("your guess 2 high")
        guess = int(input("make another guess "))
        