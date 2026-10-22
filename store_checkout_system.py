# Raw stock delivery data
raw_delivery = [
    ("Apple", 0.75, 50),
    ("Banana", 0.40, 100),
    ("Milk", 2.50, 15),
    ("Bread", 1.80, 20),
    ("Apple", 0.75, 30),  # Extra stock of apples arriving
]


# Customer shopping cart (List of products they want to buy)
shopping_cart = ["Apple", "Apple", "Milk", "Dragonfruit", "Bread"]
#1.Build Inventory
def build_inventory(raw_delivery):
    inventory = {}

    for product, price, quantity in raw_delivery:
        if product in inventory:
            inventory[product]["stock"] += quantity
        else:
            inventory[product] = {
                "price": price,
                "stock": quantity
            }

    return inventory


inventory = build_inventory(raw_delivery)

#Process Shopping Cart
receipt = []

for product in shopping_cart:

    if product not in inventory:
        print(product, "Not available in store")

    elif inventory[product]["stock"] == 0:
        print(product, "is sold out!")

    else:
        inventory[product]["stock"] -= 1
        receipt.append((product, inventory[product]["price"]))

#Generate the Receipt (Tuple & List):
print("\nReceipt:")

for product, price in receipt:
    print(product, ":", price)

total = sum(price for product, price in receipt)

print("Total Price:", total)
