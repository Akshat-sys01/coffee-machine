# ☕ Python Coffee Machine Simulator

A text-based coffee machine simulator built in Python and implemented in Jupyter Notebooks. This project demonstrates both procedural and Object-Oriented Programming (OOP) approaches to building a simple application. It simulates the core functionalities of a coffee machine, including handling drink orders, managing resources, and processing coin-based payments.

-----

## ✨ Features

  * **📝 Multiple Drink Options**: Order from a menu of espresso, latte, or cappuccino.
  * **💧 Resource Management**: Automatically tracks and deducts water, milk, and coffee inventory for each order.
  * **💰 Coin-Based Payments**: Accepts US coins (pennies, nickels, dimes, and quarters).
  * **🔄 Smart Transaction Handling**: Calculates the total cost, processes payments, and provides exact change or refunds for insufficient amounts.
  * **🛠️ Administrator Controls**: Use special commands like `report` to view current resource levels and profit, and `off` to shut down the machine for maintenance.

-----

## 📂 Project Structure

The repository contains two versions of the simulator, both implemented as Jupyter Notebooks, organized into their respective folders.

```
coffee-machine/
│
├── procedural_version/
│   └── main.ipynb         # Procedural version (Jupyter Notebook)
├── oop_version/
│   └── main.ipynb         # Object-Oriented version (Jupyter Notebook)
└── README.md              # Project documentation
```

-----

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

You'll need the following software installed to run the notebooks:

  * **Python 3.x**
  * **Jupyter Notebook** or **JupyterLab**. If you don't have it, you can install it via pip:
    ```bash
    pip install notebook
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
3.  **Run the simulators**:
    1.  Start the Jupyter environment from your terminal:
        ```bash
        jupyter notebook
        ```
    2.  A new tab will open in your web browser. From there, you can navigate into either the `procedural_version` or `oop_version` folder.
    3.  Click on the `main.ipynb` file inside your chosen folder.
    4.  Run the cells sequentially within the notebook to start the simulator.

-----

## ⚙️ Code Overview (OOP Version)

The Object-Oriented version, found in `oop_version/main.ipynb`, is refactored into distinct classes for better modularity, organization, and scalability. Each class has a specific responsibility:

  * `MenuItem`: Represents a single drink, holding its **name**, **cost**, and required **ingredients**.
  * `Menu`: Manages the collection of all available `MenuItem` objects and provides methods to get menu items or find a specific drink.
  * `CoffeeMaker`: Handles all resource-related tasks. It stores the current inventory, checks if resources are sufficient, and "makes" the coffee by deducting the required ingredients.
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
