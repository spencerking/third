ARITHMETIC_OPERATORS = ['+', '-', '*', '/']
STACK_OPERATORS = ['dup', 'swap', 'over', 'rot', 'drop', '2swap', '2dup', '2over', '2drop']

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
    elif operator == 'swap':
        oldTop = stack.pop()
        newTop = stack.pop()
        stack.append(oldTop)
        stack.append(newTop)
    elif operator == 'over':
        oldTop = stack.pop()
        sandwich = stack.pop()
        stack.append(sandwich)
        stack.append(oldTop)
        stack.append(sandwich)
    elif operator == 'rot':
        oldTop = stack.pop()
        oldMiddle = stack.pop()
        oldBottom = stack.pop()
        stack.append(oldMiddle)
        stack.append(oldTop)
        stack.append(oldBottom)
    elif operator == 'drop':
        stack.pop()
    elif operator == '2dup':
        top = stack.pop()
        bottom = stack.pop()
        stack.append(bottom)
        stack.append(top)
        stack.append(bottom)
        stack.append(top)
    elif operator == '2swap':
        oldTopTop = stack.pop()
        oldTopBottom = stack.pop()
        oldBottomTop = stack.pop()
        oldBottomBottom = stack.pop()
        stack.append(oldTopBottom)
        stack.append(oldTopTop)
        stack.append(oldBottomBottom)
        stack.append(oldBottomTop)
    elif operator == '2over':
    	oldTopTop = stack.pop()
    	oldTopBottom = stack.pop()
    	sandwichTop = stack.pop()
    	sandwichBottom = stack.pop()
    	stack.append(sandwichBottom)
    	stack.append(sandwichTop)
    	stack.append(oldTopBottom)
    	stack.append(oldTopTop)
    	stack.append(sandwichBottom)
    	stack.append(sandwichTop)
    elif operator == '2drop':
        stack.pop()
        stack.pop()

    return stack
