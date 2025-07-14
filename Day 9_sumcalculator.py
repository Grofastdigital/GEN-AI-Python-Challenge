def calculate_sum(n: int) -> int:
    return sum(range(1, n + 1))

if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer: "))
        if n < 1:
            print("Number should be positive.")
        else:
            print(f"Sum from 1 to {n} is {calculate_sum(n)}.")
    except ValueError:
        print("Please enter a valid integer.")
