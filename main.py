from modules.data_handler import load_data, save_data
from modules.user import login, register
from modules.coffee_machine import CoffeeMachine

import difflib

def main():
    print("Welcome to Python Coffee Machine!")

    # Initialize data and objects
    try:
        data = load_data()
    except (FileNotFoundError, ValueError):
        print("Data file not found, initializing defaults.")
        data = {
            "resources": {"water": 1000, "milk": 1000, "modules": 200},
            "sales": {"profit": 0}
        }
        save_data(data)

    # Login/ Register loop
    while True:
        choice = input("\n1. Login\n2. Register\n3. Exit\nChoose: ")
        if choice == "1":
            role = login()
            if role == "admin":
                CoffeeMachine(data).admin_menu()
            elif role == "customer":
                CoffeeMachine(data).customer_menu()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()