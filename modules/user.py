import json

USER_FILE = "data/users.json"

def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)["users"]
    
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump({"users": users}, f, indent=4)

def login():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("\nWelcome, {username}!")
            return user["role"]
        
    print("\nInvalid username or password.\n")
    return None

def register():
    users = load_users()
    username = input("Choose a username: ")

    # Check if username exists
    if any(user["username"] == username for user in users):
        print("Username already exists!")
        return
    
    password = input("Choose a password: ")
    users.append({"username": username, "password": password, "role": "customer"})
    save_users(users)
    print("Registration successful! You can now log in.")