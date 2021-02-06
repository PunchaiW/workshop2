fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

print("--------------")

string = "banana"
for char in string:
    print(char)

# Output:
# b
# a
# n
# a
# n
# a

print("--------------")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# Output:
# apple

print("--------------")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# Output:
# apple
# cherry

print("--------------")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
else:
    print("finally finished!")

# Output:
# apple
# banana
# cherry
# Finally finished!

print("--------------")

adjectives = ["small", "big"]
fruits = ["apple", "banana", "cherry"]

for adjective in adjectives:
    for fruit in fruits:
        print(adjective, fruit)

# Output:
# small apple
# small banana
# small cherry
# big apple
# big banana
# big cherry
