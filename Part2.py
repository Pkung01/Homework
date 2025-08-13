class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):
        self.__products = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.__products.append(product)

    def show_products(self):
        print("\nProduct List:")
        for idx, product in enumerate(self.__products, start=1):
            print(f"{idx}. {product.name} - {product.quantity} units")


