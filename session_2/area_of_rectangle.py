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

def opt_input(options: dict[str, Callable]):
    for i, title in enumerate(options):
        print(f"[{i+1}] - {title}")
    completed = False
    value = -1
    while not completed:
        value = input(f"Select Option (1-{len(options)}) > ")
        try:
            value = int(value) - 1
            if value >= 0 and value < len(options):
                completed = True
            else:
                print("Please enter a number within the range")
        except ValueError:
            print("Please enter a number")
    return list(options.values())[value]() # type: ignore


def calculate_area():
    width = safe_float_input("Width > ")
    height = safe_float_input("Height > ")

    print(f"Area is: {width*height}")

def menu_exit():
    return True

def main():
    close = True
    while close:
        close = opt_input({
            "Calculate Area": calculate_area,
            "Exit": menu_exit,
        })



if __name__=="__main__":
    main()

