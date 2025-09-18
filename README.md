# Coffee Machine Simulator ☕

A Python project that simulates a fully functional coffee machine, offered in both **procedural** and **object-oriented (OOP)** versions. This simulator is an excellent exercise for understanding different programming paradigms, class-based design, and data persistence with JSON.

-----

## 🚀 Core Features

  * **Dual Programming Styles**: Includes both a step-by-step procedural implementation and a modular object-oriented version to compare approaches.
  * **Object-Oriented Design**: The OOP version neatly organizes code into distinct classes:
      * `MenuItem` & `Menu`: Manages drink data and menu options.
      * `CoffeeMaker`: Handles resource management (water, milk, coffee).
      * `MoneyMachine`: Processes payments and tracks profit.
  * **Data Persistence**: The machine's state (resources and profit) is automatically saved to a `data.json` file. This data is loaded on startup and updated after every transaction, so you never lose your progress.
  * **Interactive Console**: A simple and intuitive command-line interface. Order drinks, print a status `report`, or turn the machine `off`.

-----

## 📂 Project Structure

```
coffee-machine/
│
├── procedural_version/
│   └── main.ipynb         # Procedural implementation
├── oop_version/
│   ├── main.ipynb         # Object-Oriented implementation
│   └── data.json          # Stores resource and sales data
└── README.md              # Project documentation
```

-----

## ⚡ How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/coffee-machine.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd coffee-machine/oop_version
    ```
3.  **Launch the Jupyter Notebook:**
    ```bash
    jupyter notebook main.ipynb
    ```
4.  **Run the cells** and interact with the coffee machine through the prompts.

-----

## 📊 Data Persistence (`data.json`)

The machine's state is saved in a simple JSON file, ensuring that resources and sales figures are preserved between sessions.

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

  * Comparing **Procedural** vs. **Object-Oriented Programming**.
  * Implementing classes, objects, and methods in Python.
  * Handling file I/O operations with the **JSON** module.
  * Writing clean, modular, and reusable code.

-----

## 💡 Potential Enhancements

  * **User Authentication**: Implement admin and customer roles with different permissions.
  * **Database Integration**: Replace `data.json` with an SQLite database for more robust storage.
  * **Interface Upgrade**: Build a Graphical User Interface (GUI) or a web-based front-end.
