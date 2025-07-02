'''Write a Python program that a generate a list of numbers from 0 – 50 and returns odd numbers.'''

list1 = range(0,51) #from 0 to (including 50 and not including) 51
for a in list1:     
    if (a %2 != 0):  # %2 to display odd numbers as a remainder
        print(a)