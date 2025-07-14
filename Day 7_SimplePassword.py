def check_password_strength(password: str, min_length: int = 8) -> str:
    if len(password) < min_length:
        return "Password too short."
    elif not any(char.isdigit() for char in password):
        return "Password should include at least one digit."
    elif not any(char.isalpha() for char in password):
        return "Password should include at least one letter."
    else:
        return "Password is strong."

if __name__ == "__main__":
    password = input("Enter a password: ")
    print(check_password_strength(password))

