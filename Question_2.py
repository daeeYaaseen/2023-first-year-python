def WriteNumbers():
    f= open("C:/Users/Windows 10 Pro/Desktop/LAB6_DEV1A_223000034/lab6.txt", 'w')
    for i in range(1, 50+1):
        f.write(str(i) + " ")
        

def ReadNumbers():
    f= open("C:/Users/Windows 10 Pro/Desktop/LAB6_DEV1A_223000034/lab6.txt", 'r')
    list = []
    for digits in f:
        numbers = digits.split()
        for num in numbers:
            if int(num) % 2 == 0:
                list.append(num)
                print(num, end=" ")


def MainFunc():
    WriteNumbers()
    ReadNumbers()

MainFunc()