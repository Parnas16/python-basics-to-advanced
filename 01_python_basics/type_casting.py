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



# Output:
# String value: 100
# After converting to int: 100
# Type: <class 'int'>
# ------------------------------
# Integer value: 25
# After converting to float: 25.0
# Type: <class 'float'>
# ------------------------------
# Float value: 99.99
# After converting to int: 99
# ------------------------------
# Integer value: 20
# After converting to string: 20
# Type: <class 'str'>
# ------------------------------
# bool(1): True
# bool(0): False
# bool('Hello'): True
# bool(''): False
# ------------------------------
# Enter a number: 2
# Enter a decimal number: 2.34
# Sum: 4.34
