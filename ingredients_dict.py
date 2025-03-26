# Dictionary of ingredients
ingredients_black_coffee = {"water": "100ml", "coffee": "10g"}
ingredients_espresso = {"water": "30ml", "coffee": "10g"}
ingredients_latte = {"water": "30ml", "coffee": "10g", "milk": "100ml"}
ingredients_cappuccino = {"water": "30ml", "coffee": "10g", "milk": "50ml"}
ingredients_frappuccino = {"water": "30ml", "coffee": "10g", "milk": "50ml", "ice": "100g"}

# Function to get ingredients by drink name
def get_ingredients(drink_name):
    ingredients = {
        "Black Coffee": ingredients_black_coffee,
        "Espresso": ingredients_espresso,
        "Latte": ingredients_latte,
        "Cappuccino": ingredients_cappuccino,
        "Frappuccino": ingredients_frappuccino,
    }
    return ingredients.get(drink_name, None)

# Main function (only here for testing purposes)
def main():
    drink_name = input("Enter the name of the drink to get its ingredients: ")
    ingredients = get_ingredients(drink_name)
    if ingredients:
        print(f"\nIngredients for {drink_name}:")
        for ingredient, quantity in ingredients.items():
            print(f"{ingredient}: {quantity}")
    else:
        print(f"Sorry, we don't have ingredients for {drink_name}.")

if __name__ == "__main__":
    main()
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
if __name__ == "__main__":
        main()