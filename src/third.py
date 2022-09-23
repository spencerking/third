from lib import *

def main():
    stack = []
    example_input = '15 dup + print'
    tokens = tokenize(example_input)
    stack = parse_tokens(stack, tokens)
    
main()
