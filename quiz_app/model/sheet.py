import gspread
from google.oauth2.service_account import Credentials
from random import randrange

from .question import Question
from .user import User

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]


class Sheet:
    """
    This class for google Sheet object,
    when passing the sheet name for the constructor, call the connect function:
    which has the suitable commands to access the sheet
    as well, this class contins a function to retrieve all data from
    the appropriate worksheet
    """

    def __init__(self, name):
        self.name = name
        self.connect()

    def get_all_values(self):
        return self.connetion.worksheet(self.name).get_all_values()

    def connect(self):
        CREDS = Credentials.from_service_account_file("creds.json")
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        self.connetion = GSPREAD_CLIENT.open("quiz_questions")


class QuestionSheet(Sheet):
    """
    This class for QuestionSheet object which extends Sheet class
    so it is a subclass from superclass "Sheet"
    Its constructor contains level difficulty (easy, medium, hard)
    and category (science, history, show)
    It contains a function for retrieving a random question from
    the appropriate worksheet
    depending on its name (which is level_category)
    """

    def __init__(self, level, category):
        self.level = level
        self.category = category
        self.get_name()
        super().__init__(self.name)

    def get_name(self):
        self.name = f"{self.level}_{self.category}"

    def get_random_question(self):
        all_values = self.get_all_values()
        random_number = randrange(len(all_values) - 1) + 1
        question_data = all_values[random_number]
        return Question(
            question_data[0], question_data[1:5], question_data[-1], self.level
        )


class UserDataSheet(Sheet):
    """
    This class for UserDataSheet object which extends Sheet class
    so it is a subclass from superclass "Sheet"
    Its constructor contains username which supposed to be unique
    to differentiate between users
    It contains a function for retrieving the user data from User worksheet
    and also contains another function to update the sheet with
    new records of the user
    """

    def __init__(self, username):
        self.username = username
        super().__init__("users")

    def get_user_data(self):
        all_users = self.get_all_values()
        user_data = ""
        user_id = 1
        for user in all_users:
            if user[0] == self.username:
                user_data = user
                return User(user_data[0], user_data[1], user_data[2], user_id)
            user_id += 1
        user = User(self.username, 1, 0, user_id)
        self.create_user(user)
        return user

    def update_user_sheet(self, User):
        worksheet_to_update = self.connetion.worksheet("users")
        worksheet_to_update.update_acell(f"B{User.id}", User.question_number)
        worksheet_to_update.update_acell(f"C{User.id}", User.points)

    def create_user(self, User):
        worksheet_to_update = self.connetion.worksheet("users")
        user_row = [User.username, User.question_number, User.points]
        worksheet_to_update.append_row(user_row)
