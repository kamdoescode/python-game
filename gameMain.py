from instructions import display_instructions
display_instructions()

#COLLECTING + STORING PLAYER CODES-----------------------------
#creating a class for players and their codes
class Player:
    def __init__(self, name):
        self.name = name
        self.code = None
#input and storage of player code
    def set_code(self):
        while True:
            code = input(f"{self.name}, enter your 5-character code: ")
            if len(code) == 5:
                self.code = code
                break 
            print("Code must be exactly 5 characters. Try again.")
#create player objects
player1 = Player("Player 1")
player2 = Player("Player 2")

player1.set_code()

#HIDING PLAYER 1s INPUT USING OS MODULE-----------
import os
os.system('cls'if os.name == 'nt' else 'clear')
print("Player 1's code has been set and hidden")

#HIDING PLAYER 2s---------------------------------------
player2.set_code()
os.system('cls'if os.name == 'nt' else 'clear')
print("Player 2's code has been set and hidden")

#COLLECTING + CHECKING THE PLAYER GUESSES----------------------
def get_player_guess():
    return input("Enter your guess:")

def check_guess(player_code, guess):
    result = ""
    correct = 0
    for a, b in zip(player_code, guess):
        if a == b:
            #green for correct
            result += f"\033[92m{b}\033[0m"
            correct += 1
        else:
            #red for incorrect
            result += f"\033[91m{b}\033[0m"

    return f"Guess: {result} | Correct: {correct}"

def  play_game(player1_code, player2_code):
    player1_guesses = 0
    player2_guesses = 0

    while True:
        #Player 1s Turn
        guess = input("Player 1, enter your guess for Player 2's code: ")
        player1_guesses += 1
        if guess == player2_code:
            print(f"Correct! Player 1 guessed Player 2's code in {player1_guesses} attempts.")
            break 
        else:
            feedback = check_guess(player2_code, guess)
            print(feedback)
            print(f"Player 1 guesses so far: {player1_guesses}")

        #Player 2s Turn
        guess = input("Player 2, enter your guess for Player 1's code: ")
        player2_guesses += 1
        if guess == player1_code:
            print(f"Correct! Player 2 guessed Player 1's code in {player2_guesses} attempts.")
            break
        else:
            feedback = check_guess(player1_code, guess)
            print(feedback)
            print(f"Player 2 guesses so far: {player2_guesses}")

    return player1_guesses, player2_guesses

#start the game and store the number of guesses for each player
player1_guesses, player2_guesses = play_game(player1.code, player2.code)


    

