import json

FILE_PATH = r"C:\Academics 25-26\3rd Sem\My Work\Focused\Projects\Coffee Machine\data\data.json"

def load_data(filename_or_path=FILE_PATH):
    with open(filename_or_path, "r") as f:
        return json.load(f)

def save_data(data, filename_or_path=FILE_PATH):
    with open(filename_or_path, "w") as f:
        json.dump(data, f, indent=4)