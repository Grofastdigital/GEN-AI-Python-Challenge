def personal_greeting():
    name: str = input("What is your name? ")
    age: int = int(input("What is your age? "))
    color: str = input("What is your favorite color? ")

    message = f"Hello {name}! At {age}, your love for {color} shows your vibrant spirit. Keep flying high! 🦅✨"
    print(message)

if __name__ == "__main__":
    personal_greeting()
