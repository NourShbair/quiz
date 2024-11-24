# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from quiz_app.model.sheet import UserDataSheet
from quiz_app.controller.game import start_play


def main():
    """
    Run all program function
    """
    username = input("Please Enter Your Username:\n")
    user = UserDataSheet(f"{username}")
    start_play(user)

"""
Starting point to execute
"""
print("Welcome to The Best Quiz App\n")
main()
