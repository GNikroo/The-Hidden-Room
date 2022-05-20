def game_logo():
    """
    Print logo.
    """
    file = open("logo.txt", encoding="utf8")
    content = file.read()
    print(content)
    file.close()


def initialize_game():
    """
    Begin game and present first question.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    print("Do you\033[1;32m investigate\033[m the corner or take to the\033[1;33m corridor\033[m?")
    first_question()


def first_question():
    """
    Runs first question:
    Investigate corner or corridor
    """
    user_input = "invalid"
    while user_input == "invalid":
        choice1 = input("Enter your choice: \n")
        if choice1 == "corridor":
            print("You choose to take the\033[1;33m corridor\033[m\n")
            user_input = "valid"
            first_corridor()
        elif choice1 == "investigate":
            print("You choose to\033[1;32m investigate\033[m the corner.\n")
            user_input = "valid"
            first_investigate()
        else:
            print("Something howls in the distance.\nPlease choose\033[1;32m investigate\033[m or take the\033[1;33m corridor\033[m.\n")


def first_corridor():
    """
    Reads the dungeon script for the corridor.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [11, 12, 13]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    game_over()


def first_investigate():
    """
    Reads the dungeon script for the corner.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [16, 17, 18, 19, 20, 21, 22, 23, 24]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    print("Do you\033[1;35m walk\033[m towards the other side of the room or keep to the\033[1;36m walls\033[m?")
    second_question()


def second_question():
    """
    Runs second question:
    Keep walking or hug the walls.
    """
    user_input = "invalid"
    while user_input == "invalid":
        choice2 = input("Enter your choice: \n")
        if choice2 == "walls":
            print("You choose to keep to the\033[1;36m walls\033[m.\n")
            user_input = "valid"
            second_walls()
        elif choice2 == "walk":
            print("You choose to\033[1;35m walk\033[m to the other side.\n")
            user_input = "valid"
            second_walk()
        else:
            print("Small stones fall from the ceiling up ahead.\nPlease choose to\033[1;35m walk\033[m or hug the\033[1;36m walls\033[m.\n")


def second_walls():
    """
    Reads the dungeon script for hugging the walls.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [27, 28, 29, 30, 31, 32, 33]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    print("Do you\033[1;31m investigate\033[m the opening or\033[1;34m continue\033[m along the perimeter?")
    walls_question()


def walls_question():
    """
    Runs walls follow up question:
    Investigate the opening or continue.
    """
    user_input = "invalid"
    while user_input == "invalid":
        choice2 = input("Enter your choice: \n")
        if choice2 == "investigate":
            print("You choose to\033[1;31m investigate\033[m the opening.\n")
            user_input = "valid"
            walls_investigate()
        elif choice2 == "continue":
            print("You choose to\033[1;34m continue\033[m to the other side.\n")
            user_input = "valid"
            # walls_continue()
        else:
            print("Something bangs in the distance.\nPlease choose to\033[1;31m investigate\033[m or \033[1;34m continue\033[m.\n")


def walls_investigate():
    """
    Reads the dungeon script for investigating the opening.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [36, 37, 38, 39]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    print("Do you\033[1;33m approach\033[m the figure or\033[1;35m leave\033[m?")


def second_walk():
    """
    Reads the dungeon script for walking to the other side.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [70, 71, 72, 73, 76, 77, 78, 79, 81, 82, 83, 84, 85, 86]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    game_over()


# def sarcophagus_no_compass():


# def sarcophagus_yes_compass():


def game_over():
    """
    Initialize game over.
    """
    file = open("game-over.txt", encoding="utf8")
    content = file.read()
    print(content)
    file.close()
    user_input = "invalid"
    while user_input == "invalid":
        restart_game = input("Enter y/n: \n")
        if restart_game == "y":
            user_input = "valid"
            initialize_game()
        elif restart_game == "n":
            print("Until next time...")
            user_input = "valid"
            break
        else:
            print("You feel the chill of icy breath at your back.\nPlease type y or n")


def main():
    """
    Run program functions
    """
    game_logo()
    initialize_game()


main()
