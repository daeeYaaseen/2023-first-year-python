'''5.	Write a Python program to remove duplicate numbers from the given list below:

a = 23, 89, 90, 23, 23 ,78, 89, 45, 11, 8, 1, 56, 34, 78, 40, 21
'''

a = [23, 89, 90, 23, 23 ,78, 89, 45, 11, 8, 1, 56, 34, 78, 40, 21] #create list with duplicate numbers
noDup = []  #create empty list

a.sort() #sort list in ascending order to see duplicates more easily
print("the list with duplicates:" , a)

for i in a:
    if i not in noDup: 
        noDup.append(i)   #append list with 'not in' to remove duplicates

print("the list with duplicates removed:" , noDup)      