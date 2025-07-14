def check_even_odd(n: int) -> str:
    return "Even" if n % 2 == 0 else "Odd"

if __name__ == "__main__":
    try:
        number = int(input("Enter a number to check: "))
        print(f"{number} is {check_even_odd(number)}.")

        number_list = list(map(int, input("Enter numbers separated by space: ").split()))
        for num in number_list:
            print(f"{num} is {check_even_odd(num)}.")
    except ValueError:
        print("Please enter valid integers.")
