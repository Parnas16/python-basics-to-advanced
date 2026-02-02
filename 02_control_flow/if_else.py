# If-Else Control Flow in Python

# Example 1: Check positive, negative or zero
num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

print("-" * 30)

# Example 2: Check even or odd
number = int(input("Enter another number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("-" * 30)

# Example 3: Voting eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")



# Output:
# Enter a number: 4
# The number is Positive
# ------------------------------
# Enter another number: 0
# Even number
# ------------------------------
# Enter your age: 19
# You are eligible to vote

