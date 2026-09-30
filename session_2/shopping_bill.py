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

class Product:
    ID = 0
    def __init__(self, name: str, cost: float) -> None:
        self.name = name
        self.cost = cost
        self.id = Product.ID
        Product.ID += 1
    def __float__(self):
        return self.cost

class Order:
    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity
    def cost(self):
        return float(self.product) * float(self.quantity)

class Main:
    def __init__(self) -> None:
        self.products: list[Product] = []
        self.basket: list[Order] = []
        self.close = True
    def run(self):
        while self.close:
            self.close = not opt_input(
                {
                    "Add Product": self.add_product,
                    "Add Product To Basket": self.add_product_to_basket,
                    "Remove from basket":self.remove_product_from_basket,
                    "Show Basket": self.show_basket,
                    "Show Cost": self.show_cost,
                    "Exit": menu_exit,
                }
            )
    def remove_product_from_basket(self):
        if len(self.basket) == 0:
            print("Please add products to your basket first!")
            return
        product_index = index_input(list(map(lambda x: x.product.name, self.basket)))
        self.basket.pop(product_index)
    def add_product(self):
        product_name = input("Product Name > ")
        product_cost = safe_float_input("Product Cost > ")
        self.products.append(Product(product_name, product_cost))
    def add_product_to_basket(self):
        if len(self.products) == 0:
            print("Please enter some products first!")
            return 
        product_index = index_input(list(map(lambda x: x.name, self.products)))
        quantity = int(safe_float_input("Amount of this product to add > "))
        in_basket = False
        for order in self.basket:
            if order.product == self.products[product_index]:
                order.quantity += quantity
                in_basket = True
        if not in_basket:
            self.basket.append(Order(self.products[product_index], quantity))
    def show_cost(self):
        print(f"Cost: £{sum(map(lambda x: x.cost(), self.basket))}")
    def show_basket(self):
        for order in self.basket:
            print(f"{order.quantity}x {order.product.name} ")
    
    
if __name__=="__main__":
    m = Main()
    m.run()


    