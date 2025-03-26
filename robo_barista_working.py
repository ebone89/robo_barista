# Import the ingredients module
from ingredients_dict import get_ingredients

while True:
    try:
        # Ask for the customer's name
        name = input("Welcome to the Robot Barista!! May I have your name?\n")

        # Greet the customer
        print(f"Hello {name}, thank you so much for coming in today.\n")

        if name.lower() == "ben":
            
            # Ask if the customer if they are evil if their name is Ben
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
        
        
        
        # Display the menu
        menu = {
            "Black Coffee": 8,
            "Espresso": 8,
            "Latte": 8,
            "Cappuccino": 8,
            "Frappuccino": 12,
        }
        print(f"{name}, what would you like from our menu today? Here is what we are serving:")
        for item, price in menu.items():
            print(f"For ${price}.00 we have {item}")

        # Take the customer's order
        order = input("\nEnter your choice (or type 'ingredients' to see the ingredients):\n")

        # Check if the customer wants to see ingredients
        if order.lower() == "ingredients":
            drink_name = input("Which drink's ingredients would you like to see?\n")
            ingredients = get_ingredients(drink_name)
            if ingredients:
                print(f"\nIngredients for {drink_name}:")
                for ingredient, quantity in ingredients.items():
                    print(f"{ingredient}: {quantity}")
            else:
                print(f"Sorry, we don't have ingredients for {drink_name}.")
            continue  # Go back to the menu

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
        print(f"\nThank you! Your total is: ${total}")

        # Inform the customer that their order will be ready soon
        print(f"\nThank you {name}, we'll have your {quantity} {order}(s) ready for you in a moment.\nTo exit program press: Ctrl+C")

    except KeyboardInterrupt:
        # Handle manual exit with Ctrl+C
        print("\nExiting program...")
        break