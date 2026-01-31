# Type Casting in Python
# Converting one data type to another

# String to Integer
num_str = "100"
num_int = int(num_str)

print("String value:", num_str)
print("After converting to int:", num_int)
print("Type:", type(num_int))

print("-" * 30)

# Integer to Float
num = 25
num_float = float(num)

print("Integer value:", num)
print("After converting to float:", num_float)
print("Type:", type(num_float))

print("-" * 30)

# Float to Integer
price = 99.99
price_int = int(price)

print("Float value:", price)
print("After converting to int:", price_int)

print("-" * 30)

# Integer to String
age = 20
age_str = str(age)

print("Integer value:", age)
print("After converting to string:", age_str)
print("Type:", type(age_str))

print("-" * 30)

# Boolean type casting
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('Hello'):", bool("Hello"))
print("bool(''):", bool(""))

print("-" * 30)

# User input example
num1 = int(input("Enter a number: "))
num2 = float(input("Enter a decimal number: "))

print("Sum:", num1 + num2)
