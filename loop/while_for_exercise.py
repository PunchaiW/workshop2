gear1 = 12
while gear1 > 0:
    print("\t[ " + str(gear1) + " ]")
    for gear2 in range(12):
        print(str(gear1) + " * " + str(gear2 + 1) + " : " + str(gear1 * (gear2 + 1)))
    gear1 = gear1 - 1
    print("---------------------")
