'''8.	Write a Python program to display the sequence: -3, -6, -9, -12, … to the 50th term. Hint: use a while loop for this. [10 marks]'''

term = 0   #number of terms
valueT = 0      #value of term

while term < 50:   #term number 50
    valueT += (1 * -3)  #arithmetic sequence, difference of -3 
    term += 1      #increasing term number by 1 each time     
    print(valueT)
   


