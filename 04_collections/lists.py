# Lists in Python
# Lists are ordered, mutable collections

# Creating a list
numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("-" * 30)

# Modifying list elements
numbers[2] = 35
print("Modified list:", numbers)

print("-" * 30)

# Adding elements
numbers.append(60)
numbers.insert(1, 15)
print("After adding elements:", numbers)

print("-" * 30)

# Removing elements
numbers.remove(35)
numbers.pop()
print("After removing elements:", numbers)

print("-" * 30)

# Looping through list
print("Looping through list:")
for num in numbers:
    print(num)

print("-" * 30)

# List length
print("Length of list:", len(numbers))

print("-" * 30)

# List slicing
print("Sliced list (1:4):", numbers[1:4])
