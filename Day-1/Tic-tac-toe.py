# # **Advanced Tic-Tac-Toe Game in Python**

# **Objective:** Create a terminal-based Tic-Tac-Toe game in Python with additional features and functionalities.

# ### **Requirements:**

# 1. The game should support two players taking turns to play Tic-Tac-Toe on a 3x3 grid.
# 2. The game should display the current state of the board after each move.
# 3. The game should correctly determine when a player has won, lost, or when it's a tie.
# 4. Players should be able to input their moves by specifying the row and column they want to place their symbol (e.g., "A1" for the top-left cell).
# 5. The game should handle invalid inputs gracefully and prompt the user to enter a valid move.

# ### **Advanced Features:**

# Choose at least three of the following advanced features to implement in the game:

# 1. **Multiple Board Sizes:** Allow players to choose the size of the game board (e.g., 3x3, 4x4, or even larger). Ensure that the game logic adapts to the selected board size.
# 2. **Scoring System:** Introduce a scoring system that keeps track of players' scores across multiple rounds or games. Display the scores at the end of each game.
# 3. **Undo and Redo Moves:** Implement the ability for players to undo and redo their moves. This feature should allow players to navigate the game's history.
# 4. **Game History:** Store the history of each move in a game and allow players to review previous moves or restart the game from a specific point.
# 5. **Customizable Winning Patterns:** Allow players to customize the winning patterns (e.g., require four symbols in a row instead of three) and adapt the game rules accordingly.
# 6. **Save and Load Games:** Enable players to save the current game state to a file and load it later to resume the game.


# ### **Documentation and Testing:**

# 1. Provide clear instructions on how to play the game, including explanations of advanced features.
# 2. Test the game thoroughly to ensure that all features work as expected and that the game is user-friendly.

# ### **Code Structure and Style:**

# 1. Organize the code into well-defined functions and classes to ensure readability and modularity.
# 2. Handle user input gracefully, providing meaningful error messages for invalid input.


# --------------------------pathway-----------
# -----------------------------------------------------------------------

# Here's a high-level outline of how you can structure your code:

# Code Structure:
# Board Class:

# Create a class to represent the game board. This class should handle operations related to the board, such as:
# Initializing the board with a given size (e.g., 3x3, 4x4).
# Displaying the current state of the board.
# Checking for a win or a tie.
# Making a move and updating the board.
# Handling undo and redo moves.
# Keeping track of move history.
# Player Class:

# Create a class to represent a player. This class should handle operations related to the player, such as:
# Storing the player's symbol (X or O).
# Keeping track of the player's score.
# Handling player moves (input validation).
# Game Class:

# Create a class to manage the game flow. This class should handle operations related to the overall game, such as:
# Starting a new game.
# Managing player turns.
# Determining the winner.
# Managing the game history.
# Handling saving and loading games.
# User Interface:

# Implement a user interface for interacting with the game. This could be a text-based interface where players input their moves.
# Advanced Features:

# Implement the selected advanced features based on the outline provided in the requirements.
# Style and Documentation:
# Use meaningful variable and function names to make the code self-explanatory.
# Add comments to explain complex logic or algorithms.
# Provide clear instructions on how to play the game, including how to use advanced features.
# Include a docstring for each class and function to describe their purpose and usage.
# Testing:
# Write test cases to ensure that each component (Board, Player, Game) functions as expected.
# Test various scenarios, including normal gameplay, edge cases, and usage of advanced features.
# User Interaction:
# Implement a user interface for interacting with the game. This could be a simple command-line interface where players input their moves (e.g., "A1" for the top-left cell).

# Save and Load Games:
# Implement the feature to save the current game state to a file and load it later to resume the game.

# Remember to break down the project into smaller tasks and tackle them one at a time. Start with the basic functionality (e.g., creating the board, handling player moves), and then gradually add the advanced features. Test each component thoroughly before moving on to the next.

# Good luck with your project! If you have specific questions or need help with specific parts of the implementation, feel free to ask.



# ----------------------------------------------------------------


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False

    def display_board(self):
        print('---------')
        for row in self.board:
            print('|', end='')
            for cell in row:
                print(cell, end='|')
            print('\n---------')

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.check_winner(row, col)
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Invalid move. Cell is already occupied.')

    def check_winner(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 3):
                r, c = row + i * dr, col + i * dc
                if 0 <= r < 3 and 0 <= c < 3 and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            for i in range(1, 3):
                r, c = row - i * dr, col - i * dc
                if 0 <= r < 3 and 0 <= c < 3 and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 3:
                self.game_over = True
                print(f'Player {self.current_player} wins!')
                return

        if all(cell != ' ' for row in self.board for cell in row):
            self.game_over = True
            print('It\'s a tie!')

    def play(self):
        while not self.game_over:
            self.display_board()
            move = input(f'Player {self.current_player}, enter your move (row col): ')
            try:
                row, col = map(int, move.split())
                if 0 <= row < 3 and 0 <= col < 3:
                    self.make_move(row, col)
                else:
                    print('Invalid input. Row and column must be between 0 and 2.')
            except ValueError:
                print('Invalid input. Please enter two integers separated by a space.')

if __name__ == '__main__':
    game = TicTacToe()
    game.play()
