from modules.coffee_maker import CoffeeMaker
from modules.money_machine import MoneyMachine
from modules.menu import Menu
from modules.data_handler import save_data
import difflib

class CoffeeMachine:
    def __init__(self, data):
        self.data = data
        self.coffee_maker = CoffeeMaker(data)
        self.money_machine = MoneyMachine(data)
        self.menu = Menu()

    # ------------------- Admin Functions ------------------
    def admin_menu(self): 
        while True: 
            choice = input("\nAdmin Menu: \n1. Refill\n2. View Report\n3. Logout\nChoose: ") 
            if choice == "1": 
                self.refill_resources() 
            elif choice == "2": 
                self.show_report() 
            elif choice == "3": 
                break 
            else: print("Invalid choice.") 

    def refill_resources(self):
        print("\nRefilling resources...")
        for item in self.data["resources"]:
            try:
                add_amount = int(input(f"Add {item} amount: "))
                self.data["resources"][item] += add_amount
            except ValueError:
                print("Please enter a valid number.")
        save_data(self.data)
        print("Resources refilled successfully!")

    def show_report(self):
        print("\n---- Resource Report ----")
        self.coffee_maker.report()
        print("\n---- Money Report ----")
        self.money_machine.report()
    
    # ---------------- Customer Functions -------------------
    def customer_menu(self): 
        while True: 
            choice = input("\nCustomer Menu:\n1. Order Coffee\n2. Logout\nChoose: ") 
            if choice == "1": 
                self.order_coffee() 
            elif choice == "2": 
                break
            else: 
                print("Invalid choice.")

    def order_coffee(self):
        options = self.menu.get_items()
        choice = input(f"\nWhat would you like ({options})? ").lower()
        if not choice.strip():
            print("Please enter a valid option.")
            return
        
        # Get all valid options
        valid_options = [item.name for item in self.menu.menu]

        # Try finding drink directly
        drink = self.menu.find_drink(choice)

        if not drink:
            # Fuzzy matching suggestion
            closest_match = difflib.get_close_matches(choice, valid_options, n=1, cutoff=0.6)
            if closest_match:
                confirm = input(f"'{choice}' not found. Did you mean '{closest_match[0]}'? (y/n): ").lower()
                if confirm == 'y':
                    drink = self.menu.find_drink(closest_match[0])
                else:
                    print(f"'{choice}' is not available. Please choose from {options}")
                    return
            else:
                print(f"'{choice}' is not available. Please choose from {options}")
                return
        
        # Process order if drink is valid
        if drink:
            if self.coffee_maker.is_resource_sufficient(drink):
                if self.money_machine.make_payment(drink.cost):
                    self.coffee_maker.make_coffee(drink, self.data)
                else:
                    print("Sorry, not enough resources to make this coffee.")
            else:
                print(f"'{choice}' is not available. Please choose from {options}")        


