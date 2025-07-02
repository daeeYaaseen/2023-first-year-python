'''(. Write a Python program that displays the sequence: 1, ½, 1/3, ¼, 1/5, … until this division converges to zero; test the convergence using 0.00001. 
Hint: the loop should stop when 1/n is less than or equal to 0.00001.'''


n = 1
value = 1/n

while value >= 0.00001:           #while loop will end once the value is less than 0.00001
    print("{:.5f}".format(value))  #format the value to 5 decimal places so it looks the same as our question (0.00001)
    value = 1/n
    n += 1                #increasing divisional value by one after each division occurs            

