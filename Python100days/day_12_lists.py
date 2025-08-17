import copy

# GitHub Copilot
# Basic introduction to lists in Python
# Save this file as day_12_lists.py and run it with: python day_12_lists.py

# 1) Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

print("empty_list:", empty_list)

print("numbers:", numbers)
print("mixed:", mixed)

# 2) Indexing and negative indexing
print("first item of numbers:", numbers[0])
print("last item of numbers (negative index):", numbers[-1])

# 3) Slicing (inclusive start, exclusive end)
print("slice numbers[1:4]:", numbers[1:4])
print("slice numbers[:3]:", numbers[:3])
print("slice numbers[3:]:", numbers[3:])

# 4) Basic mutation methods
nums = [10, 20, 30]
nums.append(40)        # add to end
nums.insert(1, 15)     # insert at index 1
print("after append & insert:", nums)

nums.extend([50, 60])  # extend with iterable
print("after extend:", nums)

nums.remove(15)        # remove first occurrence of value
print("after remove(15):", nums)

popped = nums.pop()    # remove and return last item
print("popped value:", popped, "nums now:", nums)

# 5) Length and membership
print("len(nums):", len(nums))
print("20 in nums?", 20 in nums)
print("99 in nums?", 99 in nums)

# 6) Iteration
print("iterate nums:")
for i, v in enumerate(nums):
    print(i, v)

# 7) List comprehensions (concise way to create lists)
squares = [x * x for x in range(6)]
evens = [x for x in range(10) if x % 2 == 0]
print("squares:", squares)
print("evens:", evens)

# 8) Nested lists (2D)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("matrix[1][2]:", matrix[1][2])  # row 1, col 2 (0-based)

# 9) Copying lists: assignment vs shallow copy vs deep copy
a = [1, 2, [3, 4]]
b = a           # b references same list (aliasing)
c = a.copy()    # shallow copy: top-level copied, nested objects still shared
d = copy.deepcopy(a)  # deep copy: everything copied

a[0] = 100
a[2][0] = 300
print("a:", a)
print("b (alias):", b)    # reflects both changes
print("c (shallow):", c)  # reflects nested change but not top-level change
print("d (deep):", d)     # unaffected

# 10) Sorting and reversing
unsorted = [3, 1, 4, 2]
sorted_copy = sorted(unsorted)   # returns a new sorted list
unsorted.sort()                  # sorts in-place
print("sorted_copy:", sorted_copy)
print("unsorted (after sort):", unsorted)

rev = [1, 2, 3]
rev.reverse()    # in-place reverse
print("rev reversed in-place:", rev)

# 11) Concatenation and repetition
a = [1, 2]
b = [3, 4]
print("concat:", a + b)
print("repeat:", a * 3)

# 12) Common idioms
# - initialize list with repeated values
zeros = [0] * 5
print("zeros:", zeros)

# - convert iterable to list
chars = list("hello")
print("chars:", chars)

# Summary (as comments):
# - Lists are ordered, mutable collections that can contain elements of different types.
# - Typical operations: indexing, slicing, append, insert, remove, pop, extend, sort.
# - Use list comprehensions for concise list creation.
# - Beware of aliasing and shallow copies when lists contain mutable nested objects.