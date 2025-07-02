'''QUESTION 1

Create a python program to prompt the user for hours and hourly rates to compute gross pay. 
For now, please don’t worry about making sure the pay has exactly two digits after the decimal place for now. 
If you want, you can play with the built-in Python round function to properly round the resulting pay to two decimal places.

Enter Hours: 35 
Enter Rate: 2.75 
Pay: 96.25'''

#initialise variables for user inputs
hours = float(input("Enter numbers of hours worked: "))
rate = float(input("Enter hourly rate: "))

grossPay = (hours * rate)
print("The gross pay is","{:.2f}".format(grossPay)) #format output to 2 decimal places

