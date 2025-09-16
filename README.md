# Python Coffee Machine Simulator ☕

A simple, text-based coffee machine simulator written in Python. This program mimics the functionality of a real coffee machine, allowing users to order drinks, process payments, and manage resources.

## ✨ Features

  * **Order Drinks**: Users can order one of three available drinks: **Espresso**, **Latte**, or **Cappuccino**.
  * **Resource Management**: The machine tracks its internal resources (water, milk, coffee). It will not dispense a drink if there aren't enough ingredients.
  * **Coin-Based Payments**: The program accepts payments in US coins (pennies, nickels, dimes, and quarters).
  * **Transaction Handling**: It checks if the payment is sufficient, provides change if necessary, and refunds money if the payment is too low.
  * **Admin Commands**:
      * `report`: Prints a detailed report of the current resource levels and money collected.
      * `off`: Shuts down the machine and terminates the program.

-----

## 🚀 How to Run

1.  **Prerequisites**: Ensure you have **Python 3** installed on your system.
2.  **Save the Code**: Save the provided code into a file named `main.py`.
3.  **Execute from Terminal**: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command:
    ```bash
    python main.py
    ```
4.  **Interact**: Follow the on-screen prompts to order your coffee\!

-----

## ⚙️ Code Structure

The program's logic is built around two key dictionaries and a `while` loop.

  * `menu`: A dictionary that defines each drink, including its required **ingredients** and **price**.
    ```python
    menu = {
        "espresso": {
            "ingredients": { "water": 50, "milk": 0, "coffee": 20 },
            "price": 1.5
        },
        # ... other drinks
    }
    ```
  * `resources`: A dictionary that acts as the machine's inventory, tracking the available **water**, **milk**, **coffee**, and **money**.
    ```python
    resources = {
        "water": 1000,
        "milk": 1000,
        "coffee": 100,
        "money": 0
    }
    ```
  * **Main Loop**: An infinite `while` loop keeps the machine running. Inside the loop, the program:
    1.  Prompts the user for an order.
    2.  Handles special commands (`off`, `report`).
    3.  Checks if resources are sufficient for the selected drink.
    4.  Processes coin-based payment.
    5.  Completes the transaction by deducting ingredients, adding money, and dispensing the drink (and any change).

-----

## 💡 Possible Improvements

This project serves as a great foundation. Here are a few ideas for extending its functionality:

  * **Refactor with Functions**: Encapsulate repetitive logic (like resource checking and payment processing) into separate functions to make the code cleaner and more modular (DRY - Don't Repeat Yourself).
  * **Object-Oriented Programming**: Re-implement the project using classes, such as a `CoffeeMachine` class, to better organize data and behavior.
  * **Robust Error Handling**: Add `try-except` blocks to handle invalid user inputs, such as ordering an item not on the menu or entering non-numeric values for coins.
  * **Scalability**: Make it easier to add new drinks to the `menu` without having to modify the core logic.
