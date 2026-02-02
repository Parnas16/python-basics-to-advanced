# Loops in Python

# Example 1: for loop
print("For Loop Example:")
for i in range(1, 6):
    print(i)

print("-" * 30)

# Example 2: for loop with list
fruits = ["apple", "banana", "mango"]

print("Fruits List:")
for fruit in fruits:
    print(fruit)

print("-" * 30)

# Example 3: while loop
print("While Loop Example:")
count = 5
while count > 0:
    print(count)
    count -= 1

print("-" * 30)

# Example 4: break statement
print("Break Example:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("-" * 30)

# Example 5: continue statement
print("Continue Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


Output:
For Loop Example:
1
2
3
4
5
------------------------------
Fruits List:
apple
banana
mango
------------------------------
While Loop Example:
5
4
3
2
1
------------------------------
Break Example:
1
2
3
4
------------------------------
Continue Example:
1
2
4
5

