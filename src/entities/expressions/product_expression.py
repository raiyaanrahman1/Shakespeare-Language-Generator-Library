from .arithmetic_expression import ArithmeticExpression

class ProductExpression(ArithmeticExpression):
    def __init__(self, expr1, expr2) -> None:
        super().__init__(expr1, expr2, 'the product of ')