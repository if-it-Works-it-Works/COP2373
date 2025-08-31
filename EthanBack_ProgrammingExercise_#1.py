#This code sells up to 20 cinema tickets, allowing each customer to purchase up to 4 tickets at once.
# It validates the users input, records # of remaining tickets as-well as customers, and stops once there are no remaining tickets.

MAX_TICKETS = 20 #contstant

# defining a function that will prompt the user till they give a valid input
def get_valid_ticket_request(remaining):
    while True:
        try:
            s = int(input("Hello! How Many Tickets Would You Like To Purchase?\n", ))

            if s > 4:
                print("You may only purchase up to 4 tickets, please select a new amount.")

            elif s > remaining:
                print(f"Sorry, we only have {remaining} tickets remaining, please select a new amount.")

            elif s <= 0:
                print("Please enter a positive number.")

            else:
               return s

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# defining our main function and it's variables/values
def main():
    tickets_remaining = MAX_TICKETS
    customers = 0

    while tickets_remaining > 0:
        requested = get_valid_ticket_request(tickets_remaining)

        tickets_remaining -= requested

        customers += 1

        print(f"There are now {tickets_remaining} tickets remaining.\n")

    print(f"Tickets Sold Out. There were {customers} today")

# establishing our program
if __name__ == "__main__":
    #running our "main()" function
    main()