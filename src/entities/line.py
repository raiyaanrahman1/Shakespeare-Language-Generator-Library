class Line:
    def __init__(self, character, actions) -> None:
        self.character = character
        self.actions = actions

    def __str__(self) -> str:
        return f'{self.character}:\n' + ''.join([('\t' + str(action) + '\n') for action in self.actions])