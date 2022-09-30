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

def test_perform_stack_operation_swap():
    stack = ['1.0', '2.0']
    operator = 'swap'
    result = perform_stack_operation(stack, operator)

    assert result == ['2.0', '1.0']

def test_perform_stack_operation_over():
    stack = ['1.0', '2.0']
    operator = 'over'
    result = perform_stack_operation(stack, operator)

    assert result == ['1.0', '2.0', '1.0']

def test_perform_stack_operation_rot():
    stack = ['1.0', '2.0', '3.0']
    operator = 'rot'
    result = perform_stack_operation(stack, operator)

    assert result == ['2.0', '3.0', '1.0']

def test_perform_stack_operation_drop():
    stack = ['1.0', '2.0', '3.0']
    operator = 'drop'
    result = perform_stack_operation(stack, operator)

    assert result == ['1.0', '2.0']

def test_perform_stack_operation_nip():
    stack = ['1.0', '2.0', '3.0']
    operator = 'nip'
    result = perform_stack_operation(stack, operator)

    assert result == ['1.0', '3.0']

def test_perform_stack_operation_tuck():
    stack = ['1.0', '2.0', '3.0']
    operator = 'tuck'
    result = perform_stack_operation(stack, operator)

    assert result == ['1.0', '3.0', '2.0', '3.0']

def test_perform_stack_operation_minusRot():
    stack = ['1.0', '2.0', '3.0']
    operator = '-rot'
    result = perform_stack_operation(stack, operator)

    assert result == ['3.0', '1.0', '2.0']
    
def test_perform_stack_operation_2dup():
    stack = ['1.0', '2.0', '3.0']
    operator = '2dup'
    result = perform_stack_operation(stack, operator)

    assert result == ['1.0', '2.0', '3.0', '2.0', '3.0']

def test_perform_stack_operation_2swap():
    stack = ['1.0', '2.0', '3.0', '4.0']
    operator = '2swap'
    result = perform_stack_operation(stack, operator)

    assert result == ['3.0', '4.0', '1.0', '2.0']

def test_perform_stack_operation_2over():
    stack = ['1.0', '2.0', '3.0', '4.0']
    operator = '2over'
    result = perform_stack_operation(stack, operator)

    assert result == ['1.0', '2.0', '3.0', '4.0', '1.0' , '2.0']

def test_perform_stack_operation_2drop():
    stack = ['1.0', '2.0', '3.0']
    operator = '2drop'
    result = perform_stack_operation(stack, operator)

    assert result == ['1.0']
