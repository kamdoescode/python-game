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
        self.code = input(f"{self.name}, enter your secret code:")

player1 = Player("Player 1")
player2 = Player("Player 2")

player1.set_code()





