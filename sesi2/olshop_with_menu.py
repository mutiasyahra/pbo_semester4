# Online Shopping Cart
# Class: CartItem
# Attributes: item_name, price, quantity
# Methods: additem(), removeitem(), calculate_total()

class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        
    def additem(self, quantity):
        self.quantity += quantity
        print(f"{quantity} {self.item_name} added to cart.")
        
    def removeitem(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(f"{quantity} {self.item_name} removed from cart.")
        else:
            print(f"Cannot remove {quantity} {self.item_name} from cart.")
            
    def calculate_total(self):
        return self.price * self.quantity

cart = []

while True:
    print("--Menu--")
    print("1. List Cart")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Calculate Total")
    print("5. Exit")
    
    menu = input("Select menu: ")
    
    if menu == "1":
        for index, item in enumerate(cart):
            print(f"{index+1} - {item.item_name} ({item.quantity})")
            
    elif menu == "2":
        item_name = input("Insert item name: ")
        price = int(input("Insert price: "))
        quantity = int(input("Insert quantity: "))
        cart.append(CartItem(item_name, price, quantity))
        
    elif menu == "3":
        index = int(input("Choose item index: "))
        quantity = int(input("Insert quantity to remove: "))
        cart[index-1].removeitem(quantity)
        
    elif menu == "4":
        total = 0
        for item in cart:
            total += item.calculate_total()
        print(f"Total: ${total}")
        
    elif menu == "5":
        break
        
    else:
        print("Invalid choice")