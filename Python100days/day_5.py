# Day 5: Lists and Basic Data Structures
# Today we'll learn about storing multiple items in one variable

# Creating lists
print("=== Creating Lists ===")
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]  # Lists can contain different types

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# Accessing list elements (indexing starts at 0)
print("\n=== Accessing Elements ===")
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])  # Negative index counts from the end
print("Second to last:", fruits[-2])

# Modifying lists
print("\n=== Modifying Lists ===")
fruits[1] = "blueberry"  # Change an element
print("After changing:", fruits)

fruits.append("strawberry")  # Add to the end
print("After append:", fruits)

fruits.insert(1, "mango")  # Insert at specific position
print("After insert:", fruits)

fruits.remove("orange")  # Remove specific item
print("After remove:", fruits)

popped_item = fruits.pop()  # Remove and return last item
print("Popped item:", popped_item)
print("After pop:", fruits)

# List operations
print("\n=== List Operations ===")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2  # Concatenate lists
print("Combined:", combined)

repeated = list1 * 3  # Repeat list
print("Repeated:", repeated)

# List methods
print("\n=== List Methods ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original:", numbers)

numbers.sort()  # Sort in ascending order
print("Sorted:", numbers)

numbers.reverse()  # Reverse the list
print("Reversed:", numbers)

print("Length:", len(numbers))
print("Count of 1:", numbers.count(1))
print("Index of 5:", numbers.index(5))

# Slicing lists
print("\n=== List Slicing ===")
letters = ["a", "b", "c", "d", "e", "f"]
print("Original:", letters)
print("First 3:", letters[0:3])
print("Last 3:", letters[-3:])
print("Every other:", letters[::2])
print("Reverse:", letters[::-1])

# Checking if items exist
print("\n=== Checking Items ===")
if "apple" in fruits:
    print("Apple is in the fruits list")
else:
    print("Apple is not in the fruits list")

# Looping through lists
print("\n=== Looping Through Lists ===")
for fruit in fruits:
    print(f"I like {fruit}")

for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# List comprehension (advanced but useful)
print("\n=== List Comprehension ===")
squares = [x**2 for x in range(5)]
print("Squares:", squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)

# Challenge: Create a list of your favorite movies and perform various operations on it!
