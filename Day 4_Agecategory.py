def get_age_category(age: int) -> str:
    if age < 0:
        return "Invalid age"
    if age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age <= 59:
        return "Adult"
    else:
        return "Senior"

if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        category = get_age_category(age)
        print(f"You are classified as: {category}.")
    except ValueError:
        print("Please enter a valid number for age.")
