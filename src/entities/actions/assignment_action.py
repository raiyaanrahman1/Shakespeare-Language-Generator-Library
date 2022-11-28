from action import Action
from ...utils import Utils

class AssignmentAction(Action):
    def __init__(self, number, you_or_thou='thou', punctuation='!',) -> None:
        requirements = {'you_or_thou': you_or_thou}
        Utils.check_requirements(requirements)

        you = 'You' if you_or_thou == 'you' else 'Thou'
        are = 'are' if you_or_thou == 'you' else 'art'
        super().__init__(f"{you} {are} a {str(number)}", punctuation)