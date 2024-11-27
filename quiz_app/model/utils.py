class Printable:
    """
    This class to convert any object to string so it can be printed
    """

    def __init__(self):
        self.text = ""

    def __str__(self):
        return self.text
