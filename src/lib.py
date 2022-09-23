ARITHMETIC_OPERATORS = ['+', '-', '*', '/']
STACK_OPERATORS = ['dup']

def tokenize(line):
    return line.split()

def parse_tokens(stack, tokens):
    for token in tokens:
        if token.isnumeric():
            stack.append(float(token))
        elif token in ARITHMETIC_OPERATORS:
            stack = perform_arithmetic(stack, token)
        elif token in STACK_OPERATORS:
            stack = perform_stack_operation(stack, token)
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
        result = stack.pop()
        stack.append(result)
        stack.append(result)

    return stack
 
