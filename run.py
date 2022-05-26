"""The Hidden Room game"""
import time
import sys
import os


class Choice:
    """
    Choice class.
    """
    def __init__(self, first_choice, second_choice):
        self.first_choice = first_choice
        self.second_choice = second_choice


class Life:
    """
    Life class.
    """
    life = 3

    @staticmethod
    def reduce_life():
        """
        Reduce life by one.
        """
        Life.life -= 1
        if Life.life > 0:
            print("\033[1;30;41mYou have " + str(Life.life) + " lives\033[m\n")
        else:
            time.sleep(1)
            game_over()


def read_script(lines):
    """
    Read specified lines from dungeon file.
    """
    time.sleep(1)
    file = open("dungeon.txt", encoding="utf8")
    for i, spec_line in enumerate(file):
        if i in lines:
            print(spec_line)
    file.close()
    time.sleep(1)


def question_template(choice):
    """
    Offer choices for player.
    """
    while True:
        user_input = input("Enter your choice: \n")
        if user_input.lower() == choice.first_choice:
            time.sleep(1)
            print(f"You chose {user_input.lower()}." + "\n")
            return choice.first_choice
        elif user_input.lower() == choice.second_choice:
            time.sleep(1)
            print(f"You chose {user_input.lower()}." + "\n")
            return choice.second_choice
        else:
            time.sleep(.5)
            print("Something howls in the distance.\n")


def game_logo():
    """
    Print logo.
    """
    file = open("logo.txt", encoding="utf8")
    content = file.read()
    print(content)
    file.close()
    time.sleep(1)


def scene1():
    """
    Begin game and present first question.
    """
    print("\033[1;30;41mYou have " + str(Life.life) + " lives\033[m\n")
    lines = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    read_script(lines)
    time.sleep(1)
    print("Do you\033[1;31m investigate\033[m the corner\n")
    print("or take to the\033[1;33m corridor\033[m?\n")
    scene1_choice()


def scene1_choice():
    """
    Runs first question:
    Investigate corner or corridor
    """
    choice = Choice("corridor", "investigate")
    user_input = question_template(choice)
    if user_input == choice.first_choice:
        corridor()
    else:
        scene1_investigate()


def corridor():
    """
    Reads the dungeon script for the corridor.
    """
    lines = [11, 12, 13]
    read_script(lines)
    time.sleep(1)
    Life.reduce_life()
    print("Do you\033[1;31m investigate\033[m the corner\n")
    print("or take to the\033[1;33m corridor\033[m?\n")
    scene1_choice()


def scene1_investigate():
    """
    Reads the dungeon script for the corner.
    """
    lines = [16, 17, 18, 19, 20, 21, 22, 23, 24]
    read_script(lines)
    time.sleep(1)
    print("Do you\033[1;32m walk\033[m towards the other side of the room\n")
    print("or keep to the\033[1;34m walls\033[m?\n")
    scene2()


def scene2():
    """
    Runs second question:
    Keep walking or hug the walls.
    """
    choice = Choice("walls", "walk")
    user_input = question_template(choice)
    if user_input == choice.first_choice:
        scene3()
    else:
        walk()


def scene3():
    """
    Reads the dungeon script for hugging the walls.
    """
    lines = [27, 28, 29, 30, 31, 32, 33]
    read_script(lines)
    time.sleep(1)
    print("Do you\033[1;35m investigate\033[m the opening\n")
    print("or\033[1;31m continue\033[m along the perimeter?\n")
    scene3_choice()


def scene3_choice():
    """
    Runs walls follow up question:
    Investigate the opening or continue to perimeter.
    """
    choice = Choice("investigate", "continue")
    user_input = question_template(choice)
    if user_input == choice.first_choice:
        scene3_investigate()
    else:
        scene3_continue()


def scene3_investigate():
    """
    Reads the dungeon script for investigating the opening.
    """
    lines = [36, 37, 38, 39]
    read_script(lines)
    time.sleep(1)
    print("Do you\033[1;33m approach\033[m the figure\n")
    print("or\033[1;32m leave\033[m?\n")
    scene4()


def scene4():
    """
    Runs wall investigation follow up question:
    Approach the figure or leave.
    """
    choice = Choice("approach", "leave")
    user_input = question_template(choice)
    if user_input == choice.first_choice:
        approach()
    else:
        leave()


def approach():
    """
    Reads the dungeon script for approaching the figure.
    """
    lines = [42, 43, 44, 45, 46, 47, 48]
    read_script(lines)
    time.sleep(1)
    lines = [50, 51, 52, 53]
    read_script(lines)
    time.sleep(1)
    scene5()


