import random

def display_sticks(sticks):
    print("Sticks remaining:", '| ' * sticks)

def player_turn(sticks):
    display_sticks(sticks)
    while True:
        max_remove = max(1, sticks // 2)
        remove = int(input(f"Select number of sticks to remove (1-{max_remove}): "))
        if 1 <= remove <= max_remove:
            return remove
        print("Invalid number of sticks. Try again.")

def computer_turn(sticks):
    remove = random.randint(1, max(1, sticks // 2))
    print(f"\nThe computer removes {remove} sticks.")
    return remove

def nim_game():
    sticks = random.randint(10, 30)
    print(f"Welcome to Nim! Starting with {sticks} sticks.")
    player_turn_flag = True
    while sticks > 0:
        remove = player_turn(sticks) if player_turn_flag else computer_turn(sticks)
        sticks -= remove
        player_turn_flag = not player_turn_flag
    print("\nCongratulations! You win!" if player_turn_flag else "\nSorry, you lost.")

nim_game()
