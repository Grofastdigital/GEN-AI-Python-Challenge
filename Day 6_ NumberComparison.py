def compare_numbers(a: float, b: float):
    if a > b:
        return f"{a} is greater than {b}."
    elif a < b:
        return f"{a} is less than {b}."
    else:
        return f"{a} and {b} are equal."

if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(compare_numbers(a, b))
    except ValueError:
        print("Please enter valid numbers.")
