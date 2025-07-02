import random

def RandomNumbers():
    f= open("C:/Users/Windows 10 Pro/Desktop/LAB6_DEV1A_223000034/lab6.txt", 'w')
    for i in range(20):
        num = random.randint(1, 100+1)
        f.write(str(num) + "\n")
        print(num , end=" ")

def ReadRandNums():
    f= open("C:/Users/Windows 10 Pro/Desktop/LAB6_DEV1A_223000034/lab6.txt", 'r')
    sumrandom = 0
    for digits in f:
        numb = int(digits.strip())
        sumrandom += numb
    print( "\n" "the sum is", sumrandom)

def MainFunc():
    RandomNumbers()
    ReadRandNums()

MainFunc()