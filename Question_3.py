def NumMultiples():
    f= open("C:/Users/Windows 10 Pro/Desktop/LAB6_DEV1A_223000034/lab6.txt", 'w')
    userInput = int(input("Enter a number: "))
    
    for i in range(1, 10):
        f.write(str(userInput * i) + "\n")
       
def ReadMultiples():
    f= open("C:/Users/Windows 10 Pro/Desktop/LAB6_DEV1A_223000034/lab6.txt", 'r')
    multiples = f.read()
    print(multiples)
    

def mainFunc():
    NumMultiples()
    ReadMultiples()

mainFunc()