from src.builders.number_builder import NumberBuilder
from pprint import pprint


# for i in range(10):
#     print(f"{i}: {str(NumberBuilder(i, 'positive').build_expression())}")
#     print()

print(str(NumberBuilder(-7, 'positive').build_expression()))