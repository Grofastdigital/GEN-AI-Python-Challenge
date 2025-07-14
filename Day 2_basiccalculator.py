def calculator():
    try:
        num1: float = float(input("Enter first number: "))
        num2: float = float(input("Enter second number: "))
        operation: str = input("Choose operation (+, -, *, /): ").strip()

        operations = {
            "+": num1 + num2,
            "-": num1 - num2,
            "*": num1 * num2,
            "/": num1 / num2 if num2 != 0 else "Error: Division by zero"
        }

        result = operations.get(operation, "Invalid operation")
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
