while True:
    try:
        name = input("\nWelcome to the Robot Barista!! May I have your name?\n")
 
        # Greet the customer with their name and thank them for coming in today
        if name.lower() == "ben":
            evil_status = input("Are you evil?\n")
            if not evil_status == "no":
                print("You're not welcome here Ben!! Get out!!")
                exit()
            else:
                print("Hello " + name + ", thank you so much for coming in today. \n\n\n")
        else:
            print("Hello " + name + ", thank you so much for coming in today. \n\n")

        # Display the menu and special item
        menu = "Black Coffee, Espresso, Latte, or a Cappuccino"
        spcl = "Frappuccino"
        print(name + ", what would you like from our menu today? Here is what we are serving. \n\n" + "For $8.00 we have " + menu + " and for $12.00 we have our special " + spcl)

        # Take the customer's order
        order = input("\n")

        # Determine the price based on the order
        if order == "Frappuccino":
            price = 12
        else:
            price = 8

        # Get the quantity of the order
        quantity = input("\nHow many coffees would you like?\n")

        # Calculate the total price
        total = price * int(quantity)

        # Display the total price
        print("Thank you. Your total is:\n$" + str(total))

        # Confirm the order and provide exit instructions
        print("Thank you " + name + ", we'll have your " + quantity + " " + order + "'s" + " ready for you in a moment. \n To exit program press:\n Ctrl+C")
        pass
    except KeyboardInterrupt:
        print("\nExiting program...")
        break  # Allows manual exit with control+c