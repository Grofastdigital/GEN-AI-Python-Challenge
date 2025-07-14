import time

def countdown(start: int = 13):
    for i in range(start, -1, -1):
        print(i)
        time.sleep(1)  # Faster countdown for practice
    print("Countdown complete!")

if __name__ == "__main__":
    countdown()
