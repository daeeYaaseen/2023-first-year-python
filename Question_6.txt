"""QUESTION 6

Write a program that stores the basic information (i.e. First Name, Last Name, Date of Birth, and Student Number) of a student in a Dictionary. 
Your program should prompt the user to enter the information and your program should store it in a dictionary. 
The dictionary should be displayed.
"""


#initialise variables for user inputs

firstName = "User's first name"
lastName = "User's last name"
dateOfBirth = "User's date of birth"
studentNumber = "User's student number"
                    

#create dictionary to store key:value pairs
dict1 = {
firstName : str(input("Enter your first name: ")),
lastName : str(input("Enter your last name: ")),
dateOfBirth : (input("Enter your date of birth (dd/mm/yyyy): ")),
studentNumber : int(input("Enter your student number: "))
                    
} 

print(dict1)