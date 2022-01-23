import random


def guess_random_number(tries, start, stop):
    rnum = random.randint(start, stop)

    while True:
        if tries > 0:
            print("Number of tries left:", tries)
            guess = int(input("Guess a number between 1 and 10: "))

            if guess == rnum:
                print("You guessed the correct number! ")
                break
            elif guess < rnum:
                print("Guess Higher!")
                tries -= 1

            elif guess > rnum:
                print("Guess Lower!")
                tries -= 1
        else:
            tries == 0
            print("You have failed to guess the number: " + guess)
            break


# guess_random_number(5, 0, 10)

# ^^^ task 1 ^^^

def guess_random_number(tries, start, stop):
    rnum = random.randint(start, stop)

    for i in range(start, stop + 1):
        if tries <= 0:
            print("The program has failed to guess the correct number.")
            break
        if i == rnum:
            print("The progam has guessed the correct number!")
            return
        elif i < rnum:
            print(f'The program is guessing... {i}')
        elif i > rnum:
            print(f'The program is guessing... {i}')
        tries -= 1

# guess_random_number(5 ,0 ,10)

# ^^^ task 2 ^^^


def guess_random_num_binary(tries, start, stop):
    rnum = random.randint(start, stop + 1)
    upper_bound = stop
    lower_bound = start
    print(f'Random number to find is: {rnum}')

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_value = tries[mid]
        if rnum == mid_value:
            print("Found it! {rnum}")
            break
        elif rnum > mid_value:
            lower_bound = mid + 1
            print("Guessing higher!")
            tries -= 1
        elif rnum < mid_value:
            upper_bound = mid - 1
            print("Guessing lower!")
            tries -= 1
        else:
            print("Your program failed to find the number. ")
            break

# guess_random_number(5, 0, 100)

# ^^^ task 3 ^^^
