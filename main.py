from coffee.menu import Menu, MenuItem
from coffee.coffee_maker import CoffeeMaker
from coffee.money_machine import MoneyMachine
from coffee.data_handler import load_data, save_data

import difflib

def main():
    try:
        data = load_data()
    except (FileNotFoundError, ValueError):
        print("Data file not found, initializing defaults.")
        data = {
            "resources": {"water": 1000, "milk": 1000, "coffee": 200},
            "sales": {"profit": 0}
        }
        save_data(data)

    money_machine = MoneyMachine(data)
    coffee_maker = CoffeeMaker(data)
    menu = Menu()

    is_on = True
    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like ({options})? ").lower()

        if choice == "off":
            save_data(data)
            print("Turning off... Goodbye!")
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif not choice.strip():
            print("Please enter a valid option.")
        else:
            valid_options = [item.name for item in menu.menu]
            if choice not in valid_options:
                closest_match = difflib.get_close_matches(choice, valid_options, n=1, cutoff=0.6)
                if closest_match:
                    confirm = input(f"'{choice}' not found. Did you mean '{closest_match[0]}'? (y/n): ").lower()
                    if confirm == "y":
                        choice = closest_match[0]
                    else:
                        print(f"'{choice}' is not available. Please choose from {options}")
                        continue
                else:
                    print(f"'{choice}' is not available. Please choose from {options}")
                    continue

            drink = menu.find_drink(choice)
            if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink, data)

if __name__ == "__main__":
    main()
