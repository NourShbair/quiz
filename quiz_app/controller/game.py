from quiz_app.model.sheet import QuestionSheet
from quiz_app.view.printer import colored_print
from quiz_app.view.printer import colored_print_fb

from quiz_app.view import constants

def get_question(question_number):
    """
    This method to retrieve a random question from a specified sheet
    depending on question number, and using difficulty level and question category
    """
    level_cat_arr = [("easy","science"),("easy","history"),("easy","shows"),
    ("medium","science"),("medium","history"),("medium","shows"),
    ("hard","science"),("hard","history"),("hard","shows")]
    level,category= level_cat_arr[question_number-1]
    question = QuestionSheet(level, category)
    retrieved_question = question.get_random_question()
    colored_print(f"{question_number}. {retrieved_question}",constants.CYAN,"center")
    order = 1
    answers_to_print = ""
    for ans in retrieved_question.answers:
        #print the answers in the same line using "end" attribute
        answers_to_print = answers_to_print + str(order)+". " + ans.text + "      "
        order += 1
    colored_print(answers_to_print,constants.WHITE,"center")
    return retrieved_question

def validate_answer(question, answer):
    """
    Inside the try, converts string value into int.
    Raises ValueError if strings cannot be converted into int,
    or if it is not one of 4 answers options (1,2,3,4).
    """
    possible_answers = [1,2,3,4]
    ans = int(answer)
    if ans not in possible_answers:
        colored_print("Invalid data: Exactly a number from 1 to 4 is required, please try again:",constants.YELLOW,"center")
        print("\n")
        ans = input("",constants.CENTER_SPACE)
        return validate_answer(question, ans)
    else:
        entered_answer = question.answers[ans-1]
        if entered_answer.is_correct():
            print("Correct")
            return True
        else:
            return False



def continue_play(user,user_data,question):
    while True:
        print("\n")
        colored_print("Please Enter Your Answer:",constants.MAGENTA,"center")
        answer = int(input(constants.CENTER_SPACE))
        max_points, min_points = question.calculate_question_points()
        if validate_answer(question, answer):
            user_data.points += max_points
            user_data.question_number +=1
            user.update_user_sheet(user_data)
            next_question = get_question(user_data.question_number)
        else:
            colored_print("Incorrect, please try again:",constants.RED,"center")
            second_answer = int(input("\n",constants.CENTER_SPACE))
            if validate_answer(question, second_answer):
                user_data.points += min_points
                user_data.question_number +=1
                user.update_user_sheet(user_data)
                next_question = get_question(user_data.question_number)
            else:
                exit(0)
            

def start_play(user):
    user_data = user.get_user_data()
    print("\n")
    colored_print("Retrieving question...",constants.YELLOW,"center")
    print("\n")
    question = get_question(user_data.question_number)
    continue_play(user,user_data,question)




