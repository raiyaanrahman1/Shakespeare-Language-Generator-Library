from .action import Action
from ...utils import Utils

class NumericOutputAction(Action):
    def __init__(self, you_or_thou='you', punctuation='!') -> None:
        requirements = {'you_or_thou': you_or_thou}
        Utils.check_requirements(requirements)
        your_or_thy = 'your' if you_or_thou == 'you' else 'thy'
        
        super().__init__(f'Open {your_or_thy} heart', punctuation)