# String Formatting in Python

name = "Parna"
age = 20
branch = "AIML"

print("-" * 30)

# 1. Using comma (basic print)
print("Name:", name, "Age:", age)

print("-" * 30)

# 2. Using format() method
formatted_text = "My name is {} and I am {} years old.".format(name, age)
print(formatted_text)

print("-" * 30)

# 3. Using format() with index
formatted_text2 = "Branch: {1}, Name: {0}".format(name, branch)
print(formatted_text2)

print("-" * 30)

# 4. Using f-strings (Recommended & Modern Way)
f_string_text = f"My name is {name}, I am {age} years old, studying {branch}."
print(f_string_text)

print("-" * 30)

# 5. Formatting numbers
pi = 3.1415926535
print(f"Value of Pi (2 decimal places): {pi:.2f}")

print("-" * 30)

# 6. Padding and alignment
print(f"{name:>10}")   # Right align
print(f"{name:<10}")   # Left align
print(f"{name:^10}")   # Center align
