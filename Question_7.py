'''QUESTION 7

 
Write a program that asks the user to enter the number of random numbers they want, the lower limit of the random numbers, and the upper limit. 
Your program should then generate random integers in this range and add it to an empty list. Display this list.

'''
import random 
#initialise variables for user input
userInput = int(input("Enter the amount of random numbers that you want: "))
lowerLimit = int(input("Enter the lower limit of the random numbers: "))
upperLimit = int(input("Enter the upper limit of the random numbers: "))

list1 = [] #create an empty list
for i in range(userInput):
    randomIntegers = random.randint(lowerLimit, upperLimit) #random integers between given user values
    list1.append(randomIntegers) #append a to empty list1
print(list1)