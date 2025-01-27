#INSTRUCTIONS--------------------------
def display_instructions():

    import rich
    from rich import print
    from rich.panel import Panel 
    from rich.text import Text

    instructions = Text.assemble(
        ("Welcome to Code Breaker!", "bold magenta"),
        "\n\n\n1.Assign a Player 1 and a Player 2"
        "\n\n2.Each player create a 5 digit code of letters and numbers"
        "\n\n3.Players, take turns guessing the code"
        "\n>>>A guess of the right character in the right position will turn Green"
        "\n>>>A guess of the wrong character in wrong position will turn Red"
        "\n\n5.Whoever guesses the code first wins"
        "\n\n\nGoodluck!"
    )

    print(Panel(instructions, title = "Game Instructions",
    border_style= "bright_blue"))
