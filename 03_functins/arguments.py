# Types of Function Arguments in Python

# 1. Positional Arguments
def add(a, b):
    print("Sum:", a + b)

add(10, 5)

print("-" * 30)

# 2. Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Parna")

print("-" * 30)

# 3. Default Arguments
def greet(name, message="Hello"):
    print(message, name)

greet("Parna")
greet("Parna", "Welcome")

print("-" * 30)

# 4. Variable Length Arguments (*args)
def total_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Total Sum:", total)

total_sum(10, 20, 30)
total_sum(5, 15)

print("-" * 30)

# 5. Keyword Variable Length Arguments (**kwargs)
def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)

student_details(name="Parna", age=20, branch="AIML")
