#1.	

""" Write a Python program that reads three numbers and displays the sum of the first two, concatenated with the last number. """
#assign variables to user inputs
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))
numSum = ( num1 + num2) #sum of first two numbers
print(str(numSum) + str(num3)) #concatenation without space, along with the sum
print(str(numSum) + " " + str(num3)) #concatenation with space, along with the sum

