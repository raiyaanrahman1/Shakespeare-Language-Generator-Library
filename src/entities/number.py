SPECIAL_NOUNS = ['Heaven', 'Hell', 'Microsoft']
SPECIAL_ADJECTIVES = ['honest']
VOWELS = ['a', 'e', 'i', 'o', 'u']

class Number:
    def __init__(self, numeric_value, adjectives, noun) -> None:
        self.numeric_value = numeric_value
        if numeric_value == 0:
            self.spl_value = 'nothing'
            return
        word_article = self.get_word_article(noun, adjectives)
        if len(adjectives) == 0:
            self.spl_value = f"{word_article}{noun}"
            return
        self.spl_value = f"{word_article}{' '.join(adjectives)} {noun}"
        

    def __str__(self) -> str:
        return self.spl_value

    def get_word_article(self, noun, adjectives):
        if noun in SPECIAL_NOUNS and len(adjectives) == 0:
            return ''
        first_word = noun if len(adjectives) == 0 else adjectives[0]
        if len(adjectives) != 0 and first_word in SPECIAL_ADJECTIVES:
            return 'an '
        if any([first_word.lower().startswith(vowel) for vowel in VOWELS]):
            return 'an '
        return 'a '
        