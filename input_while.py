while True:
    print("1. Number One")
    print("2. Number Two")
    print("3. Number Three")
    option = input("Pick Option: ")
    if option == "1":
        print("You chose 1")
    elif option == "2":
        print("You choose 2")
    elif option == "3":
        print("Leaving the Loop!")
        break
    else:
        print("Invalid command")
print("You have left the loop. ")
