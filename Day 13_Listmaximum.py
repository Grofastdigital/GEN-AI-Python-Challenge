# Day 13/50 - AI Python Challenge
# Task: Find the largest number in a list without using max() function

def find_max_in_list(numbers):
    """
    Finds the largest number in a list without using max().
    """
    if not numbers:
        return None  # handle empty list gracefully

    max_number = numbers[0]  # assume first element is max
    for num in numbers:
        if num > max_number:
            max_number = num  # update if a larger number is found
    return max_number

if __name__ == "__main__":
    # Sample test list
    test_list = [12, 45, 23, 89, 156, 34, 90, 10]

    print(f"List to check: {test_list}")

    largest = find_max_in_list(test_list)

    if largest is not None:
        print(f"The largest number in the list is: {largest}")
    else:
        print("The list is empty. No maximum value found.")

