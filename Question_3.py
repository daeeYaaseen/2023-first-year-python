def mathFunc():

    a = float(input("Enter a value for a: "))
    b = float(input("Enter a value for b : "))

    if b == (2*a):
        print("Division error.")
    else:
        result = a / (b - (2*a))

        return result
   

print("The main program that tests for: a / (b - (2*a)): ")
print(mathFunc())    