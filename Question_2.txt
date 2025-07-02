'''QUESTION 2

Write a function that generates ‘n’ number of pins that contain 4 random alphabets, 4 random digits and 2 random characters (~!@#$%^&*) and returns a list of the pins.
 Call the function in your main program. 

Sample Input: 
10

Sample Output: 
['eqBE7250&!', 'roOE1015!$', 'zuUX9242%^', 'dKgA6652#%', 'azBw0373^#', 'SdOF9418%*', 'VafA7776&#', 'pYuJ9542$$', 'GyYF6381!@', 'kotx5215!%']'''

import string                                                              #to be used in function
import random                                                              #to generate random figures

def pinsFunction(a):                                                       #define function "pins"
    pinsList = []                                                          #create an empty list
    for i in range(a):
        alphabet = (random.choices(string.ascii_letters, k=4))             # generate 4 random alphabets, k=4 denote size of string, input 4 alphabets
        digits = (random.choices(string.digits, k=4))                      # generate 4 random digits, k=4 denote size of string, input 4 digits
        specialCharacters = (random.choices("~!@#$%^&*", k=2))             # generate 2 random special characters, k=2 denote size of string, input 2 special characters
        concatPin = "".join(alphabet +  digits + specialCharacters)        #concatenate all items, or else they will be displayed separately
        pinsList.append(concatPin)                                         #append pin to empty pins list
    return pinsList

pinsFunction = pinsFunction(int(input("Enter number of pins to be generated: "))) #call function, prompt user input - "n" number of pins
print(pinsFunction)