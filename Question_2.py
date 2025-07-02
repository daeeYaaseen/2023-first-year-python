'''2.	Write a PYTHON program that will take in 5 numbers from a user and store the numbers in an array, then square the number and display the new array.

Sample Input
[4, 2, 1, 8, 5]
Sample Output
[16, 4, 1, 64, 25]
'''
#initialise variables for user input
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))
num4 = int(input("Enter a fourth number: "))
num5 = int(input("Enter a fifth number: "))

list1 = [ num1, num2, num3, num4, num5] #python doesn't have built-in arrays, lists are used instead
print("5 numbers from a user, stored in an array:" , list1)

index = 0
while index < len(list1):
    list1[index] = int(list1[index])**2
    index +=1
print("the new array with every number squared:", list1)    