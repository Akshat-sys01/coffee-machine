from coffee.data_handler import save_data

# Define "CoffeeMaker" class
class CoffeeMaker:
  def __init__(self, data):
    self.resources = data["resources"]

  def report(self):
    print(f"Water: {self.resources['water']}ml")
    print(f"Milk: {self.resources['milk']}ml")
    print(f"Coffee: {self.resources['coffee']}g")

  def is_resource_sufficient(self, drink):
    can_make = True
    for item in drink.ingredients:
      if drink.ingredients[item] > self.resources[item]:
        print(f"Sorry there is not enough {item}.")
        can_make = False
    return can_make

  def make_coffee(self, order, data):
    for item in order.ingredients:
      self.resources[item] -= order.ingredients[item]

    data["resources"] = self.resources
    save_data(data)

    print(f"Here is your {order.name} ☕️. Enjoy!")
