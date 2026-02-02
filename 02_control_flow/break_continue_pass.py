# break, continue, and pass statements in Python

# break example
print("BREAK example:")
for i in range(1, 10):
    if i == 6:
        break
    print(i)

print("-" * 30)

# continue example
print("CONTINUE example:")
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

print("-" * 30)

# pass example
print("PASS example:")
for i in range(1, 6):
    if i == 3:
        pass   # placeholder, does nothing
    else:
        print(i)

print("Loop completed")


Output:
BREAK example:
1
2
3
4
5
------------------------------
CONTINUE example:
1
2
3
4
6
7
8
9
------------------------------
PASS example:
1
2
4
5
Loop completed

