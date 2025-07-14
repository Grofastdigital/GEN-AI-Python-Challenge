def shopping_bill(prices: list[float], tax_percent: float) -> float:
    subtotal = sum(prices)
    tax = subtotal * (tax_percent / 100)
    total = subtotal + tax
    return total

if __name__ == "__main__":
    try:
        prices = [float(input(f"Enter price for item {i+1}: ")) for i in range(3)]
        tax_percent = float(input("Enter tax percentage: "))
        total = shopping_bill(prices, tax_percent)
        print(f"Total amount to pay (including tax): {total:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
