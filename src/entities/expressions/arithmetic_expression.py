from ..number import Number

class ArithmeticExpression:
    def __init__(self, expr1, expr2, prefix) -> None:
        value = prefix

        if not isinstance(expr1, Number):
            value = value.rstrip() + '\n'
        value += str(expr1)

        value += ' and '

        if not isinstance(expr2, Number):
            value = value.rstrip() + '\n'
        value += str(expr2)

        self.value = value

    def __str__(self) -> str:
        return self.value
        