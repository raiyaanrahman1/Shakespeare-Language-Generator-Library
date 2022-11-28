from src.builders.number_builder import NumberBuilder
from src.entities.actions.assignment_action import AssignmentAction
from src.entities.scenes.phrase_gen_scene import PhraseGenScene
from src.entities.expressions.sum_expression import SumExpression
from src.entities.number import Number
from pprint import pprint


# for i in range(10):
#     print(f"{i}: {str(NumberBuilder(i, 'positive').build_expression())}")
#     print()

# print(str(NumberBuilder(-7, 'positive').build_expression()))


# action = AssignmentAction(SumExpression(SumExpression(Number(1, [], 'pig'), Number(1, [], 'pig')), Number(1, [], 'pig')))
# print(str(action))

lines = PhraseGenScene(['Romeo', 'Juliet'], 'positive', 'Romeo, O Romeo, where art thou?').generate_phrase()

for line in lines:
    print(str(line))