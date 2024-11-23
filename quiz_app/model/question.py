
from .utils import Printable


class Question(Printable):
    """
    This class for Question object, which extends Printable class,
    so, it can be printed "convert it to string"
    And it contains the question text, and the array of possible answers, and the correct answer
    """
    # text: str, answers: [str], correct_answer: str
    def __init__(self, text, answers, correct_answer):
        self.text = text
        self.answers = []
        for answer in answers:
            # The Answer object has to vars, the answer text, and a flag to determine if it is the correct answer
            self.answers.append(Answer(answer, answer == correct_answer))
 
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

