from asciiLookup import *

def spaces(count):
    spaces_str = ''
    for i in range(count):
        spaces_str += ' '
    return spaces_str

def emit(value):
    return ASCII_TABLE.get(value, '')

def cr():
    return "\n"
