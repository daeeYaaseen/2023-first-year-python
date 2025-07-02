import random

def play_guess_number_game():
    print("GUESS NUMBER GAME")
    name = input("Hey, what is your name: ")
    print(f"{name}, do you want to go first? (yes/no): ")
    user_first = input().lower() == "yes"

    user_score = 50
    robot_score = 50

    if user_first:
        print("Alright, cool! You go first.")
        user_secret_number = random.randint(0, 10)
        robot_guesses_user_number(user_secret_number, name, user_score, robot_score)
    else:
        print("Alright, cool! I'll go first.")
        robot_secret_number = random.randint(0, 10)
        user_guesses_robot_number(robot_secret_number, name, user_score, robot_score)

def user_guesses_robot_number(robot_secret_number, name, user_score, robot_score):
    print(f"Well {name}, I have picked a number between the range of 0 and 10. Now go ahead and guess it!")
    attempts = 5

    while attempts > 0:
        user_guess = int(input("Guess the number: "))

        if user_guess == robot_secret_number:
            print(f"Congratulations! You have guessed it correctly in {6 - attempts} attempts!")
            user_score -= (5 - attempts) * 10
            break
        elif user_guess < robot_secret_number:
            print(f"{name}, you went too low. Try again. {attempts - 1} attempts left!")
        else:
            print(f"{name}, you went too high. Try again. {attempts - 1} attempts left!")

        attempts -= 1

    print(f"Your score is {user_score}.")
    print("Well, it's my turn.")

    robot_guesses_user_number(user_score, name, user_score, robot_score)

def robot_guesses_user_number(user_secret_number, name, user_score, robot_score):
    print(f"{name}, input your own secret number: ")
    robot_guesses = 5
    low = 0
    high = 10

    while robot_guesses > 0:
        robot_guess = random.randint(low, high)
        print(f"Well Robot, I guess your number is {robot_guess}.")

        if robot_guess == user_secret_number:
            print(f"Congratulations to myself! I have guessed it correctly in {6 - robot_guesses} attempts!")
            robot_score -= (5 - robot_guesses) * 10
            break
        elif robot_guess < user_secret_number:
            print(f"Robot, you went too low. Try again. {robot_guesses - 1} attempts left!")
            low = robot_guess + 1
        else:
            print(f"Robot, you went too high. Try again. {robot_guesses - 1} attempts left!")
            high = robot_guess - 1

        robot_guesses -= 1

    print(f"My score is {robot_score}.")
    print(f"{name}, you won this game {user_score}:{robot_score}. Not bad. Let's play again!")

# Run the game
play_guess_number_game()
