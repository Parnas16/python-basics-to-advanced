# Recursion in Python
# A function calling itself

# Example 1: Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number for factorial: "))
print("Factorial:", factorial(num))

print("-" * 30)

# Example 2: Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter number of terms for Fibonacci: "))

print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
print()

print("-" * 30)

# Example 3: Sum of natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

n = int(input("Enter a number to find sum: "))
print("Sum of natural numbers:", sum_natural(n))
