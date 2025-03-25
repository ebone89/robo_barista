while True:
    try:
        # Ask for the customer's name
        name = input("Welcome to the Robot Barista!! May I have your name?\n")
 
        # Greet the customer with their name and thank them for coming in today
        if name.lower() == "Ben":
            # Ask if the customer is evil if their name is Ben
            evil_status = input("Are you evil?\n")
            if not evil_status == "no":
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
        menu = "Black Coffee, Espresso, Latte, or a Cappucino"
        spcl = "Frappucino"
        print(name + ", what would you like from our menu today? Here is what we are serving. \n\n" + "For $8.00 we have " + menu + " and for $12.00 we have our special " + spcl)

        # Take the customer's order
        order = input("\n")

        # Determine the price based on the order
        if order == "Frappucino":
            price = 12
        else:
            price = 8

        # Ask for the quantity of the order
        quanity = input("\nHow many coffees would you like?\n")

        # Calculate the total price
        total = price * int(quanity)

        # Display the total price to the customer
        print("Thank you Your total is:\n$" + str(total))

        # Inform the customer that their order will be ready soon
        print("Thank you " + name + ", we'll have your " + quanity + " " + order +"'s" + " ready for you in a moment. \n To exit program press:\n Ctrl+C")
        pass
    except KeyboardInterrupt:
        # Handle manual exit with Ctrl+C
        print("\nExiting program...")
        break