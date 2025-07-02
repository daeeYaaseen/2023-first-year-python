'''QUESTION 3

Create a python program which prompts the user for a Celsius temperature, converts the temperature to Fahrenheit, and prints out the converted temperature.
'''


#initialise variables for user inputs
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = ((celsius * 1.8) + 32)
print("The temperature in Fahrenheit is", fahrenheit)