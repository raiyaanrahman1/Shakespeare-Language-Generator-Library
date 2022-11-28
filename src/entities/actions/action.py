class Action:
    def __init__(self, message, punctuation = '!') -> None:
        self.message = message
        self.punctuation = punctuation

    def __str__(self) -> str:
        return f'{self.message}{self.punctuation}'