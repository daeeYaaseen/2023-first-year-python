
'''3.	Write a PYTHON program that will have the user input the ages of 8 employees into a list and display the lowest age and the highest age.

Sample Input
(17, 21, 33, 25, 55, 40, 20, 24)
Sample Output
The youngest employee is 17 years
The oldest employee is 55 years.
'''
#initialise variables for user inputs
emp1 = int(input("Enter employee age: "))
emp2 = int(input("Enter employee age: "))
emp3 = int(input("Enter employee age: "))
emp4 = int(input("Enter employee age: "))
emp5 = int(input("Enter employee age: "))
emp6 = int(input("Enter employee age: "))
emp7 = int(input("Enter employee age: "))
emp8 = int(input("Enter employee age: "))

list1 = [ emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8]
print(list1)

list1.sort()  #sort list in ascending order to use indexing
youngest = (list1[0]) #index 0 will present the first value in the list
oldest = (list1[-1])  #index -1  will present the last value in the list 

print("the youngest employee is", youngest)
print("the oldest employee is", oldest)