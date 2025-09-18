# ☕ Python Coffee Machine Simulator

A fully functional coffee machine simulator built with Python. This project demonstrates core **object-oriented programming (OOP)** principles by modeling a coffee machine's menu, resources, and payment processing. The machine's state, including resources and profit, is automatically saved to a `data.json` file after every transaction.

-----

## 🚀 Core Features

  * **Object-Oriented Design**: The machine is built using distinct classes (`MenuItem`, `Menu`, `CoffeeMaker`, `MoneyMachine`), making the code modular, clean, and easy to maintain.
  * **Data Persistence**: Never lose your progress\! The machine’s resources (water, milk, coffee) and total profit are **saved to `data.json`** and reloaded every time you run the simulator.
  * **Resource Management**: The `CoffeeMaker` class intelligently checks if there are enough ingredients to make a drink before brewing.
  * **Transaction Processing**: The `MoneyMachine` class handles all payment logic, accepting virtual coins, calculating change, and tracking profits.
  * **Interactive CLI**: A simple and intuitive command-line interface allows you to order drinks, check resources with a `report`, or turn the machine `off`.

-----

## 📂 Project Structure

The project is organized into just two key files, keeping it simple and straightforward.

```
coffee-machine/
│
├── main.ipynb      # The main Python script with the coffee machine logic.
└── data.json       # Stores and loads the machine's resources and profit.
```

-----

## ⚡ Getting Started

Running the simulator is easy. Just follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/coffee-machine.git
    cd coffee-machine
    ```

2.  **Launch the Jupyter Notebook:**

    ```bash
    jupyter notebook main.ipynb
    ```

3.  **Run the cells** in the notebook and follow the prompts in the console to interact with your coffee machine\!

-----

## 📊 How It Works: Data Persistence

The machine's state is stored in `data.json`. This file is read when the simulator starts and updated after every successful purchase, ensuring your resource levels and sales data are always current.

**Example `data.json`:**

```json
{
  "resources": {
    "water": 300,
    "milk": 200,
    "coffee": 100
  },
  "sales": {
    "profit": 0.0
  }
}
```

-----

## 🎯 Key Concepts Demonstrated

This project is an excellent practical exercise for understanding:

  * **Object-Oriented Programming (OOP)** in Python.
  * **Class and method design** for building modular systems.
  * **JSON file handling** for data storage and retrieval.
  * Writing **clean, reusable, and well-documented code**.

-----

## 💡 Future Roadmap

Here are a few ideas for extending the project's functionality:

  * **User Authentication**: Implement different roles, like an "admin" who can refill resources and a "customer" who can only order.
  * **Database Integration**: Replace the `data.json` file with a more robust database system like **SQLite**.
  * **GUI Interface**: Upgrade the command-line interface to a graphical user interface using a library like **Tkinter** or **PyQt**.
