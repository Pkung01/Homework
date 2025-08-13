# เริ่มต้นรายการสินค้า (ว่าง)
product_list = []

def add_product(product_list):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    product = {"name": name, "quantity": quantity}
    product_list.append(product)

def show_products(product_list):
    print("\nProduct List:")
    for idx, product in enumerate(product_list, start=1):
        print(f"{idx}. {product['name']} - {product['quantity']} units")


