class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(total_cost))

def main():
    print("Item 1")
    name1 = input("Enter the item name: ")
    price1 = float(input("Enter the item price: "))
    quantity1 = int(input("Enter the item quantity: "))
    item1 = ItemToPurchase(name1, price1, quantity1)
    print("\n")

    print("Item 2")
    name2 = input("Enter the item name: ")
    price2 = float(input("Enter the item price: "))
    quantity2 = int(input("Enter the item quantity: "))
    item2 = ItemToPurchase(name2, price2, quantity2)
    print("\n")

    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print("Total: $" + str(total_cost))

if __name__ == "__main__":
    main()
