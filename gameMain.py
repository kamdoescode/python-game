import rich
from rich import print
from rich.panel import Panel 
from rich.text import Text

instructions = Text.assemble(
    ("Welcome to Code Breaker!", "bold magenta"),
    "\n\nPlayer 1: Create a secret code",
    "\nPlayer 2: Try to guess the code",
    "\n\nGoodluck!"
)

print(Panel(instructions, title = "Game Instructions",
border_style= "bright_blue"))


