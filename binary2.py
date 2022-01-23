import random

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
        elif rnum  > mid_value:
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

guess_random_number(5, 0, 100)