
from .utils import Printable


class Question(Printable):
    """
    This class for Question object, which extends Printable class,
    so, it can be printed "convert it to string"
    And it contains the question text, and the array of possible answers, and the correct answer
    """
    # text: str, answers: [str], correct_answer: str, difficulty: str
    def __init__(self, text, answers, correct_answer, difficulty):
        self.text = text
        self.difficulty = difficulty
        self.answers = []
        for answer in answers:
            # The Answer object has to vars, the answer text, and a flag to determine if it is the correct answer
            self.answers.append(Answer(answer, answer == correct_answer))
 
    def calculate_question_points(self):
        if (self.difficulty == "easy"):
            max_points = 10
            min_points = 5
        elif (self.difficulty == "medium"):
            max_points = 30
            min_points = 15
        elif (self.difficulty == "hard"):
            max_points = 50
            min_points = 25
        else:
            raise Exception("Sorry, invalid data")
        return max_points, min_points

class Answer(Printable):
    """
    This class for Answer object, which extends Printable class,
    so, it can be printed "convert it to string"
    And it contains the answer text, and a flag to determine if it is the correct answer
    """  
    def __init__(self, text, is_correct):
        self.text = text
        self._is_correct = is_correct   
    def is_correct(self):
        return self._is_correct

