from collections.abc import Callable

def safe_float_input(prompt="", error_message="Invalid Input... Try Again!"):
    value = None
    while value == None:
        str_input = input(prompt)
        try: 
            value = float(str_input)
        except ValueError:
            print(error_message)
    return value

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

def menu_exit():
    return True

def opt_input(options: dict[str, Callable]):
    for i, title in enumerate(options):
        print(f"[{i+1}] - {title}")
    value = index_input(list(options.keys()))
    return list(options.values())[value]() # type: ignore

class Main:
    def __init__(self) -> None:
        self.marks = []
        self.close = True
    def run(self):
        while not self.close:
            print(", ".join(self.marks))
            self.close = opt_input(
                {
                    "Enter Mark": self.add_mark,
                    "Remove Mark": self.remove_mark,
                    "Display Average Mark": self.average,
                    "Display Highest Mark": self.highest,
                    "Exit": menu_exit,
                }
            )
    def average(self):
        if self.check_marks():
            print("Average:",sum(self.marks)/len(self.marks))
    def highest(self):
        if self.check_marks():
            print("Highest Mark:",max(self.marks))
    def check_marks(self):
        if len(self.marks) == 0:
            print("Please enter some marks first!")
            return False
        return True
    def add_mark(self):
        mark = int(safe_float_input("Enter Mark > "))
        self.marks.append(mark)
    def remove_mark(self):
        index = index_input(self.marks)
        self.marks.pop(index)
    
if __name__=="__main__":
    m = Main()
    m.run()

