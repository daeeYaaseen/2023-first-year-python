'''6.	Write a Python program that reads in many numbers and multiples them until a user enters 0. 
When the user enters 0, your program should not multiply this. You will need a while loop for this. 
The result of the multiples should be displayed.'''



userInput = int(input("Please enter a number: "))
while userInput != 0:                                   # not equal to zero
    AddInput = int(input("Please enter another number: "))
    if AddInput == 0:
        break                                           # the while loop will break when the user inputs 0
    userInput = AddInput * userInput
    print("user input so far: " , userInput)            # shows all the numbers multiplied so far
    if userInput == 0:
        break                                           # the while loop will break and show the total
print(userInput)    


