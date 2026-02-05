# Tuples in Python
# Tuples are ordered and immutable collections

# Creating a tuple
colors = ("red", "green", "blue")
print("Colors:", colors)

# Accessing elements
print("First color:", colors[0])
print("Last color:", colors[-1])

print("-" * 30)

# Tuple with different data types
mixed_tuple = (1, "Python", 3.14, True)
print("Mixed tuple:", mixed_tuple)

print("-" * 30)

# Tuple length
print("Length of tuple:", len(colors))

print("-" * 30)

# Looping through tuple
print("Looping through tuple:")
for color in colors:
    print(color)

print("-" * 30)

# Tuple slicing
print("Sliced tuple (0:2):", colors[0:2])

print("-" * 30)

# Tuple packing and unpacking
student = ("Parna", 20, "AIML")
name, age, branch = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)

print("-" * 30)

# Immutable nature demonstration
print("Tuples cannot be modified after creation")
