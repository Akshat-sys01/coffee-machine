# ☕ Python Coffee Machine Simulator

A text-based coffee machine simulator built in Python. This project demonstrates both procedural and Object-Oriented Programming (OOP) approaches to building a simple application. It simulates the core functionalities of a coffee machine, including handling drink orders, managing resources, and processing coin-based payments.

-----

## ✨ Features

  * **📝 Multiple Drink Options**: Order from a menu of espresso, latte, or cappuccino.
  * **💧 Resource Management**: Automatically tracks and deducts water, milk, and coffee inventory for each order.
  * **💰 Coin-Based Payments**: Accepts US coins (pennies, nickels, dimes, and quarters).
  * **🔄 Smart Transaction Handling**: Calculates the total cost, processes payments, and provides exact change or refunds for insufficient amounts.
  * **🛠️ Administrator Controls**: Use special commands like `report` to view current resource levels and profit, and `off` to shut down the machine for maintenance.

-----

## 📂 Project Structure

The repository is organized into two main implementation files: one procedural and one object-oriented.

```
coffee-machine/
│
├── main.py          # Procedural version
├── main_oop.py      # Object-Oriented version
└── README.md        # Project documentation
```

-----

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have **Python 3.x** installed on your system. You can check your version by running:

```bash
python --version
```

### Installation & Execution

1.  **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/your-username/coffee-machine.git
    ```

2.  **Navigate to the project directory**:

    ```bash
    cd coffee-machine
    ```

3.  **Run the simulator**: You can run either the procedural or the OOP version of the machine.

      * To run the **procedural version**:
        ```bash
        python main.py
        ```
      * To run the **Object-Oriented version**:
        ```bash
        python main_oop.py
        ```

-----

## ⚙️ Code Overview (OOP Version)

The Object-Oriented version (`main_oop.py`) is refactored into distinct classes for better modularity, organization, and scalability. Each class has a specific responsibility:

  * `MenuItem`: Represents a single drink, holding its **name**, **cost**, and required **ingredients**.
  * `Menu`: Manages the collection of all available `MenuItem` objects and provides methods to get menu items or find a specific drink.
  * `CoffeeMaker`: Handles all resource-related tasks. It stores the current inventory of water, milk, and coffee, checks if resources are sufficient, and "makes" the coffee by deducting the required ingredients.
  * `MoneyMachine`: Manages all financial transactions. It processes coin payments, confirms if the payment is sufficient, provides change, and tracks the total profit.

### Example Initialization & Main Loop

```python
# Create objects from classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # Check resources and process payment before making the coffee
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
```

-----

## 🎯 Key Learning Objectives

This project is an excellent exercise for:

  * Practicing Python fundamentals such as functions, loops, and dictionaries.
  * Understanding and applying **Object-Oriented Programming (OOP)** principles including classes, objects, attributes, and methods.
  * Learning how to refactor procedural code into a clean, modular, and reusable OOP design.

-----

## 🔮 Future Enhancements

Potential improvements and future directions for the project include:

  * **Data Persistence**: Save resource levels and sales data to a file (JSON/CSV) or a database (SQLite).
  * **User Authentication**: Differentiate between an admin (who can run reports and refill resources) and a customer.
  * **GUI Implementation**: Build a graphical user interface using a framework like **Tkinter** or **PyQt**.
  * **Web Application**: Convert the simulator into a web app using **Flask** or **Django**.
