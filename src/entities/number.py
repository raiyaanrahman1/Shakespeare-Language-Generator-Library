class Number:
    def __init__(self, numeric_value, adjectives, noun) -> None:
        if numeric_value == 0:
            self.spl_value = 'nothing'
        elif len(adjectives) == 0:
            self.spl_value = f"a {noun}"
        else:
            self.spl_value = f"a {' '.join(adjectives)} {noun}"
        self.numeric_value = numeric_value

    def __str__(self) -> str:
        return self.spl_value