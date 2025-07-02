"""QUESTION 5

Write a Python program that displays 20 to 70 in reverse order, using a for-loop. 
Displayed number must be on the same line, separated by space.
"""


#initialise list for values

list1 = []  #to be displayed on same line
for i in range(20,71):  #for 70 to be included
    list1.append(i)  #append range(20,71) to list1
list1.reverse()  #reverse list order
print(list1)