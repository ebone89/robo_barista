while True:
    try:
        name = input("Welcome to the Robot Barista!! May I have your name?\n")
 
#greet the customer with their name and thank them for coming in today
 
        if name.lower() == "Ben":
            evil_status = input("Are you evil?\n")
            if not evil_status == "no":
                print("You're not welcome here Ben!! Get out!!")
                exit()
            else:
                print("Hello " + name + ", thank you so much for coming in today. \n\n\n")
        else:
            print("Hello " + name + ", thank you so much for coming in today. \n\n")

        menu = "Black Coffee, Espresso, Latte, or a Cappucino"
        spcl = "Frappucino"
        print(name + ", what would you like from our menu today? Here is what we are serving. \n\n" + "For $8.00 we have " + menu + " and for $12.00 we have our special " + spcl)

        order = input("\n")

        if order == "Frappucino":
            price = 12
        else:
            price = 8

        quanity = input("\nHow many coffees would you like?\n")

        total = price * int(quanity)

        print("Thank you Your total is:\n$" + str(total))

        print("Thank you " + name + ", we'll have your " + quanity + " " + order +"'s" + " ready for you in a moment. \n To exit program press:\n Ctrl+C")
        pass
    except KeyboardInterrupt:
        print("\nExciting program...")
        break #Allows manualk exit with control+c