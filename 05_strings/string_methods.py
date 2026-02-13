# String Methods in Python

text = "Hello Python World"

print("Original String:", text)

print("-" * 30)

# Case conversion
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Title Case:", text.title())

print("-" * 30)

# Searching
print("Find 'Python':", text.find("Python"))
print("Count of 'o':", text.count("o"))

print("-" * 30)

# Replacing
new_text = text.replace("World", "Programming")
print("After Replace:", new_text)

print("-" * 30)

# Splitting
words = text.split()
print("Split words:", words)

print("-" * 30)

# Checking methods
print("Is alphabetic:", text.isalpha())
print("Is numeric:", "12345".isdigit())
print("Starts with 'Hello':", text.startswith("Hello"))
print("Ends with 'World':", text.endswith("World"))

print("-" * 30)

# String length
print("Length of string:", len(text))
