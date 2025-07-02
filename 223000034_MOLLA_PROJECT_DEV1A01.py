import random

def PlayGuessingGame():

    print("----NUMBER GUESSING GAME----")
    print("Both the user and Computer start off with 50 points each.")
    print("You will have 5 attempts. Each wrong answer deducts 10 points. ")
    userName = input("User, what is your name? ")

    while True:
        print(userName, "do you want to guess first? (yes/no): ")
        userFirst = input().lower()
    
        if userFirst == "yes":
            print("Okay. You will guess first.")
            userScore = userTurn()
            print(userName, "'s score is",userScore)
            print("Computer's turn.")
            computerScore = computerTurn()
            print("Computer's score is", computerScore)
            break
        elif userFirst == "no":
            print("Okay. Computer will guess first.")
            computerScore = computerTurn()
            print("Computer's score is", computerScore)
            print(userName, "'s turn")
            userScore = userTurn()
            print(userName, "'s score is", userScore)
            break
        else:
            print("Invalid choice. please choose 'yes' or 'no'.")
        
    print("----GAME OVER----")
    print(userName, "'s score is", userScore)
    print("Computer's score is", computerScore)

    if userScore > computerScore:
        print(userName, "won this game", userScore, ":", computerScore, "!", "Great stuffs!")
        print("Thanks for playing chief!")
    elif userScore < computerScore:
        print("Computer won this game", computerScore, ":", userScore, "!", "Better luck next time chief!")
        print("Thanks for playing chief!")
    else:
        print("It's a tie!", userScore, ":", computerScore)
        print("Thanks for playing chief!")

    while True:
        playAgain = input("Would you like to play again? (yes/no): ").lower()
        if playAgain == "yes" :
            PlayGuessingGame()
            break
        elif playAgain == "no":
            print("See you next time. Thanks for playing chief!")
            break
        else:
            print("Invalid choice. Please choose 'yes' or 'no' .")

def computerTurn():
    while True:
        try:
            userNumber = int(input("Enter a number for Computer to guess: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10: ")
    print("You have picked a number. Computer will try to guess it!")

    attemptsRemaining = 5
    while attemptsRemaining > 0:
        computerGuess = random.randint(0,10)
        print("Computer guesses ", computerGuess)
        if computerGuess == userNumber:
            print("WOW. Computer has guessed it correctly in", (6 - attemptsRemaining), "attempts!")
            return 50 - (5 - attemptsRemaining) * 10
        elif computerGuess > userNumber:
            print("Computer's guess was too high. Trying again.")
        else:
            print("Computer's guess was too low. Trying again.")
        attemptsRemaining -= 1

    print("Computer couldn't guess the number, which was", userNumber)
    
    return 0            

def userTurn():
    computerNumber = random.randint(0,10)
    print("Computer has picked a number between 0 and 10. Try to guess what it is!")

    attemptsRemaining = 5
    while attemptsRemaining > 0:
        while True:
            try:
                userGuess = int(input("Guess the number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 10: ")

        if userGuess == computerNumber:
            print("Congratulations chief! You have guessed it correctly in", (6- attemptsRemaining), "attempts!")
            return 50 - (5 - attemptsRemaining) * 10
        elif userGuess < computerNumber:
            print("Your guess was too low, try again chief!", (attemptsRemaining - 1), "attempts remaining!")
        else:
            print("Your guess was too high, try again chief!", (attemptsRemaining - 1), "attempts remaining!")
        attemptsRemaining -= 1

    print("You couldn't guess the number. Computer's number was ", computerNumber)         
              
    return 0

PlayGuessingGame() 
