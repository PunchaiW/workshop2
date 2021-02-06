thisdict = {"brand": "Ford", "model": "Mustange", "year": 1964}

# EX 1
for key in thisdict:
    print(key)

# Output:
# brand
# model
# year

print("-----------------------------------------------")

thisdict = {"brand": "Ford", "model": "Mustange", "year": 1964}

# EX 2
for key in thisdict:
    print(thisdict[key])

# Output:
# Ford
# Mustang
# 1964

print("-----------------------------------------------")

thisdict = {"brand": "Ford", "model": "Mustange", "year": 1964}

# EX 3
for key in thisdict.keys():
    print(key)

# Output:
# brand
# model
# year

print("-----------------------------------------------")

thisdict = {"brand": "Ford", "model": "Mustange", "year": 1964}

# EX 4
for key in thisdict.values():
    print(key)

# Output:
# Ford
# Mustang
# 1964

print("-----------------------------------------------")

thisdict = {"brand": "Ford", "model": "Mustange", "year": 1964}

# EX 5
for key, value in thisdict.items():
    print(key, value)

# Output:
# Ford
# Mustang
# 1964