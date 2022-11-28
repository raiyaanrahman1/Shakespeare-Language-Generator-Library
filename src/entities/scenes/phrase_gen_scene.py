from .scene import Scene
from ..actions.assignment_action import AssignmentAction
from ...builders.number_builder import NumberBuilder
from ..actions.push_action import PushAction
from ..line import Line
import random

class PhraseGenScene(Scene):
    def __init__(self, characters, tone, phrase) -> None:
        super().__init__(characters)
        self.tone = tone
        self.phrase = phrase

    def generate_phrase(self, print_immediately=True):
        lines = []
        for letter in self.phrase[::-1]:
            assignment_action = self.generate_letter(letter)
            you_or_thou = random.choice(['you', 'thou'])
            punctuation = random.choice(['.', '!'])
            push_action = PushAction(you_or_thou, punctuation)
            lines.append(Line(self.characters[0], [assignment_action, push_action]))
        return lines

    def generate_letter(self, letter):
        if len(letter) != 1:
            raise Exception('Expected a string of length 1')

        if not (32 <= ord(letter) <= 126):
            raise Exception(f'{letter} is not a valid character: its ASCII value must be between 32 and 126 inclusive')
            
        num_expr = NumberBuilder(ord(letter), self.tone).build_expression()
        return AssignmentAction(num_expr)
        