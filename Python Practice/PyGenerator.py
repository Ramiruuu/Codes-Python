import random

# 1. Counting Generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# 2. Fibonacci Generator
def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

# 3. Random Number Generator
def random_numbers(count, start=1, end=100):
    for _ in range(count):
        yield random.randint(start, end)

# 4. File Reader Generator (For demonstration, it reads from a string)
def read_lines_from_text(text):
    for line in text.split("\n"):
        yield line

# 5. Custom Range Generator
def my_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step

# Function to handle user input and execute generators
def main():
    while True:
        print("\nChoose a generator to run:")
        print("1. Counting Generator")
        print("2. Fibonacci Generator")
        print("3. Random Number Generator")
        print("4. File Reader Generator (Simulated)")
        print("5. Custom Range Generator")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            n = int(input("Enter the maximum number to count up to: "))
            print("Counting Generator Output:")
            for num in count_up_to(n):
                print(num)

        elif choice == "2":
            limit = int(input("Enter how many Fibonacci numbers to generate: "))
            print("Fibonacci Generator Output:")
            for num in fibonacci(limit):
                print(num)

        elif choice == "3":
            count = int(input("How many random numbers to generate? "))
            start = int(input("Enter the start range: "))
            end = int(input("Enter the end range: "))
            print("Random Number Generator Output:")
            for num in random_numbers(count, start, end):
                print(num)

        elif choice == "4":
            text = input("Enter some text with multiple lines (use \\n for new lines): ")
            print("File Reader Generator Output:")
            for line in read_lines_from_text(text):
                print(line)

        elif choice == "5":
            start = int(input("Enter start number: "))
            stop = int(input("Enter stop number: "))
            step = int(input("Enter step size: "))
            print("Custom Range Generator Output:")
            for num in my_range(start, stop, step):
                print(num)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()