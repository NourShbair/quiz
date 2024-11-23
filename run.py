# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from quiz_app.model.sheet import QuestionSheet
from quiz_app.model.sheet import UserDataSheet

def get_question(question_number):
    """
    This method to retrieve a random question from a specified sheet
    depending on question number, and using difficulty level and question category
    """
    print("Retrieving question...\n")
    level_cat_arr = [("easy","science"),("easy","history"),("easy","shows"),
    ("medium","science"),("medium","history"),("medium","shows"),
    ("hard","science"),("hard","history"),("hard","shows")]
    level,category= level_cat_arr[question_number-1]
    question = QuestionSheet(level, category)
    retrieved_question = question.get_random_question()
    print(retrieved_question)

def main():
    """
    Run all program function
    """
    username = input("Please Enter Your Username:\n")
    user = UserDataSheet(f"{username}")
    user_data = user.get_user_data()
    get_question(user_data.question_number)
    

"""
Starting point to execute
"""
print("Welcome to The Best Quiz App\n")
main()
