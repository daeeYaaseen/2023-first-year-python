def sumOdd():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    SumOddNUm = 0

    #minimising chances of error
    if num1 > num2:
        for i in range(num2, num1 + 1):
            if i % 2 != 0:
                SumOddNUm += i

    elif num2 > num1:
        for i in range(num1, num2 + 1):
            if i % 2 != 0:
                SumOddNUm += i

    else:
        print("Error. Numbers can't be equal.")            

    return SumOddNUm
    

print(sumOdd())



