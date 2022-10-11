from stack import *
from printOps import *

ARITHMETIC_OPERATORS = ['+', '-', '*', '/']
STACK_OPERATORS = ['dup', 'swap', 'over', 'rot', 'drop', 'nip', 'tuck', '-rot', '2swap', '2dup', '2over', '2drop']
PRINT_OPERATORS = ['spaces', 'emit']
USER_WORDS = []
USER_WORD_DEFINITIONS = {} # USER_WORD: command string

def tokenize(line):
    return line.split()

def parse_tokens(stack, tokens):
    for token in tokens:
        token = token.lower()
        if token.isnumeric():
            stack.append(float(token))
        elif token in ARITHMETIC_OPERATORS:
            stack = perform_arithmetic(stack, token)
        elif token in STACK_OPERATORS:
            stack = perform_stack_operation(stack, token)
        elif token in PRINT_OPERATORS:
            perform_print_operation(stack, token)
        elif token == ':':
            print('Defining a new word')
            # Append the next token to USER_WORDS
            # Add the rest of the string after the USER_WORD as a value in USER_WORD_DEFINITIONS
        elif token == 'print':
           print(stack[-1])

    return stack

def perform_arithmetic(stack, operator):
    if operator == '+':
        result = stack.pop() + stack.pop()
    elif operator == '-':
        result = stack.pop() - stack.pop()
    elif operator == '*':
        result = stack.pop() * stack.pop()
    elif operator == '/':
        result = stack.pop() / stack.pop()

    stack.append(result)
    return stack

def perform_stack_operation(stack, operator):
    if operator == 'dup':
        return dup(stack)
    elif operator == 'swap':
        return swap(stack)
    elif operator == 'over':
        return over(stack)
    elif operator == 'rot':
        return rot(stack)
    elif operator == 'drop':
        return drop(stack)
    elif operator == 'nip':
        return nip(stack)
    elif operator == 'tuck':
        return tuck(stack)
    elif operator == '-rot':
        return minusRot(stack)
    elif operator == '2dup':
        return twoDup(stack)
    elif operator == '2swap':
        return twoSwap(stack)
    elif operator == '2over':
        return twoOver(stack)
    elif operator == '2drop':
        stack = drop(stack)
        return drop(stack)
    else:
        return stack

def perform_print_operation(stack, operator):
    if operator == 'spaces':
        print(spaces(stack[-1]))
    elif operator == 'emit':
        print(emit(stack[-1]))
