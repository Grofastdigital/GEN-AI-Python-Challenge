def count_numbers(numbers: list[int]):
    positive = sum(1 for n in numbers if n > 0)
    negative = sum(1 for n in numbers if n < 0)
    zero = sum(1 for n in numbers if n == 0)
    return positive, negative, zero

if __name__ == "__main__":
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        pos, neg, zero = count_numbers(numbers)
        print(f"Positive: {pos}, Negative: {neg}, Zeros: {zero}")
    except ValueError:
        print("Please enter valid integers.")
