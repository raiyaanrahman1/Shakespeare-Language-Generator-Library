from ..utils import Utils
from ..entities.number import Number
from ..entities.expressions.sum_expression import SumExpression
from ..entities.expressions.product_expression import ProductExpression
from copy import copy
import random

nouns = {'positive': [], 'negative': [], 'neutral': []}
adjectives = {'positive': [], 'negative': [], 'neutral': []}
word_types = {'nouns': nouns, 'adjectives': adjectives}
for word_type in word_types:
    for tone in ('positive', 'negative', 'neutral'):
        dic = word_types[word_type]
        with open(f'./{word_type}/{tone}_{word_type}.txt') as file:
            words = [line.strip() for line in file]
        dic[tone] = words

class NumberBuilder:
    def __init__(self, number_to_build, tone) -> None:
        self.number_to_build = number_to_build
        self.tone = tone

    def build_expression(self) -> None:
        Utils.check_requirements({'tone': self.tone})

        if self.number_to_build == 0:
            return Number(self.number_to_build, [], None)

        binary = bin(self.number_to_build)[2:]
        
        numbers = [self.build_power_of_two(2**i, self.tone) for i, bit in enumerate(binary[::-1]) if int(bit) == 1]

        if len(numbers) == 1:
            return numbers[0]

        sum_exprs = []
        
        extra_num = None
        for i in range(0, len(numbers), 2):
            if i == len(numbers) - 1:
                extra_num = numbers[i]
            else:
                sum_exprs.append(SumExpression(numbers[i], numbers[i + 1]))

        while len(sum_exprs) > 1:
            temp = []
            for i in range(0, len(sum_exprs), 2):
                temp.append(SumExpression(sum_exprs[i], sum_exprs[i + 1]))
            sum_exprs = temp

        if extra_num is not None:
            expr = SumExpression(sum_exprs[0], extra_num)
        else:
            expr = sum_exprs[0]

        if self.tone == 'negative':
            expr = ProductExpression(expr, self.build_power_of_two(1, self.tone))

        return expr

    def build_power_of_two(self, num, tone):
        phrase_noun = random.choice(nouns[tone])
        phrase_adjs = []

        temp = num
        adjs_copy = copy(adjectives[tone])
        while temp / 2 >= 1:
            index = random.randint(0, len(adjs_copy) - 1)
            phrase_adjs.append(adjs_copy[index])
            adjs_copy.pop(index)
            temp = temp // 2

        return Number(num, phrase_adjs, phrase_noun)