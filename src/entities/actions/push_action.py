from action import Action
from ...utils import Utils

class PushAction(Action):
    def __init__(self, you_or_thou, punctuation='!') -> None:
        requirements = {'you_or_thou': you_or_thou}
        Utils.check_requirements(requirements)

        yourself = 'yourself' if you_or_thou == 'you' else 'thyself'
        super().__init__(f'Remember {yourself}', punctuation)