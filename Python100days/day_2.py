# Day 2: User Input and String Formatting
# Today we'll learn how to get input from users and format strings

# Getting input from the user
# input() function pauses the program and waits for user to type something
name = input("What is your name? ")
print("Hello,", name + "!")

# We can get different types of input
age = input("How old are you? ")
print("You are", age, "years old")

# Note: input() always returns a string, even for numbers
# If we want to do math with the input, we need to convert it
birth_year = input("What year were you born? ")
birth_year = int(birth_year)  # Convert string to integer
current_year = 2024
age_calculated = current_year - birth_year
print("You are approximately", age_calculated, "years old")

# String formatting - different ways to combine strings and variables
# Method 1: Using commas (what we've been doing)
print("Name:", name, "Age:", age)

# Method 2: Using + operator
print("Name: " + name + " Age: " + age)

# Method 3: Using f-strings (formatted strings) - recommended!
print(f"Name: {name} Age: {age}")

# Method 4: Using .format() method
print("Name: {} Age: {}".format(name, age))

# Let's create a simple program that uses all these concepts
print("\n=== Personal Information Form ===")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
favorite_color = input("What's your favorite color? ")
favorite_number = input("What's your favorite number? ")

# Display the information using f-strings
print(f"\nHello {first_name} {last_name}!")
print(f"Your favorite color is {favorite_color}")
print(f"Your favorite number is {favorite_number}")

# Challenge: Create your own input form and display the results!
