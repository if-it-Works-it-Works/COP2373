#This code keeps current ticket and buyer count, selling people up to 4 tickets at a time, and only sells up to 20 tickets total


if __name__ == "__main__":
    # Establishing Tickets variable
    t = 20
    # Establishing Total Buyers variable, to be referenced
    b = 0

    # loops so long as there are tickets left
    while t > 0:
        # Prompts the user until they give a valid input
        while True:
            try:
                s = int(input("Hello, How Many Tickets Would You Like To Purchase?\n",))
                if s > 4:
                    print("You may only purchase up to 4 tickets, please select a new amount.")
                elif s > t:
                    print(f"Sorry, we only have {t} tickets remaining, please select a new amount.")
                elif s <= 0:
                    print("Please enter a positive number.")
                else:
                    break # if the input fits all criteria then this breaks the "while True loop" above
            except ValueError: # prompt for if the user enters a non-integer value
                print("Invalid input. Please enter a valid number.")

        # Reduces the ticket count and counts a customer
        t -= s
        b += 1
        print(f"There are now {t} tickets remaining.\n")


    print(f"There were {b} buyers today.")