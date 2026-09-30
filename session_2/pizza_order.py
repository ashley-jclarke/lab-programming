from collections.abc import Callable

def index_input(options: list) -> int:
    completed = False
    value = -1
    while not completed:
        str_value = input(f"Select Option (1-{len(options)}) > ")
        try:
            value = int(str_value) - 1
            if value >= 0 and value < len(options):
                completed = True
            else:
                print("Please enter a number within the range")
        except ValueError:
            print("Please enter a number")
    return value

def opt_input(options: dict[str, Callable]):
    for i, title in enumerate(options):
        print(f"[{i+1}] - {title}")
    value = index_input(list(options.keys()))
    return list(options.values())[value]() # type: ignore

menu = list(map(lambda pizza: pizza + " pizza", [
    "RAM",
    "HDD",
    "CPU",
    "GPU",
    "ACC",
    "ROM",
    "CD",
    "DVD",
    "Blu-Ray"
]))

def menu_exit():
    return True

class Main:
    def __init__(self) -> None:
        self.basket = []
        self.close = False
    def run(self):
        while not self.close:
            self.close = opt_input({
                "Add Pizza": self.add_to_basket,
                "Show Cost": self.show_cost,
                "Exit": menu_exit,
            })
    def add_to_basket(self):
        index = index_input(menu)
        self.basket.append(menu[index])
        print(f"Added {menu[index]}!")
    def show_cost(self):
        print(f"Order costs: {8*len(self.basket)}")

    
if __name__=="__main__":
    m = Main()
    m.run()

