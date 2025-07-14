def calculate_average(scores: list[float]) -> float:
    return sum(scores) / len(scores)

if __name__ == "__main__":
    try:
        scores = [float(input(f"Enter score {i+1}: ")) for i in range(5)]
        avg = calculate_average(scores)
        status = "Pass" if avg >= 50 else "Fail"
        print(f"Average: {avg:.2f}, Status: {status}")
    except ValueError:
        print("Please enter valid scores.")
