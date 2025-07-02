'''1.	Write a PYTHON program that stores the information – (Book Name, Author Name, ISBN Number, and Number of pages) in a Dictionary. 
Your program should prompt the user to enter the information and your program should store it in a dictionary. The dictionary should be displayed.'''

#initialise variables for user input
bookName = "Name of book"
authorName = "Author's name"
isbnNumber = "Book's ISBN number (10)"
numberOfPages = "Number of book pages"

dictionary = {                                            #store values in a key:value pairs
bookName : str(input("Enter the name of the book: ")), 
authorName : str(input("Enter the name of the author: ")),
isbnNumber : int(input("Enter the book's ISBN (10 digit) number: ")),
numberOfPages : int(input("Enter the number of book pages: "))
}

print(dictionary)
