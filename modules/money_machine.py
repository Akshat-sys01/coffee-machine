# Define "MoneyMachine" class
class MoneyMachine:
  CURRENCY = "$"
  COIN_VALUES = {
      "quarters": 0.25,
      "dimes": 0.10,
      "nickels": 0.05,
      "pennies": 0.01
  }

  def __init__(self, data):
    self.profit = data["sales"]["profit"]
    self.money_received = 0
    self.data = data

  def report(self):
    print(f"Money: {self.CURRENCY}{self.profit}")

  def process_coins(self):
    self.money_received = 0
    print("Please insert coins.")
    for coin in self.COIN_VALUES:
      while True:
        try:
          count = int(input(f"How many {coin}?: "))
          if count < 0:
            print("\nPlease enter a  non-negative number.")
            continue
          self.money_received += count * self.COIN_VALUES[coin]
          break
        except ValueError:
          print("\nPlease enter a valid number.")
    return self.money_received

  def make_payment(self, cost):
    self.process_coins()
    if self.money_received >= cost:
      change = round(self.money_received - cost, 2)
      print(f"\nHere is {self.CURRENCY}{change} in change.")
      self.profit += cost
      self.data["sales"]["profit"] = self.profit
      self.money_received = 0
      return True
    else:
      print("\nSorry that's not enough money. Money refunded.")
      self.money_received = 0
      return False
