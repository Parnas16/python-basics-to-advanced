# Sets in Python
# Sets are unordered and do not allow duplicate elements

# Creating a set
numbers = {1, 2, 3, 4, 4, 5}
print("Numbers set:", numbers)

print("-" * 30)

# Adding elements
numbers.add(6)
print("After adding 6:", numbers)

print("-" * 30)

# Removing elements
numbers.remove(3)
print("After removing 3:", numbers)

print("-" * 30)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Set1:", set1)
print("Set2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)

print("-" * 30)

# Looping through a set
print("Looping through set:")
for num in numbers:
    print(num)

print("-" * 30)

# Set properties
print("Length of set:", len(numbers))
print("Is 2 in set?:", 2 in numbers)
