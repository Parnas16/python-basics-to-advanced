# Functions in Python

# Example 1: Simple function
def greet():
    print("Hello, welcome to Python!")

greet()

print("-" * 30)

# Example 2: Function with parameters
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

print("-" * 30)

# Example 3: Function with user input
def multiply(x, y):
    return x * y

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Multiplication:", multiply(num1, num2))

print("-" * 30)

# Example 4: Function with default argument
def student_info(name, branch="AIML"):
    print("Name:", name)
    print("Branch:", branch)

student_info("Parna")
student_info("Parna", "CSE")
