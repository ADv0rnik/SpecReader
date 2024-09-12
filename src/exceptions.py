class CustomException(Exception):
    def __init__(self):
        self.message = "Common exception"

    def __str__(self):
        return f"The function raised an error: {self.message}"


class NoArgumentException(CustomException):
    def __init__(self):
        self.message = "Tuple expected but no argument found"
