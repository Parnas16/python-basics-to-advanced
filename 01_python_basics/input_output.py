# Python Input and Output Example

# Taking input from the user
name = input("Enter your name: ")
age = input("Enter your age: ")

# Output
print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)

# Type conversion
age = int(age)
print("Age after 1 year:", age + 1)

# Multiple inputs in one line
a, b = input("\nEnter two numbers separated by space: ").split()
a = int(a)
b = int(b)

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
