#!/usr/bin/env python3

import ast
import math
import operator
from random import randrange

Constants = {
    'e': math.e,
    'pi': math.pi,
    'rand': randrange(100)
}

arithmetic_ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    # '/': operator.div,
    '!': operator.not_,
    '!=': operator.is_not,
}

math_ops = {
    'fact': math.factorial,
    'sqrt': math.sqrt,
    'exp': math.exp,
    'ln': math.log10,
    'log': math.log,
    'pow': math.pow
}


# TODO : validate expression
def valid_rpn(expression):
    pass


def evaluate_expression(expression):
    items = expression.split()
    stack = []
    for counter, item in enumerate(items):
        const = Constants.get(item)
        if not (item.isdigit() or const):
            operation = arithmetic_ops.get(item) or math_ops.get(item)
            operands = (stack.pop(), stack.pop()) if len(stack) > 1 else stack.pop()
            if type(operands) == tuple:
                result = operation(*operands)
            else:
                result = operation(operands)
            stack.append(result)
        else:
            stack.append(const or ast.literal_eval(item))
    return stack.pop()


if __name__ == '__main__':
    expression = input('> ')
    quit = ["exit", "quit"]
    while expression not in quit:
        print(evaluate_expression(expression))
        expression = input('> ')