def leave():
    """
    Reads the dungeon script for leaving the figure alone.
    """
    lines = [56, 57, 58, 59, 60, 61]
    read_script(lines)
    time.sleep(1)
    scene6()


def scene3_continue():
    """
    Reads the dungeon script for continuing to the perimeter.
    """
    lines = [50, 51, 52, 53]
    read_script(lines)
    time.sleep(1)
    lines = [70, 71, 72]
    read_script(lines)
    time.sleep(1)
    lines = [75, 76, 77, 78, 79, 80]
    read_script(lines)
    time.sleep(1)
    Life.reduce_life()
    print("Do you\033[1;35m investigate\033[m the opening\n")
    print("or\033[1;31m continue\033[m along the perimeter?\n")
    scene3_choice()


def walk():
    """
    Reads the dungeon script for walking to the other side.
    """
    lines = [64, 65, 66, 67]
    read_script(lines)
    time.sleep(1)
    lines = [70, 71, 72, 73]
    read_script(lines)
    time.sleep(1)
    scene6()


def scene6():
    """
    Reads the dungeon script to approach the sarcophagus
    without a compass.
    """
    lines = [75, 76, 77, 78, 79, 80]
    read_script(lines)
    time.sleep(1)
    Life.reduce_life()
    print("Do you\033[1;32m walk\033[m towards the other side of the room\n")
    print("or keep to the\033[1;34m walls\033[m?\n")
    scene2()


def scene5():
    """
    Reads the dungeon script to approach the sarcophagus
    with the compass.
    """
    lines = [83, 84, 85, 86, 87]
    read_script(lines)
    time.sleep(1)
    print("Do you give in to temptation and\033[1;34m look\033[m\n")
    print("or do you\033[1;35m escape\033[m?\n")
    scene5_choice()


def scene5_choice():
    """
    Runs sarcophagus question:
    Look at what emerges or escape.
    """
    choice = Choice("look", "escape")
    user_input = question_template(choice)
    if user_input == choice.first_choice:
        look()
    else:
        escape()


def look():
    """
    Reads the dungeon script to look at what
    emerges.
    """
    lines = [90, 91, 92, 93, 94, 95]
    read_script(lines)
    time.sleep(1)
    lines = [97, 98]
    read_script(lines)
    time.sleep(1)
    lines = [100, 101, 102, 103, 104]
    read_script(lines)
    time.sleep(1)
    lines = [106, 107, 108, 109]
    read_script(lines)
    time.sleep(1)
    lines = [111, 112, 113]
    read_script(lines)
    time.sleep(1)
    lines = [115]
    read_script(lines)
    time.sleep(1)
    Life.reduce_life()
    print("Do you give in to temptation and\033[1;34m look\033[m\n")
    print("or do you\033[1;35m escape\033[m?\n")
    scene5_choice()


def escape():
    """
    Reads the dungeon script to escape.
    """
    lines = [118, 119, 120, 121]
    read_script(lines)
    time.sleep(1)
    lines = [123, 124]
    read_script(lines)
    time.sleep(1)
    lines = [126, 127, 128, 129, 130]
    read_script(lines)
    time.sleep(1)
    lines = [132]
    read_script(lines)
    time.sleep(1)
    lines = [134, 135, 136, 137]
    read_script(lines)
    time.sleep(1)
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
            Life.life = 3
            main()
        elif restart_game == "n":
            user_input = "valid"
            print("Until next time...")
            time.sleep(2)
            clear_console()
            sys.exit()
        else:
            print("You feel the chill of icy breath at your back.\n")
            print("Please type y or n\n")


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
        restart_game = input("Care to play again? Enter y/n: \n")
        if restart_game == "y":
            user_input = "valid"
            Life.life = 3
            main()
        elif restart_game == "n":
            user_input = "valid"
            print("Until next time...")
            time.sleep(2)
            clear_console()
            sys.exit()
        else:
            print("Your bed creaks under the weight of your hoard.\n")
            print("Please type y or n\n")


def clear_console():
    """
    Clear console after choosing to exit game.
    """
    user_os = sys.platform
    prefixes = ['win32', 'cygwin', 'os2emx']
    result = user_os.startswith(tuple(prefixes))
    if result:
        return os.system('cls')
    else:
        return os.system('clear')


def main():
    """
    Run program functions
    """
    clear_console()
    game_logo()
    scene1()


main()
