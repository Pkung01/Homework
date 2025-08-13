class OnlineShop:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.products = []

    def addingItemsToCart(self, customer, product, quantity):
        customer.cart.append({"product": product, "quantity": quantity})

    def checkOut(self, customer):
        if not customer.cart:
            print("Cart is empty.")
            return
        total_price = sum(item["product"].price * item["quantity"] for item in customer.cart)
        order_id = len(customer.past_orders) + 1
        order = {
            "order_id": order_id,
            "items": customer.cart.copy(),
            "total_price": total_price
        }
        customer.past_orders.append(order)
        customer.cart.clear()
        print(f"Order #{order_id} placed successfully! Total: {total_price:.2f}")

    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                print(f"Order found: {order}")
                return
        print("Order not found.")

class Product:
    def __init__(self, name, description, price, online_shop):
        self.name = name
        self.description = description
        self.price = price
        self.online_shop = online_shop
        online_shop.products.append(self)

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []
        self.past_orders = []

