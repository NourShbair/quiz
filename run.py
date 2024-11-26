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
    colored_print("Please Enter Your Username:",constants.MAGENTA,"center")
    username = input(constants.CENTER_SPACE)
    user = UserDataSheet(f"{username}")
    start_play(user)

def show_introduction():
    colored_print(constants.WELCOME_MSG,constants.CYAN,"")
    colored_print("""\n\n
    • You’ll answer 9 questions from 3 categories: Science, History, and Shows.\n
    • Questions range from Easy to Hard.\n
    • Each question has 4 options; type the number (1,2,3,or 4) of the correct answer and hit Enter.\n
    • You’ll earn full points for answering on the first try, half points on the second, and 0 points if you fail twice.\n
    """,constants.GREEN,"center")
    
    colored_print("Let’s see how much you know. Good luck! 🎯",constants.WHITE,"center")

"""
Starting point to execute
"""
main()

