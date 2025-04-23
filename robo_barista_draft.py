while True:
    try:
        # Ask for the customer's name
        name = input("Welcome to the Robot Barista!! May I have your name?\n")
 
        # Greet the customer with their name and thank them for coming in today
        if name.lower() == "ben":
            # Ask if the customer is evil if their name is Ben
            evil_status = input("Are you evil?\n")
            if evil_status.lower() != "no":
                # If the customer is evil, ask them to leave
                print("You're not welcome here Ben!! Get out!!")
                exit()
            else:
                # If the customer is not evil, greet them
                print("Hello " + name + ", thank you so much for coming in today. \n\n\n")
        else:
            # Greet customers with names other than Ben
            print("Hello " + name + ", thank you so much for coming in today. \n\n")

        # Display the menu and special item
        menu = {
            "Black Coffee": 8,
            "Espresso": 8,
            "Latte": 8,
            "Cappuccino": 8,
            "Frappuccino": 12
        }
        print(name + ", what would you like from our menu today? Here is what we are serving.")
        for item, price in menu.items():
            print(f"For ${price}.00 we have {item}")

        # Take the customer's order
        order = input("\n")

        # Determine the price based on the order
        price = menu.get(order, 8)

        # Ask for the quantity of the order
        while True:
            try:
                quantity = int(input("\nHow many coffees would you like?\n"))
                if quantity > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid number.")

        # Calculate the total price
        total = price * quantity

        # Display the total price to the customer
        print("\nThank you! Your total is:\n$" + str(total))

        # Inform the customer that their order will be ready soon
        print("\nThank you " + name + ", we'll have your " + str(quantity) + " " + order + "(s) ready for you in a moment. \nTo exit program press:\n Ctrl+C")
        
    except KeyboardInterrupt: 
        # Handle manual exit with Ctrl+C
        print("\nExiting program...")
        break