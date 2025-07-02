#3

""" 3.	Write a Python program that implements the quadratic equation algorithm. 
Your program should assume that the roots are always REAL and NOT COMPLEX. For this program, DO NOT worry about complex roots.
 Use ‘if’ statement to check if the equation has no real solutions, if the equation has one solution or if the equation has two solutions """

print("The quadratic equation is ax**2 + bx + c")
import math #to work with the quadratic equation

#user assign values to the variables
a = float(input("Please enter a value for a: "))
b = float(input("Please enter a value for b: "))
c = float(input("Please enter a value for c: "))

d = ((b**2) - (4*a*c))  #discriminant formula to find roots
if (d == 0):
    x1 = (((-b) + (math.sqrt(d))) / (2*(a)))
    x2 = (((-b) - (math.sqrt(d))) / (2*(a)))
    print("x = ", x1, "or", "x = ", x2)
    solution = "The equation has one solution."
elif (d > 0):
    x1 = (((-b) + (math.sqrt(d))) / (2*(a)))
    x2 = (((-b) - (math.sqrt(d))) / (2*(a)))
    print("x = ", x1, "or", "x = ", x2)
    solution = "The equation has two solutions."
else:
    solution = "The equation has no real solution"    
print(solution)    


