class ItemToPurchase:
    ''' Created in Module 4 '''
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        # Create an item with name, price, quantity, and description. Description was added from email feedback.
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        # Print a formatted string of the item name, quantity, price, and resulting total cost
        total_cost = self.item_price * self.item_quantity
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(total_cost))


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Initialize shopping cart with customer name, date, and an empty list of items
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        # Add an item to the shopping cart with ItemToPurchase object
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # Remove an item from the shopping cart by name if it exists
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, itemToPurchase):
        # Update an existing item's details in the cart if it exists and itemToPurchase has non default values
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == itemToPurchase.item_name:
                if itemToPurchase.item_price != 0:
                    cart_item.item_price = itemToPurchase.item_price
                if itemToPurchase.item_quantity != 0:
                    cart_item.item_quantity = itemToPurchase.item_quantity
                if itemToPurchase.item_description != "none":
                    cart_item.item_description = itemToPurchase.item_description
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Return the amount of items in the cart
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        # Return the total cost of all items in the cart
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        # Formatted print of all items in the cart and the corresponding total cost
        print("\nOUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")
        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            total_cost = self.get_cost_of_cart()
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        # Formatted print of all items and corresponding item descriptions in the cart
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(cart):
    # Show list of options user can perform on shopping cart until they quit (q)
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice == 'a':
            # Ask user for item details and add to cart
            name = input("Enter the item name: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            description = input("Enter the item description: ")
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
        elif choice == 'r':
            # Ask user for item name to remove from cart
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            # Ask user for item details to modify in cart
            name = input("Enter the item name: ")
            price = float(input("Enter the new item price (0 to leave unchanged): "))
            quantity = int(input("Enter the new item quantity (0 to leave unchanged): "))
            description = input("Enter the new item description (None to leave unchanged): ")
            item = ItemToPurchase(name, price, quantity, description)
            cart.modify_item(item)
        elif choice == 'i':
            # Print item descriptions in the cart
            cart.print_descriptions()
        elif choice == 'o':
            # Print total cost of items in the cart
            cart.print_total()
        elif choice == 'q':
            # Quit the program by exiting out of while loop
            break
        else:
            # Invalid input, ask again
            print("Not a recognized menu option. Please choose from the menu.")

def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}\n")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()
