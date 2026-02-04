# Lambda Functions in Python
# Lambda functions are small anonymous functions

# Example 1: Simple lambda function
add = lambda a, b: a + b
print("Sum:", add(10, 5))

print("-" * 30)

# Example 2: Lambda with single argument
square = lambda x: x * x
print("Square of 4:", square(4))

print("-" * 30)

# Example 3: Lambda with conditional expression
max_num = lambda a, b: a if a > b else b
print("Maximum:", max_num(10, 20))

print("-" * 30)

# Example 4: Lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

print("-" * 30)

# Example 5: Lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
