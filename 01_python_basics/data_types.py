# Python Data Types Example

# 1. Numbers
integer_num = 10          # int
float_num = 3.14          # float
complex_num = 2 + 3j      # complex

print("Integer:", integer_num)
print("Float:", float_num)
print("Complex:", complex_num)

# 2. Strings
name = "Parna"
greeting = 'Hello, World!'

print("Name:", name)
print("Greeting:", greeting)

# 3. Boolean
is_student = True
has_passed = False

print("Is student:", is_student)
print("Has passed:", has_passed)

# 4. List
fruits = ["apple", "banana", "mango"]
print("Fruits list:", fruits)
print("First fruit:", fruits[0])

# 5. Tuple
coordinates = (10, 20)
print("Coordinates tuple:", coordinates)

# 6. Set
unique_numbers = {1, 2, 2, 3, 3, 4}
print("Unique numbers set:", unique_numbers)

# 7. Dictionary
student = {
    "name": "Parna",
    "age": 20,
    "branch": "AIML"
}
print("Student dictionary:", student)
print("Student name:", student["name"])

# 8. Type checking
print("Type of integer_num:", type(integer_num))
print("Type of fruits:", type(fruits))



#Output:
# Integer: 10
# Float: 3.14
# Complex: (2+3j)
# Name: Parna
# Greeting: Hello, World!
# Is student: True
# Has passed: False
# Fruits list: ['apple', 'banana', 'mango']
# First fruit: apple
# Coordinates tuple: (10, 20)
# Unique numbers set: {1, 2, 3, 4}
# Student dictionary: {'name': 'Parna', 'age': 20, 'branch': 'AIML'}
# Student name: Parna
# Type of integer_num: <class 'int'>
# Type of fruits: <class 'list'>


