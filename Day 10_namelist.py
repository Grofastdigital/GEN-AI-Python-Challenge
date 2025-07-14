def collect_names(count: int = 5):
    names = [input(f"Enter name {i+1}: ") for i in range(count)]
    for name in names:
        print(f"{name} (Length: {len(name)})")

if __name__ == "__main__":
    collect_names()
