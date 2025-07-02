def oldEnough(age):
    if age >= 21:
        enroll = "You are old enough to enroll."
    elif 0 < age < 21:
        enroll = "You are too young to enroll."
    else:
        enroll = "Invalid input."  

    return enroll


age = int(input("Enter your age: "))
print(oldEnough(age))