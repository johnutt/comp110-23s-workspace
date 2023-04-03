"""Exercise 06: Choose your own adventure."""
__author__ = 730579193

from random import randint
player: str = ""
current_monster: str = ""
monster_hp: int = 0
points: int = 0
still_playing: bool = True
BASE_MONSTER_HP: int = 100
DOOR_CHOICES: str = "\U0001F6AA \U0001F6AA \U0001F6AA"

def greet() -> None:
    """Introduction to the game."""
    global player
    print("Welcome to Monster Hunter! In this game, you will earn points by choosing your path while attacking monsters you find along the way!")
    name: str = input("Enter your name: ")
    player = name


def attack(att_points: int) -> int:
    """Attacks a monster based on user input."""
    global monster_hp
    original_points: int = att_points

    while monster_hp > 0:
        choice: int = int(input("Do you (1) Punch, (2) Kick, or (3) Throw a rock? (Answer 1, 2, or 3): "))
        if choice == 1:
            damage: int = randint(0, 25)
            monster_hp -= damage
            print(f"+ {damage} Adventure Points!")
            print(f"{player}, you punched the monster and did {damage} damage!")
            att_points += damage
            if monster_hp < 0:
                original_points += 100
                return original_points
            print(f"The monster has {monster_hp}/{BASE_MONSTER_HP} HP remaining!")
                
        if choice == 2:
            damage: int = randint(10, 15)
            monster_hp -= damage
            print(f"+ {damage} Adventure Points!")
            print(f"{player}, you kicked the monster and did {damage} damage!")
            att_points += damage
            if monster_hp < 0:
                original_points += 100
                return original_points
            print(f"The monster has {monster_hp}/{BASE_MONSTER_HP} HP remaining!")

        if choice == 3:
            damage: int = randint(5, 20)
            monster_hp -= damage
            print(f"+ {damage} Adventure Points!")
            print(f"{player}, you threw a rock at the monster and did {damage} damage!")
            att_points += damage
            if monster_hp < 0:
                original_points += 100
                return original_points
            print(f"The monster has {monster_hp}/{BASE_MONSTER_HP} HP remaining!")

    return att_points
            

def crossroads() -> None:
    """Player chooses a door."""
    global current_monster
    global monster_hp
    global points
    global still_playing
        
    print(DOOR_CHOICES)
    choice: int = int(input(f"{player},  you are faced with three doors. Do you choose (1) The first door, (2) The second door, (3) The third door, or (4) Leave and finish the game (Answer 1, 2, 3, or 4): "))
        
    if choice == 1 or choice == 2 or choice == 3:
        rand_monster: int = randint(1, 5)
        if rand_monster == 1:
            current_monster = "\U0001F47B"
            points += 10
            monster_hp = 100
            print("+ 10 Adventure Points")
                
        if rand_monster == 2:
            current_monster = "\U0001F47A"
            points += 10
            print("+ 10 Adventure Points")
            monster_hp = 100

        if rand_monster == 3:
            current_monster = "\U0001F47D"
            points += 10
            print("+ 10 Adventure Points")
            monster_hp = 100
            
        if rand_monster == 4:
            current_monster = "\U0001F921"
            points += 10
            print("+ 10 Adventure Points")
            monster_hp = 100
        
        if rand_monster == 5:
            current_monster = "\U0001F916"
            points += 10
            print("+ 10 Adventure Points")
            monster_hp = 100

    if choice == 4:
        still_playing = False
        return
        
    print(f"Uh oh, {player}, behind Door {choice}, {current_monster}  was waiting! Defend yourself!")
        

def main() -> None:
    """Monster Hunter."""
    global points        

    greet()
    while still_playing:
        crossroads()
        if still_playing:
            points = attack(points)
            print("The enemy has been defeated!")
            print(f"You now have {points} Adventure Points!")
        
    print(f"Thanks for playing, {player}!")
    print(f"Total Adventure Points: {points}")


if __name__ == "__main__":
    main()