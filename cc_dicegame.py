import random

high_score = 0

def dice_game():

    print("Current High Score: 0")
    user_input = input("Enter your choice :")
 
    pips = random.randint(1, 6)
    print("You roll a...", pips)
    pipps = random.randint(1, 6)
    print("You roll a...", pipps)

dice_game()
