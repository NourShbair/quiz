# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from quiz_app.model.sheet import UserDataSheet
from quiz_app.controller.game import start_play
from quiz_app.view.printer import colored_print
from quiz_app.view.printer import colored_print_fb
from quiz_app.view import constants


def main():
    """
    Run all program function
    """
    show_introduction()
    print("\n")
    colored_print("Please Enter Your Username:", constants.MAGENTA, "center")
    while True:
        username = input(constants.CENTER_SPACE)
        if len(username) > 20:
            print("\n")
            colored_print(
                "Invalid username, please choose a username contains "
                "less than 20 charachters",
                constants.RED,
                "center",
            )

        elif validate_username(username):
            user = UserDataSheet(f"{username}")
            user_data = user.get_user_data()
            # Check if the user already finish all levels
            if user_data.question_number > 9:
                points = user_data.points
                print("\n")
                colored_print(
                    "You've already finish all the levels, "
                    "Enter R to restart the quiz."
                    , constants.GREEN, "center")
                entered_value = input(constants.CENTER_SPACE)
                if entered_value == "R":
                    restart_quiz(user)
            else:
                start_play(user)
        else:
            print("\n")
            colored_print(
                "Invalid username, please choose a username contains "
                "at least one character",
                constants.RED,
                "center",
            )


def validate_username(name):

    for char in name:
        if char.isalpha():
            return True
    return False


def restart_quiz(user):
    user_data = user.get_user_data()
    user_data.points = 0
    user_data.question_number = 1
    user.update_user_sheet(user_data)
    start_play(user)


def show_introduction():
    colored_print(constants.WELCOME_MSG, constants.CYAN, "")
    colored_print(
        """\n\n
    • Answer 9 questions from 3 categories: Science, History, and Shows.\n
    • Questions range from Easy to Hard.\n
    • Each question has 4 options.\n
    • Enter the number of your answer (1-4) and press Enter.\n
    • Earn full points on the first try,half on the second,0 after two fails.\n
    """,
        constants.GREEN,
        "center",
    )

    colored_print(
        "Let’s see how much you know. Good luck! 🎯", constants.WHITE, "center"
    )


if __name__ == "__main__":
    """
    Starting point to execute
    """
    main()
