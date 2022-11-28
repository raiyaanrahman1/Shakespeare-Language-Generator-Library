from .arithmetic_expression import ArithmeticExpression

class SumExpression(ArithmeticExpression):
    def __init__(self, expr1, expr2) -> None:
        super().__init__(expr1, expr2, 'the sum of ')