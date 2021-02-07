int1 = 5
int2 = 5

string1 = "Hello"
string2 = "Hello"

float1 = 0.1
float2 = 0.1

print(int1 is int2)  # Output: True

print(string1 is string2)  # Output: True

print(float1 is float2)  # Output: True

dict1 = {"name": "pipusna", "age": "26"}
dict2 = {"name": "pipusna", "age": "26"}
dict3 = dict1

print(dict1 is dict3)  # Output: True

print(dict1 is dict2)  # Output: False

print(dict1 == dict2)  # Output: True

# Tuple, Set, List