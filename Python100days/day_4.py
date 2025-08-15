# Day 4: Loops (for and while)
# Today we'll learn how to repeat code multiple times

# For loop - when you know how many times to repeat
print("=== For Loop Examples ===")

# Looping through a range of numbers
for i in range(5):
    print(f"Count: {i}")

# Looping through a range with start and end
for i in range(1, 6):
    print(f"Number: {i}")

# Looping through a range with step
for i in range(0, 10, 2):
    print(f"Even number: {i}")

# Looping through a string
word = "Python"
for letter in word:
    print(f"Letter: {letter}")

# Looping through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loop - when you don't know how many times to repeat
print("\n=== While Loop Examples ===")

# Basic while loop
count = 0
while count < 5:
    print(f"While count: {count}")
    count += 1  # Don't forget to increment!

# While loop with user input
print("\n=== Number Guessing Game ===")
secret_number = 7
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You got it in {attempts} attempts!")

# Loop control: break and continue
print("\n=== Loop Control Examples ===")

# break - exits the loop completely
for i in range(10):
    if i == 5:
        break  # Stop when i equals 5
    print(f"Break example: {i}")

# continue - skips the rest of the current iteration
for i in range(10):
    if i % 2 == 0:  # If i is even
        continue    # Skip to next iteration
    print(f"Continue example: {i}")  # Only odd numbers

# Nested loops (loop inside a loop)
print("\n=== Nested Loops ===")
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# Challenge: Create a program that prints a multiplication table for numbers 1-5!
