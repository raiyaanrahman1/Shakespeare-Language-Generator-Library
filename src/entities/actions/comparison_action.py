from .action import Action
from ..number import Number
from ..expressions.arithmetic_expression import ArithmeticExpression
from ..character import Character
from typing import Union, Literal

Unit = Union[Number, ArithmeticExpression, Character]
CompOp = Union[Unit, Literal['I', 'you', 'yourself', 'me', 'myself']]


class ComparisonAction(Action):
    def __init__(self, comparison_operator, operand1: CompOp, operand2: CompOp) -> None:
        self.validate(comparison_operator, operand1, operand2)
        operator_to_words = {
            '>': 'better than',
            '<': 'worse than',
            '=': 'as good as'
        }

        is_ = 'Is'
        if str(operand1) == 'I':
            is_ = 'Am'
        elif str(operand1) == 'you':
            is_ = 'Are'
        
        super().__init__(f'{is_} {str(operand1)} {operator_to_words[comparison_operator]} {str(operand2)}', '?')

    
    def validate(self, comparison_operator, operand1, operand2):
        if comparison_operator not in ('>', '<', '='):
            raise Exception(f"Invalid comparison operator {comparison_operator}, expecting '>', '<', or '='")
        
        for op in (operand1, operand2):
            if (
                not isinstance(op, (Number, ArithmeticExpression, Character))
                or op not in ('I', 'you', 'yourself', 'me', 'myself')                
            ):
                raise Exception(f'Invalid operand {op}')
