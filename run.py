import time


def game_logo():
    """
    Print logo.
    """
    file = open("logo.txt", encoding="utf8")
    content = file.read()
    print(content)
    file.close()
    time.sleep(1)


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
    time.sleep(2)
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
            time.sleep(1)
            print("You choose to take the\033[1;33m corridor\033[m\n")
            user_input = "valid"
            first_corridor()
        elif choice1 == "investigate":
            time.sleep(1)
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
    time.sleep(2)
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
    time.sleep(2)
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
            time.sleep(1)
            print("You choose to keep to the\033[1;36m walls\033[m.\n")
            user_input = "valid"
            second_walls()
        elif choice2 == "walk":
            time.sleep(1)
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
    time.sleep(2)
    print("Do you\033[1;31m investigate\033[m the opening or\033[1;34m continue\033[m along the perimeter?")
    walls_question_1()


def walls_question_1():
    """
    Runs walls follow up question:
    Investigate the opening or continue.
    """
    user_input = "invalid"
    while user_input == "invalid":
        choice2 = input("Enter your choice: \n")
        if choice2 == "investigate":
            time.sleep(1)
            print("You choose to\033[1;31m investigate\033[m the opening.\n")
            user_input = "valid"
            walls_investigate()
        elif choice2 == "continue":
            time.sleep(1)
            print("You choose to\033[1;34m continue\033[m to the other side.\n")
            user_input = "valid"
            walls_continue()
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
    time.sleep(2)
    print("Do you\033[1;33m approach\033[m the figure or\033[1;35m leave\033[m?")
    walls_question_2()


def walls_question_2():
    """
    Runs wall investigation follow up question:
    Approach the figure or leave.
    """
    user_input = "invalid"
    while user_input == "invalid":
        choice2 = input("Enter your choice: \n")
        if choice2 == "approach":
            time.sleep(1)
            print("You choose to\033[1;31m approach\033[m the figure.\n")
            user_input = "valid"
            walls_investigate()
        elif choice2 == "leave":
            time.sleep(1)
            print("You choose to\033[1;34m leave\033[m.\n")
            user_input = "valid"
            walls_continue()
        else:
            print("The sound of shuffling footsteps echo nearby.\nPlease choose to\033[1;31m approach\033[m or \033[1;34m leave\033[m.\n")


def walls_approach():
    """
    Reads the dungeon script for approaching the figure.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [42, 43, 44, 45, 46, 47, 48]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [50, 51, 52, 53]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    time.sleep(2)
    sarcophagus_yes_compass()


def walls_leave():
    """
    Reads the dungeon script for leaving the figure alone.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [56, 57, 58, 59, 60, 61]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    time.sleep(2)
    sarcophagus_no_compass()


def walls_continue():
    """
    Reads the dungeon script for continuing to the perimeter.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [50, 51, 52, 53]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [70, 71, 72]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [75, 76, 77, 78, 79, 80]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()     
    time.sleep(2)
    game_over()


def second_walk():
    """
    Reads the dungeon script for walking to the other side.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [64, 65, 66, 67]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [70, 71, 72, 73]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    time.sleep(2)
    sarcophagus_no_compass()


def sarcophagus_no_compass():
    """
    Reads the dungeon script to approach the sarcophagus
    without a compass.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [75, 76, 77, 78, 79, 80]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    time.sleep(2)
    game_over()


def sarcophagus_yes_compass():
    """
    Reads the dungeon script to approach the sarcophagus
    with the compass.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [83, 84, 85, 86, 87]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    time.sleep(2)
    print("Do you give in to temptation and\033[1;31m look\033[m at what has emerged from the sarcophagus or do you\033[1;34m escape\033[m on?")
    sarcophagus_question()


def sarcophagus_question():
    """
    Runs sarcophagus question:
    Look at what emerges or escape.
    """
    user_input = "invalid"
    while user_input == "invalid":
        choice2 = input("Enter your choice: \n")
        if choice2 == "look":
            time.sleep(1)
            print("You choose to\033[1;31m look\033[m at what emerges.\n")
            user_input = "valid"
            sarcophagus_look()
        elif choice2 == "escape":
            time.sleep(1)
            print("You choose to\033[1;34m escape\033[m.\n")
            user_input = "valid"
            sarcophagus_escape()
        else:
            print("You hear your name on the breeze.\nPlease choose to\033[1;31m look\033[m or \033[1;34m escape\033[m.\n")


def sarcophagus_look():
    """
    Reads the dungeon script to look at what
    emerges.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [90, 91, 92, 93, 94, 95]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [97, 98]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [100, 101, 102, 103, 104]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [106, 107, 108, 109]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [111, 112, 113]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [115]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    time.sleep(2)
    game_over()


def sarcophagus_escape():
    """
    Reads the dungeon script to escape.
    """
    file = open("dungeon.txt", encoding="utf8")
    read_lines = [118, 119, 120, 121]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [123, 124]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [126, 127, 128, 129, 130]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [132]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    time.sleep(2)
    read_lines = [134, 135, 136, 137]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    time.sleep(2)
    win_game()  


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
        time.sleep(1)
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


def win_game():
    """
    Initialize game win.
    """
    file = open("win-game.txt", encoding="utf8")
    content = file.read()
    print(content)
    file.close()
    user_input = "invalid"
    while user_input == "invalid":
        time.sleep(1)
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
