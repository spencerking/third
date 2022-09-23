from lib import *

def test_tokenize():
    input = '15 dup + print'
    result = tokenize(input)

    assert result == ['15', 'dup', '+', 'print']

def test_parse_tokens():
    stack = []
    tokens = ['15', 'dup', '+']
    result = parse_tokens(stack, tokens)

    assert result == [30.0]

def test_perform_arithmetic_addition():
    stack = [1.0, 1.0]
    operator = '+'
    result = perform_arithmetic(stack, operator)
    
    assert result == [2.0]

def test_perform_arithmetic_subtraction():
    stack = [1.0, 4.0]
    operator = '-'
    result = perform_arithmetic(stack, operator)
    
    assert result == [3.0]

def test_perform_arithmetic_multiplication():
    stack = [2.0, 5.0]
    operator = '*'
    result = perform_arithmetic(stack, operator)
    
    assert result == [10.0]

def test_perform_arithmetic_division():
    stack = [4.0, 100.0]
    operator = '/'
    result = perform_arithmetic(stack, operator)
    
    assert result == [25.0]

def test_perform_stack_operation_dup():
    stack = ['4.0']
    operator = 'dup'
    result = perform_stack_operation(stack, operator)

    assert result == ['4.0', '4.0']
