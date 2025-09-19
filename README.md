# ☕ Python Coffee Machine Simulator

A sophisticated, object-oriented coffee machine simulator written in Python. This project showcases a clean, modular architecture, persistent data storage, and a dual-role user authentication system.

This isn't just a coffee machine; it's a robust application demonstrating core OOP principles, designed to be easily extensible, maintainable, and user-friendly.

-----

## ✨ Core Features

### 👤 Robust User & Authentication System

  * **Secure Registration & Login**: Create and access accounts with credentials stored securely.
  * **Role-Based Access Control**: The experience is tailored to your role:
      * **Customers** can view the menu, order drinks, and process payments.
      * **Admins** have access to a special panel to view sales reports, check inventory, and refill resources.

### ⚙️ Machine Operations

  * **Complete Drink Menu**: A pre-defined menu of drinks with detailed recipes.
  * **Resource Management**: The machine intelligently tracks inventory (water, milk, coffee) and reports shortages.
  * **Payment Processing**: Handles coin-based transactions, calculates costs, and provides change.
  * **Persistent Data**: The machine's state, user accounts, and sales history are automatically saved to JSON files, ensuring data is never lost between sessions.

### 🧠 Smart & User-Friendly

  * **Fuzzy Name Matching**: Typed `espreso` instead of `espresso`? No problem\! The machine uses fuzzy matching to suggest the closest available drink, preventing user frustration.
  * **Clear CLI Interface**: A clean and intuitive command-line experience guides the user through every step.

-----

## 🏗️ Project Architecture & Design

This project is built using an **Object-Oriented Programming (OOP)** approach, where each component of the coffee machine is a self-contained object with specific responsibilities. This modular design makes the code clean, reusable, and easy to debug.

### 📂 Project Structure

```
coffee-machine/
│
├── main.py             # Entry point of the program
├── data/
│   ├── data.json       # Stores resources & sales history
│   └── users.json      # Stores user credentials & roles
│
├── modules/
│   ├── coffee_machine.py # Main class; handles user roles & menus
│   ├── coffee_maker.py   # Manages resources and brews coffee
│   ├── money_machine.py  # Processes payments and profits
│   ├── menu.py           # Defines the Menu and MenuItem classes
│   ├── data_handler.py   # Handles all JSON read/write operations
│   └── user.py           # Manages user authentication & registration
│
└── README.md
```

-----

## 🚀 Getting Started

Follow these simple steps to get the coffee machine running on your local machine.

### Prerequisites

  * Python 3.9 or newer

### Installation & Setup

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/coffee-machine.git
    cd coffee-machine
    ```

2.  **(Optional but Recommended) Create a Virtual Environment**

    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Run the Application**

    ```bash
    python main.py
    ```

    That's it\! The machine will start, and you'll be prompted to log in or register a new account.

-----

## 💡 Roadmap for Future Enhancements

This project has a solid foundation, but there's always room for improvement. Here are some planned features:

  * **Database Integration**: Migrate from JSON to a more robust database system like **SQLite** for improved data management and scalability.
  * **Graphical User Interface (GUI)**: Develop a user-friendly desktop application using a framework like **Tkinter** or **PyQt**.
  * **Dynamic Menu Management**: Allow admins to add, remove, or update drink recipes directly from the admin panel.
  * **Unit Testing**: Implement a comprehensive test suite with **pytest** to ensure the reliability and stability of each module.
