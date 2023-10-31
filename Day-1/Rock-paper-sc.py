# **Objective:** Implement a command-line game of Rock, Paper, Scissors in Python.--write Code--

# ### **Requirements:**

# 1. The game should be between a user and the computer.
# 2. The game should ask the user for their choice (rock, paper, or scissors).
# 3. The computer's choice should be selected randomly.
# 4. The game should compare the two choices and determine the winner. The rules for winning are as follows:
#     - Rock beats Scissors (Rock crushes Scissors)
#     - Scissors beats Paper (Scissors cut Paper)
#     - Paper beats Rock (Paper covers Rock)
# 5. The game should keep track of the score and display it at the end of each round. The score display should include the number of rounds the user has won, the number of rounds the computer has won, and the number of draws.
# 6. The game should continue in a loop until the user decides to quit.
# 7. The user should be able to quit the game at any point.

# ### **Extra Challenge:**

# For students who finish early or want an extra challenge, consider adding one or more of the following features:

# 1. Add additional valid moves, such as Lizard and Spock (as in the extended version of the game popularized by "The Big Bang Theory" TV show). Update the winning rules to accommodate these new moves.
# 2. Add a simple graphical user interface (GUI) using a library such as tkinter. The GUI should display the choices for the user and the computer, show the current score, and provide buttons for the user to make their choice or quit the game.
# 3. Save the scores to a file and load them when the game starts. This way, scores can persist across multiple game sessions.

# ## Ensure the following thing :

# 1. Functionality: Does the program behave as expected and adhere to the requirements.
# 2. Code Style: Is the code well-structured into functions? Is the code easy to read and understand?
# 3. Robustness: Does the program handle invalid user input gracefully, such as inputs that are not "rock", "paper", or "scissors"?





import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors), or 'q' to quit: ").lower()
        if user_choice in ['rock', 'paper', 'scissors', 'q']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'q' to quit.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_round():
    user_choice = get_user_choice()
    if user_choice == 'q':
        return 'quit', None, None

    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    return winner, user_choice, computer_choice

def print_round_result(winner, user_choice, computer_choice):
    if winner == 'draw':
        print(f"Both chose {user_choice}. It's a draw!")
    elif winner == 'user':
        print(f"You chose {user_choice} and computer chose {computer_choice}. You win!")
    else:
        print(f"You chose {user_choice} and computer chose {computer_choice}. Computer wins.")

def main():
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        winner, user_choice, computer_choice = play_round()

        if winner == 'quit':
            break

        print_round_result(winner, user_choice, computer_choice)

        if winner == 'user':
            user_wins += 1
        elif winner == 'computer':
            computer_wins += 1
        else:
            draws += 1

        print(f"Score - User: {user_wins}, Computer: {computer_wins}, Draws: {draws}\n")

if __name__ == "__main__":
    main()



# This code defines a command-line Rock, Paper, Scissors game in Python. Here's how it works:

# The get_user_choice function prompts the user to enter their choice and validates it.
# The get_computer_choice function randomly selects the computer's choice.
# The determine_winner function determines the winner based on the choices made by the user and the computer.
# The play_round function orchestrates a single round of the game, including getting user and computer choices, determining the winner, and handling a user's decision to quit.
# The print_round_result function prints the outcome of a round (draw, user wins, or computer wins).
# The main function is the entry point of the program. It manages the game loop, keeps track of scores, and prints the current score after each round.
# To play the game, run the script. Follow the prompts to enter your choice (rock, paper, or scissors). You can also type 'q' to quit the game at any time. The game will continue until you choose to quit.