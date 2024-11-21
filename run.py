# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quiz_questions')

def get_question():
    print("Retrieving question...\n")
    easy_science = SHEET.worksheet("easy_science").get_all_values()
    question = easy_science[2][0]
    return question
def main():
    """
    run all program function
    """
    retrieved_question = get_question()
    print(retrieved_question)


print("Welcome to The Best Quiz App")
main()
