def game_logo():
    """
    Print logo.
    """
    file = open("logo.txt")
    content = file.read()
    print(content)
    file.close()


def initialize_game():
    """
    Begin game and present first choice.
    """
    file = open("dungeon.txt")
    read_lines = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i, spec_line in enumerate(file):
        if i in read_lines:
            print(spec_line)
    file.close()
    print("Do you investigate the\033[1;32m corner\033[m or take to the\033[1;33m corridor\033[m?")
    first_choice()


def first_choice():
    """
    Runs response to the first question:
    Investigate corner or corridor
    """
    user_input = "invalid"
    while user_input == "invalid":
        choice1 = input("Enter your choice: \n")
        if choice1 == "corridor":
            print("You choose to take the\033[1;33m corridor\033[m\n")
            user_input = "valid"
        elif choice1 == "corner":
            print("You choose to investigate the\033[1;32m corner\033[m\n")
            user_input = "valid"
        else:
            print("Something howls in the distance.\nPlease choose either the\033[1;32m corner\033[m or\033[1;33m corridor\033[m\n")


def main():
    """
    Run program functions
    """
    game_logo()
    initialize_game()


main()
