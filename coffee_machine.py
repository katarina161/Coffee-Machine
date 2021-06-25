class MachineActions:
    BUY = "buy"
    FILL = "fill"
    TAKE = "take"
    EXIT = "exit"
    REMAINING = "remaining"
    BACK = "back"


class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money, *coffee_supply):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.coffee_supply = list(coffee_supply)

    def update_machine_stock(self, water=0, milk=0, beans=0, cups=0, money=0):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups
        self.money += money

    def enough_to_make_coffee(self, coffee):
        can = True
        message = "Sorry, not enough "
        deficit = []
        if self.water < coffee.water:
            deficit.append("water")
        if self.milk < coffee.milk:
            deficit.append(", milk")
        if self.beans < coffee.beans:
            deficit.append(", coffee beans")
        if self.cups < 1:
            deficit.append(", disposable cups")

        message += ", ".join(deficit)
        message += "!"
        if deficit:
            print(message)
            can = False
        return can

    def do(self):
        print()
        action = input("Write action (buy, fill, take):\n")
        print()
        if action == MachineActions.EXIT:
            return False

        if action == MachineActions.BUY:
            self.buy_coffee()
        elif action == MachineActions.FILL:
            self.fill_machine()
        elif action == MachineActions.REMAINING:
            print(self.__str__())
        else:
            self.take_money()

        return True

    def buy_coffee(self):
        message = "What do you want to buy? "
        message += ', '.join([str(c) for c in self.coffee_supply])
        message += ", back - to main menu:"
        c_type = input(message + "\n")
        if c_type == MachineActions.BACK:
            return

        coffee = None
        for c in self.coffee_supply:
            if c.c_id == int(c_type):
                coffee = c

        if coffee and self.enough_to_make_coffee(coffee):
            self.update_machine_stock(water=-coffee.water,
                                      milk=-coffee.milk,
                                      beans=-coffee.beans,
                                      cups=-1,
                                      money=coffee.price)
            print("I have enough resources, making you a coffee!")

    def fill_machine(self):
        water = int(input("Write how many ml of water you want to add:\n"))
        milk = int(input("Write how many ml of milk you want to add:\n"))
        beans = int(input("Write how many grams of coffee beans you want to add:\n"))
        cups = int(input("Write how many disposable coffee cups you want to add:\n"))

        self.update_machine_stock(water, milk, beans, cups)

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def __str__(self):
        dialogue = "The coffee machine has:"
        dialogue += f"\n{self.water} of water"
        dialogue += f"\n{self.milk} of milk"
        dialogue += f"\n{self.beans} of coffee beans"
        dialogue += f"\n{self.cups} of disposable cups"
        dialogue += f"\n${self.money} of money"
        return dialogue


class Coffee:

    def __init__(self, c_id, c_type, water, milk, beans, price):
        self.c_id = c_id
        self.c_type = c_type
        self.water = water
        self.milk = milk
        self.beans = beans
        self.price = price

    def __str__(self):
        return f"{self.c_id} - {self.c_type}"


if __name__ == "__main__":

    espresso = Coffee(1, "espresso", 250, 0, 16, 4)
    latte = Coffee(2, "latte", 350, 75, 20, 7)
    cappuccino = Coffee(3, "cappuccino", 200, 100, 12, 6)

    machine = CoffeeMachine(400, 540, 120, 9, 550, espresso, latte, cappuccino)

    working = True
    while working:
        working = machine.do()
