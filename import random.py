import random

def play_game():
    print("GUESS NUMBER GAME")
    name = input("Hey, what is your name: ")
    print(f"{name}, do you want to guess first? (yes/no): ")
    user_first = input().lower() == 'yes'
    
    user_score = 50
    robot_score = 50
    
    if user_first:
        print("Alright, cool! You go first.")
        user_score = user_turn()
        print("Well, it's my turn.")
        robot_score = robot_turn()
    else:
        print("Alright, cool! I'll guess first.")
        robot_score = robot_turn()
        print("Well, it's your turn.")
        user_score = user_turn()
    
    print("Game Over!")
    print(f"{name}, your score is {user_score}.")
    print(f"My score is {robot_score}.")
    
    if user_score > robot_score:
        print(f"{name}, you won this game {user_score}:{robot_score}! Well done.")
    elif user_score < robot_score:
        print(f"{name}, I won this game {robot_score}:{user_score}! Better luck next time.")
    else:
        print("It's a tie! Good game, everyone.")
    
    play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        play_game()
    else:
        print("Thank you for playing!")

def user_turn():
    secret_number = random.randint(0, 10)
    print("I have picked a number between 0 and 10. Now go ahead and guess it!")
    
    attempts_left = 5
    while attempts_left > 0:
        guess = int(input("Guess the number: "))
        if guess == secret_number:
            print(f"Congratulations, you have guessed it correctly in {6 - attempts_left} attempts!")
            return 50 - (5 - attempts_left) * 10
        elif guess < secret_number:
            print(f"You went too low, try again. {attempts_left - 1} attempts left!")
        else:
            print(f"You went too high, try again. {attempts_left - 1} attempts left!")
        attempts_left -= 1
    
    print(f"Sorry, you couldn't guess the number. The secret number was {secret_number}.")
    return 0

def robot_turn():
    secret_number = int(input("Input your own secret number: "))
    print("Well, I have picked a number between 0 and 10. Now go ahead and guess it!")
    
    attempts_left = 5
    while attempts_left > 0:
        guess = random.randint(0, 10)
        print(f"I guess {guess}.")
        if guess == secret_number:
            print(f"Congratulations, I have guessed it correctly in {6 - attempts_left} attempts!")
            return 50 - (5 - attempts_left) * 10
        elif guess < secret_number:
            print("I went too low, trying again.")
        else:
            print("I went too high, trying again.")
        attempts_left -= 1
    
    print(f"I couldn't guess the number. Your secret number was {secret_number}.")
    return 0

play_game()
