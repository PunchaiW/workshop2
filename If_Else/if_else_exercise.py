score = input("Enter your score: ")


def score_calculate(sco):
    if sco <= 100 and sco >= 80:
        sco = "A"
    elif sco <= 79 and sco >= 75:
        sco = "B+"
    elif sco <= 74 and sco >= 70:
        sco = "B"
    elif sco <= 69 and sco >= 65:
        sco = "C+"
    elif sco <= 64 and sco >= 60:
        sco = "C"
    elif sco <= 59 and sco >= 55:
        sco = "D+"
    elif sco <= 54 and sco >= 50:
        sco = "D"
    elif sco <= 49 and sco >= 0:
        sco = "F"
    else:
        print("Error can't clculate grade")
    # sco = "A" if sco <= 100 and sco >= 80 else True
    # sco = "B+" if sco <= 79 and sco >= 75 else True
    # sco = "B" if sco <= 74 and sco >= 70 else True
    # sco = "C+" if sco <= 69 and sco >= 65 else True
    # sco = "C" if sco <= 64 and sco >= 60 else True
    # sco = "D+" if sco <= 59 and sco >= 55 else True
    # sco = "D" if sco <= 54 and sco >= 50 else True
    # sco = "F" if sco <= 49 and sco >= 0 else True
    # sco = "A" if sco <= 100 and sco >= 80 else True
    print("grade: " + sco)


score_calculate(int(score))