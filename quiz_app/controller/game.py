from quiz_app.model.sheet import QuestionSheet

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
    print(retrieved_question)
    order = 1
    for ans in retrieved_question.answers:
        print(f"{order}. {ans}")
        order += 1
    return retrieved_question

def validate_answer(question, answer):
    entered_answer = question.answers[answer-1]
    if entered_answer.is_correct():
        print("Correct")
        return True
    else:
        return False 

def continue_play(user,user_data,question):
    while True:
        answer = int(input("Please Enter The Number Of The Correct Answer:\n"))
        max_points, min_points = question.calculate_question_points()
        if validate_answer(question, answer):
            user_data.points += max_points
            user_data.question_number +=1
            user.update_user_sheet(user_data)
            next_question = get_question(user_data.question_number)
        else:
            second_answer = int(input("Incorrect, please try again:\n"))
            if validate_answer(question, second_answer):
                user_data.points += min_points
                user_data.question_number +=1
                user.update_user_sheet(user_data)
                next_question = get_question(user_data.question_number)
            else:
                exit(0)
            

def start_play(user):
    user_data = user.get_user_data()
    print("Retrieving question...\n")
    question = get_question(user_data.question_number)
    continue_play(user,user_data,question)




