from .action import Action

class StringOutputAction(Action):
    def __init__(self, punctuation='!') -> None:
        super().__init__('Speak your mind', punctuation)