#INSTRUCTIONS--------------------------
# learned about rich via: https://medium.com/@ahmedharabi/get-started-with-the-python-rich-library-2736b1b57941
import rich
from rich import print
from rich.panel import Panel 
from rich.text import Text

instructions = Text.assemble(
    ("Welcome to Code Breaker!", "bold magenta"),
    "\n\n\n1.Assign a Player 1 and a Player 2"
    "\n\n2.Player 1 create a 6 digit code of letters and numbers"
    "\n\n3.Player 2, try to guess the code"
    "\n>>>A guess of the right character in the right position will turn Green"
    "\n>>>A guess of the right character in the wrong position will turn Yellow"
    "\n>>>Your amount of guesses will be tracked in the top right corner"
    "\n\n4.When the code is fully guessed correctly, the players will switch"
    "\n\n5.Whoever guesses the code in the least amount of tries wins"
    "\n\n\nGoodluck!"
)

print(Panel(instructions, title = "Game Instructions",
border_style= "bright_blue"))
#----------------------------------------------------

#COLLECTING + STORING PLAYER CODES-----------------------------

#creating a class for players and their codes
class Player:
    def __init__(self, name):
        self.name = name
        self.code = None
#input and storage of player code
    def set_code(self):
        self.code = input(f"{self.name}, enter your secret code:")

player1 = Player("Player 1")
player2 = Player("Player 2")

player1.set_code()





