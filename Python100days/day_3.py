# Day 3: Conditional Statements (if, elif, else)
# Today we'll learn how to make decisions in our programs

# Basic if statement
age = 18
if age >= 18:
    print("You are an adult!")
    print("You can vote!")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# if-elif-else statement (multiple conditions)
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Comparison operators
# == (equal to), != (not equal to)
# < (less than), > (greater than)
# <= (less than or equal to), >= (greater than or equal to)

x = 10
y = 5

if x == y:
    print("x equals y")
elif x > y:
    print("x is greater than y")
else:
    print("x is less than y")

# Logical operators: and, or, not
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login successful!")
else:
    print("Login failed!")

# Let's create an interactive program
print("=== Age Checker ===")
user_age = int(input("Enter your age: "))

if user_age < 0:
    print("That's not a valid age!")
elif user_age < 13:
    print("You're a child!")
elif user_age < 20:
    print("You're a teenager!")
elif user_age < 65:
    print("You're an adult!")
else:
    print("You're a senior!")

# Challenge: Create a program that checks if a number is positive, negative, or zero!
