
class User:
    """
    This class for User object,
    and it contains the user data which are:
    username: str, question_number: int, points: int
    """
    def __init__(self, username, question_number, points):
        self.username = username
        self.question_number = int(question_number)
        self.points = int(points)
        