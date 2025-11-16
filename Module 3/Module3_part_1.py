def main():
    # Get food charge from user
    charge_amt = float(input("Enter the charge for the food: $"))

    # Calculate tax, tip, and total price
    tax = charge_amt * 0.07
    tip = charge_amt * 0.18
    total_price = charge_amt + tax + tip

    # Display results
    print(f"Sales Tax (7%): ${tax:.2f}")
    print(f"Tip (18%): ${tip:.2f}")
    print(f"Total Price: ${total_price:.2f}")

if __name__ == "__main__":
    main()