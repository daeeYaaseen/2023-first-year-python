def UserName():
    f= open("C:/Users/Windows 10 Pro/Desktop/LAB6_DEV1A_223000034/lab6.txt", 'a')
    while True:
        userInput = input("Enter your full name: ")
        f.write(str(userInput + "\n"))
        if userInput == " ":
            break
        
        f.close()

        return ""

def ReadUsers():
    f= open("C:/Users/Windows 10 Pro/Desktop/LAB6_DEV1A_223000034/lab6.txt", 'r')
    data = f.read()
    print("outputs: " + "\n" , data)    
    f.close()

    return ""

def MainFunc():
    UserName()
    ReadUsers()

    return ""

MainFunc()
