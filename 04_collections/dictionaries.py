# Dictionaries in Python
# Dictionaries store data in key-value pairs

# Creating a dictionary
student = {
    "name": "Parna",
    "age": 20,
    "branch": "AIML"
}

print("Student dictionary:", student)

print("-" * 30)

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))

print("-" * 30)

# Modifying values
student["age"] = 21
print("After updating age:", student)

print("-" * 30)

# Adding new key-value pair
student["college"] = "CBIT"
print("After adding college:", student)

print("-" * 30)

# Removing elements
student.pop("branch")
print("After removing branch:", student)

print("-" * 30)

# Looping through dictionary
print("Looping through dictionary:")
for key, value in student.items():
    print(key, ":", value)

print("-" * 30)

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
